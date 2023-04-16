# outline for a myst_nb project with sphinx
# build with: sphinx-build -nW --keep-going -b html . ./_build/html
#  .venvX/bin/sphinx-build  -nW --keep-going -b html . ./_build/html
html_favicon = 'favicon.ico'

language = 'en'

# html_static_path = ['_static']

project = 'Manim Share'
# copyright = ''
# author = ''
html_title = "Manim Share"

# specify project details
master_doc = "index"
project = "MyST-NB Quickstart"

# basic build settings
exclude_patterns = ["_build", "README.md"]
include_patterns = ["*.md", "*.ipynb"]

nitpicky = True

nb_execution_mode = "off"


# load extensions
extensions = ["myst_nb",
              "sphinx_copybutton"
]

# html_theme = 'furo'
html_theme = 'sphinx_book_theme'