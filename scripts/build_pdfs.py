"""Build the Grande manual (default), another product, or all product manuals."""

import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main():
    base = yaml.safe_load((ROOT / "mkdocs.yml").read_text())
    products = {"color-kit-grande": None}
    for section in base["nav"]:
        if isinstance(section, dict) and "Guides" in section:
            for entry in section["Guides"]:
                for title, path in entry.items():
                    if isinstance(path, str):
                        products[Path(path).stem] = [{title: path}]

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--product", choices=products, default="color-kit-grande")
    parser.add_argument("--all", action="store_true", help="Build one English PDF per product")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "output/pdf")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    for product in products if args.all else [args.product]:
        config = yaml.safe_load((ROOT / "mkdocs.pdf.yml").read_text())
        config["INHERIT"] = str(ROOT / "mkdocs.yml")
        config["docs_dir"] = str(ROOT / "docs")
        config["theme"]["custom_dir"] = str(ROOT / "overrides")
        config["watch"] = []
        config["hooks"] = [str(ROOT / "scripts/pdf_hooks.py")]
        pdf = config["plugins"][0]["exporter"]["formats"]["pdf"]
        pdf["stylesheets"] = [str(ROOT / "resources/pdf.scss")]
        pdf["aggregator"]["output"] = product + ".pdf"
        if products[product] is not None:
            config["nav"] = products[product].copy()
            # Append matching hardware specs, where the website has them.
            specs = {"wifi-color-display-kit": "specs/wifi-color-display-kit.md",
                     "espaper-lite-kit": "specs/2_9-espaper-kit-dimensions.md",
                     "espaper-plus-kit": "specs/2_9-espaper-kit-dimensions.md"}
            if product in specs:
                config["nav"].append({"Hardware specifications": specs[product]})
        with tempfile.TemporaryDirectory(prefix="thingpulse-pdf-") as work:
            config["site_dir"] = str(Path(work) / "site")
            config_path = Path(work) / "mkdocs.yml"
            config_path.write_text(yaml.safe_dump(config, sort_keys=False))
            subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict", "-f", str(config_path)], cwd=ROOT, check=True)
            destination = args.output_dir / (product + ".pdf")
            shutil.copy2(Path(config["site_dir"]) / destination.name, destination)
            print(f"Created {destination}", flush=True)


if __name__ == "__main__":
    main()
