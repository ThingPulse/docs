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
