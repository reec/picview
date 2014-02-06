import sys
import os

sys.path.insert(0, os.path.abspath('../../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'picview.picview_settings_example'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
]


templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'


project = 'picview'
copyright = '2014, Wictor Olseryd'

version = '0.1.0'
release = '0.1.0'

exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'nature'
html_static_path = ['_static']
htmlhelp_basename = 'picviewdoc'



latex_elements = {}
latex_documents = [
  ('index', 'picview.tex', 'picview Documentation',
   'Wictor Olseryd', 'manual'),
]


man_pages = [
    ('index', 'picview', 'picview Documentation',
     ['Wictor Olseryd'], 1)
]


texinfo_documents = [
  ('index', 'picview', 'picview Documentation',
   'Wictor Olseryd', 'picview', 'One line description of project.',
   'Miscellaneous'),
]

intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'django': ('http://pillow.readthedocs.org/en/latest/', None),
    'PIL': ('http://pillow.readthedocs.org/en/latest/', None),
}
