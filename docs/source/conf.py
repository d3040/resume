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
import datetime
import pydata_sphinx_theme

td = datetime.date.today()
today_date = td.strftime('%Y%m%d')
today_year = td.strftime('%Y')
# -- Project information -----------------------------------------------------

project = 'Resume'
copyright = today_year + ', Daniel Clavijo'
author = 'Daniel Clavijo'

# The full version, including alpha/beta/rc tags
release = '1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'es'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_theme_options = {
    "use_fullscreen_button": False,
    "toc_title": "Secciones",
    "use_sidenotes": True,
    #"repository_url": "https://github.com/d3040/resume",
    #"use_repository_button": True,
    #"show_toc_level": 2,
    #"extra_navbar": "<p>test</p>"
    #"announcement": "My announcement!"
}
html_sidebars =  {
    #"**": [] # to disable left  sidebar
    "home_page_in_toc": True,
    "show_navbar_depth": 2,
    "max_navbar_depth": 4,
    "collapse_navbar": False,#True,
}
html_title = "d3040" #today_date
html_logo = "img/my_picture3.jpg" #"beaver.png"
html_favicon = "img/accessibility.svg"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_js_files = ['js/custom.js']
