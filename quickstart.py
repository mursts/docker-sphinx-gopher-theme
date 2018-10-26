#!/usr/bin/env python
# coding: utf-8

import copy
import os
import sys

from sphinx.cmd import quickstart
from sphinx.cmd.quickstart import generate


hook_d = {}


def monkey_patch_generate(d, overwrite=False, templatedir=None):
    global hook_d
    hook_d = copy.copy(d)

    generate(d, overwrite, templatedir)


def main(argv=sys.argv[1:]):
    global hook_d

    hook_d = {}
    quickstart.generate = monkey_patch_generate

    quickstart.main(argv)

    d = hook_d

    srcdir = d['sep'] and os.path.join(d['path'], 'source') or d['path']
    conf_path = os.path.join(srcdir, "conf.py")

    with open(conf_path, "a+") as f:
        conf_py = """

# ----- sphinxjp.themes.gopher
html_theme = "gopher"
extensions.append('sphinxjp.themes.gopher')
html_theme_options = {'note_enabled': True}
"""

        f.write(conf_py)

    if d['makefile'] is True:
        make_path = os.path.join(d['path'], 'Makefile')
        with open(make_path, "a+") as f:
            makefile = """

livehtml:
\tsphinx-autobuild -b html --host 0.0.0.0 $(SOURCEDIR) $(BUILDDIR)/html
"""
            f.write(makefile)


if __name__ == '__main__':
    main(sys.argv[1:])
