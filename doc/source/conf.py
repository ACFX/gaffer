# -*- coding: utf-8 -*-
#
# Gaffer documentation build configuration file, created by
# sphinx-quickstart on Tue Apr 12 15:50:27 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import json
import sys
import os
import re
import inspect
import docutils

import sphinx_rtd_theme

# To avoid needing to maintain a working sphinx install for the matrix
# of Gaffer python versions, we dump out version information into a
# generic form, so we can read it here.
with open( "./gafferVars.json" ) as f :
	gaffer = json.load( f )

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = gaffer["name"]
copyright = gaffer["copyright"].replace( "Copyright (c) ", "" )
author = u'John Haddon'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = gaffer["versionString"]
# The full version, including alpha/beta/rc tags.
release = gaffer["versionString"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
	'logo_only': True,
	'collapse_navigation': False
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#html_title = u'Gaffer v0.24.0.0'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/GafferLogoMini.svg"

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [ "_static" ]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Gafferdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
	(master_doc, 'Gaffer.tex', u'Gaffer Documentation',
	u'John Haddon', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
	(master_doc, 'gaffer', u'Gaffer Documentation',
	[author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
	(master_doc, 'Gaffer', u'Gaffer Documentation',
	author, 'Gaffer', 'One line description of project.',
	'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# Variables for string replacement functions

arnold_version = '7.1.1.1'
arnold_path_linux = '/opt/solidangle/arnold-{0}'.format( arnold_version )
arnold_path_osx = '/opt/solidangle/arnold-{0}'.format( arnold_version )

delight_version = '13.0.18'
delight_path_linux = '/opt/3delight-{0}'.format( delight_version )
delight_path_osx = '/opt/3delight-{0}'.format( delight_version )

tractor_version = '2.2'
tractor_path_linux = '/opt/pixar/Tractor-{0}'.format( tractor_version )
tractor_path_osx = '/Applications/pixar/Tractor-{0}'.format( tractor_version )

# Add the `myst_parser` extension, which adds a parser
# for MarkDown files with a `.md` extension.
extensions = [ "myst_parser" ]
myst_enable_extensions = [ "substitution" ]

class GafferTransform( docutils.transforms.Transform ) :

	default_priority = 1
	suffix_set = { "md" }

	def apply( self, *kw ) :

		for node in self.document.traverse( docutils.nodes.block_quote ) :

			# Convert block quotes beginning with "admonitionType :" to real
			# admonitions. This allows us to create admonitions in pure
			# Markdown, without resorting to `{eval-rst}` directives.

			if not len( node ) :
				continue

			if not isinstance( node[0], docutils.nodes.paragraph ) :
				continue

			if not isinstance( node[0][0], docutils.nodes.Text ) :
				continue

			partition = node[0][0].partition( ":" )
			if not partition[1] :
				continue

			admonitions = dict( inspect.getmembers( docutils.nodes, lambda x : inspect.isclass( x ) and issubclass( x, docutils.nodes.Admonition ) ) )

			admonition = partition[0].strip().lower()
			if admonition not in admonitions :
				continue

			node[0][0] = docutils.nodes.Text( partition[2] ) # Remove "admonition : " prefix
			node.replace_self( admonitions[admonition]( "", *node.children ) )

def gafferSourceSubstitutions( app, docName, source ) :

	source[0] = source[0].replace( "!GAFFER_VERSION!", gaffer["versionString"] )
	source[0] = source[0].replace( "!GAFFER_MILESTONE_VERSION!", str( gaffer["milestoneVersion"] ) )
	source[0] = source[0].replace( "!GAFFER_MAJOR_VERSION!", str( gaffer["majorVersion"] ) )
	source[0] = source[0].replace( "!GAFFER_MINOR_VERSION!", str( gaffer["minorVersion"] ) )
	source[0] = source[0].replace( "!GAFFER_PATCH_VERSION!", str( gaffer["patchVersion"] ) )

def thirdPartySourceSubtitutions( app, docName, source) :

	source[0] = source[0].replace( "!ARNOLD_VERSION!", arnold_version )
	source[0] = source[0].replace( "!ARNOLD_PATH_LINUX!", arnold_path_linux )
	source[0] = source[0].replace( "!ARNOLD_PATH_OSX!", arnold_path_osx )
	source[0] = source[0].replace( "!DELIGHT_VERSION!", delight_version )
	source[0] = source[0].replace( "!DELIGHT_PATH_LINUX!", delight_path_linux )
	source[0] = source[0].replace( "!DELIGHT_PATH_OSX!", delight_path_osx )
	source[0] = source[0].replace( "!TRACTOR_VERSION!", tractor_version )
	source[0] = source[0].replace( "!TRACTOR_PATH_LINUX!", tractor_path_linux )
	source[0] = source[0].replace( "!TRACTOR_PATH_OSX!", tractor_path_osx )

def setup( app ) :

	app.add_transform( GafferTransform )

	app.connect( "source-read", gafferSourceSubstitutions )
	app.connect( "source-read", thirdPartySourceSubtitutions )

	# Add the custom stylesheet; used in all .md and .rst files in source
	app.add_css_file( 'gaffer.css' )
	app.add_js_file( 'scrollspy.js' )
