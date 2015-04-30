# BigSense Presentations

This repository contains presentations for BigSense which can be used when presenting at technology user-groups and meetups. It's built using [reveal.js](https://travis-ci.org/hakimel/reveal.js).

Individual slides are kept in the `slides` subfolder. The `sets` subfolder can be used define sets of slides and the `*.slides` file in the base directory are compiled by the `build.py` script into HTML files. Finally, the `publish` script builds all the static html and places it in the `gh-pages` branch so it's accessible via [bigsense.github.io](http://bigsense.github.io).

## Watchers

There are two watcher scripts, `watch.sh` and `watch.ps1` that can be run to automatically build the HTML files as changes are detected to the source files.
 
