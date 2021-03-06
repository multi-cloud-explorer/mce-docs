# -- Path setup --------------------------------------------------------------

import os

os.environ['DATABASE_URL'] = 'sqlite:///db.sqlite3'
os.environ['DJANGO_SETTINGS_MODULE'] = 'mce_django_server.settings.doc'

#from mce_azure import core

import django
django.setup()

# -- Project information -----------------------------------------------------

project = 'multi-cloud-explorer'
copyright = '2020, stephane.rault'
author = 'stephane.rault'

release = "0.1.0"
version = release


# -- General configuration ---------------------------------------------------

master_doc = "index"

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints',
    'sphinx_rtd_theme',
    'sphinx.ext.extlinks',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']

exclude_patterns = []

#highlight_language = 'python'

todo_include_todos = False


# -- Options for HTML output -------------------------------------------------

# https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html

html_context = {
    "display_github": True, 
    "github_user": "multi-cloud-explorer", # Username
    "github_repo": "mce-docs", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/source/", # Path in the checkout to the docs root
}

html_theme = "sphinx_rtd_theme"

html_static_path = ['_static']

html_theme_options = {
    #'github_url': 'https://github.com/multi-cloud-explorer/mce-docs.git',
    'canonical_url': 'https://multi-cloud-explorer.readthedocs.io/',
    #'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    #'vcs_pageview_mode': 'display_github',
    #'style_nav_header_background': 'white',
    'collapse_navigation': True,
    #'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    #'titles_only': False
}

# -- Extension configuration -------------------------------------------------

# sphinx.ext.napoleon
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

intersphinx_mapping = {
    'python': ('http://docs.python.org/3.7', None),
    'django': ('http://docs.djangoproject.com/en/dev/', 'http://docs.djangoproject.com/en/dev/_objects/'),
}

# sphinx_autodoc_typehints
typehints_fully_qualified = True 
set_type_checking_flag = True
always_document_param_types = True

"""
extlinks = {
    'duwikipediafr': ('http://fr.wikipedia.org/wiki/'
                      '%s', ''),
    'duwikipediaen': ('http://en.wikipedia.org/wiki/'
                      '%s', ''),
    'rs-base': ('https://support.radical-spam.org/public/'
                      '%s', ''),
}
Je suis en :duwikipediafr:`France` depuis ...
"""

def setup(app):
    from recommonmark.transform import AutoStructify
    app.add_config_value('recommonmark_config', {
            'enable_eval_rst': True,
            'commonmark_suffixes': ['.md', '.hpp'],
            }, True)
    app.add_transform(AutoStructify)
