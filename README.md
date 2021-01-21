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
$ mkdocs serve
```

and open [http://127.0.0.1:8000]() in the browser of your choice.

**Note**

MkDocs supports hot-reloading changes. However, it does not reload master pages if one of the included pages changes. If you change any document in the `includes` folder you need to restart MkDocs to see those applied.
