# ThingPulse documentation

[![Build Status](https://travis-ci.org/ThingPulse/docs.svg?branch=master)](https://travis-ci.org/ThingPulse/docs)

[https://docs.thingpulse.com/](https://docs.thingpulse.com/)

## How to build this yourself

A Python 3 installation is required to build this documentation site. Prepare the environment with:

```
$ pip3 install -r requirements.txt
```

If `pip` points to a Python/pip 3 version you can of course also use that executable.

Then run

```
$ mkdocs serve --livereload
```

and open [http://127.0.0.1:8000]() in the browser of your choice.

**Note**

MkDocs supports hot-reloading changes. The `includes` folder is explicitly watched
so changes to shared instructions also rebuild the pages that include them.


## Product PDFs

PDF builds use [mkdocs-exporter](https://adrienbrignon.github.io/mkdocs-exporter/)
and its Chromium browser. Install the additional dependencies once:

```sh
python -m pip install -r requirements-pdf.txt
python -m playwright install chromium --with-deps
```

Build the English Color Kit Grande manual:

```sh
python scripts/build_pdfs.py
```

The result is `output/pdf/color-kit-grande.pdf`. It contains the ten current
Color Kit Grande chapters in navigation order and the OpenWeatherMap API-key
instructions as an appendix. It excludes the old single-page guide, German
duplicates, other products, and general site pages. The chapter allowlist is in
`mkdocs.pdf.yml`; update it when adding a Grande chapter. Video embeds become
clickable links, and all tabs are expanded for print. Links to documentation
pages open the online documentation; videos and external resources still need
an internet connection.

The same build command can also export the other products listed in the website
navigation, including matching hardware specifications where available:

```sh
python scripts/build_pdfs.py --product wifi-color-display-kit
python scripts/build_pdfs.py --all
python scripts/build_pdfs.py --help
```

These optional manuals use each product's guide (including its shared Markdown
includes); linked external documents are not bundled. PDF exports currently use
English source pages. The bilingual website build is unchanged.

Deployment builds the Grande PDF into `site/downloads/color-kit-grande.pdf`
after the normal website build. For a local export, use the default output
directory above; temporary HTML and chapter PDFs are automatically removed.
Generated PDFs are ignored by Git. To inspect the intermediate HTML manually,
run `mkdocs build -f mkdocs.pdf.yml` (outputs to `site-pdf/`).

Run the PDF scoping and print-conversion regression checks with
`python -m unittest discover -s scripts -p 'test_*.py'`. When changing the print
styles or exporter version, also render the Grande PDF and check the assembly
steps and long troubleshooting sections for missing content or clipping.

## Translations

English is the source language and keeps its existing URLs. German pages are
built under `/de/` using `mkdocs-static-i18n`. All 29 documentation pages and all
six shared instruction fragments have German translations, including the older
single-page Color Kit Grande guide. New pages without a German translation fall
back to English and display a German notice. Linked PDFs, screenshots, videos,
and external websites remain in their original language.

Add translations beside their English source: `assembly.md` becomes
`assembly.de.md`. Keep Markdown links language-neutral (`assembly.md`, not
`assembly.de.md`); the plugin resolves the language during the build. Share the
existing images and videos unless a localized asset is needed. Translate visible
text and image descriptions, but preserve commands, filenames, pin assignments,
and software UI labels. German instructions use informal “du” and Swiss Standard
German spelling (ss instead of ß).

When changing an English page or shared instruction fragment, update its German counterpart in
the same change. Check technical values, warnings, and step ordering against the
source. Preserve explicit heading IDs used by incoming links, or update all
affected links when translating headings.

Shared instructions live in `includes/`. German pages must explicitly include
the `.de.md` fragment, for example `{!../includes/install-drivers.de.md!}`;
the include extension does not select translations automatically. Preserve the
same heading IDs in both versions so existing section links keep working.

Navigation labels are configured under the German language's `nav_translations`
in `mkdocs.yml`. Explicit admonition titles should also be translated.

Run `mkdocs build --strict` and preview both languages with `mkdocs serve` before
publishing. Check language switching on individual pages, fallback notices,
heading links, tables, images, and video embeds.
