"""Limit exports to the PDF navigation and make interactive content printable."""

from bs4 import BeautifulSoup
from mkdocs.plugins import event_priority
from urllib.parse import urlsplit, urlunsplit

selected_pages = set()

@event_priority(110)
def on_page_markdown(markdown, page, **kwargs):
    # MkDocs also builds pages outside nav; never let those into the PDF.
    page.meta["pdf"] = page.file.src_uri in selected_pages
    return markdown


def on_nav(nav, **kwargs):
    global selected_pages
    selected_pages = {page.file.src_uri for page in nav.pages}


def on_page_content(html, page, **kwargs):
    if not page.meta.get("pdf"):
        return html
    soup = BeautifulSoup(html, "html.parser")
    # Tabs need their labels as headings once every panel is visible in print.
    for tabs in soup.select(".tabbed-set"):
        labels = tabs.select(".tabbed-labels label")
        panels = tabs.select(".tabbed-content > .tabbed-block")
        for label, panel in zip(labels, panels):
            heading = soup.new_tag("h3")
            heading.string = label.get_text(" ", strip=True)
            panel.insert(0, heading)
    if page.file.src_uri.endswith("color-kit-grande/assembly.md"):
        for table in soup.find_all("table"):
            rows = table.find_all("tr")
            if len(rows) < 10:
                continue
            steps = soup.new_tag("div", attrs={"class": "pdf-steps"})
            for number, row in enumerate(rows, 1):
                step = soup.new_tag("div", attrs={"class": "pdf-step"})
                heading = soup.new_tag("h3")
                heading.string = f"Step {number}"
                step.append(heading)
                for cell in row.find_all(["th", "td"], recursive=False):
                    block = soup.new_tag("div")
                    block.extend(list(cell.contents))
                    step.append(block)
                steps.append(step)
            table.replace_with(steps)
    # Long troubleshooting rows can exceed a printed page. Paged.js can drop
    # such rows altogether, so present each symptom as an ordinary section.
    if page.file.src_uri.endswith("color-kit-grande/troubleshooting.md"):
        for table in soup.find_all("table"):
            sections = soup.new_tag("div", attrs={"class": "pdf-troubleshooting"})
            for row in table.select("tbody tr"):
                cells = row.find_all("td", recursive=False)
                if not cells:
                    continue
                heading = soup.new_tag("h3")
                heading.extend(list(cells[0].contents))
                sections.append(heading)
                for cell in cells[1:]:
                    paragraph = soup.new_tag("div")
                    paragraph.extend(list(cell.contents))
                    sections.append(paragraph)
            table.replace_with(sections)
    media = list(soup.find_all("iframe"))
    media += list(soup.find_all("img", alt="type:video"))
    for frame in media:
        url = frame.get("src", "")
        if not url:
            continue
        parts = urlsplit(url)
        if parts.hostname in {"www.youtube.com", "youtube.com"} and parts.path.startswith("/embed/"):
            query = "v=" + parts.path.removeprefix("/embed/")
            if parts.query:
                query += "&" + parts.query
            url = urlunsplit((parts.scheme, parts.netloc, "/watch", query, parts.fragment))
        link = soup.new_tag("a", href=url)
        link.string = "Watch video: " + link["href"]
        paragraph = soup.new_tag("p")
        paragraph.append(link)
        frame.replace_with(paragraph)
    return str(soup)


@event_priority(110)
def on_post_page(output, **kwargs):
    # Offline exports do not need website analytics or other remote scripts.
    soup = BeautifulSoup(output, "html.parser")
    for script in soup.find_all("script"):
        script.decompose()
    return str(soup)
