# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'DMtools'
# If specified, this will be used in the nav bar instead.
html_short_title = "DMtools"
copyright = '2023, momocoding'
author = 'momocoding'

# The full version, including alpha/beta/rc tags
release = '0.1'

# Or it can be a URL:
#html_logo = 'https://awesome.com/static/logo.png'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'sphinx.ext.mathjax'
#'sphinx.ext.imgmath'
]

mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS-MML_HTMLorMML'
imgmath_latex = '/usr/local/texlive/2023/bin/universal-darwin/latex'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# select the theme
html_theme = 'sphinx_rtd_theme'
#html_theme = 'sphinx_typo3_theme'
#html_theme = 'alabaster'
#html_theme = 'piccolo_theme'
#import sphinx_book_theme
#html_theme = 'sphinx_book_theme'
#html_theme_path = [sphinx_book_theme.get_html_theme_path()]
#from better import better_theme_path
#html_theme = 'better'
#html_theme_path = [better_theme_path]

html_theme_options = {
    "banner_text": 'Welcome to dmtools!',
    "banner_hiding": "permanent",
    "source_url": 'https://github.com/ZhouQiangwei/dmtools',
    "source_icon": "github"
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

## double dash -- of paramater will convert to one dash - 
smartquotes = False

# source_suffix = '.rst'
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']
