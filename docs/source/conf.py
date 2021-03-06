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
#  style(reST):Change code-block->literalinclude #154

import os
import sys

sys.path.append(os.path.abspath("../.."))
# sys.path.append(os.path.abspath("../source/_static"))

# print("***********\nExecutable\n", sys.executable)
# print("\nPATHS\n", sys.path, "\n***********\n")
# -- Project information -----------------------------------------------------
__version__ = "0.7.1"

project = "Junction Box"
copyright = "2021, Mark Sevelj"
author = "Mark Sevelj"
# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "autoclasstoc",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
# Available styles ['default', 'emacs', 'friendly', 'colorful',
# 'autumn', 'murphy', 'manni', 'material', 'monokai', 'perldoc',
# 'pastie', 'borland', 'trac', 'native', 'fruity', 'bw', 'vim',
# 'vs', 'tango', 'rrt', 'xcode', 'igor', 'paraiso-light', 'paraiso-dark',
# 'lovelace', 'algol', 'algol_nu', 'arduino', 'rainbow_dash', 'abap',
# 'solarized-dark', 'solarized-light', 'sas', 'stata', 'stata-light',
# 'stata-dark', 'inkpot', 'zenburn', 'gruvbox-dark', 'gruvbox-light']
pygments_style = "monokai"
pygments_dark_style = "monokai"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"
# html_theme = "sphinx_rtd_theme"

html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Options for extensions configuration ------------------------------------

# sphinx-copybutton is a lightweight code-block copy button
# config options are here https://sphinx-copybutton.readthedocs.io/en/latest/
# This config removes Python Repl + continuation, Bash line prefixes,
# ipython and qtconsole + continuation, jupyter-console + continuation and preceding line numbers
copybutton_prompt_text = r"^\d|^.\d|^\d\d|^\d\d\d|>>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# datalad download-url http://www.tldp.org/LDP/Bash-Beginners-Guide/Bash-Beginners-Guide.pdf \
# --dataset . \
# -m "add beginners guide on bash" \
# -O books/bash_guide.pdf
# is correctly pasted with the following setting
copybutton_line_continuation_character = "\\"


autodoc_default_options = {
    "members": True,
    "special-members": True,
    "private-members": True,
    "inherited-members": True,
    "undoc-members": True,
    "exclude-members": "__weakref__",
}


autosummary_generate = True

autoclasstoc_sections = [
    "public-attrs",
    "public-methods",
    "private-attrs",
    "private-methods",
]

# Intersphinx settings

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.9", None),
    "django": (
        "https://docs.djangoproject.com/en/3.2",
        "https://docs.djangoproject.com/en/3.2/_objects",
    ),
}
