project = "MRE"
copyright = "2021, Foo"
author = "Foo"

extensions = [
    "autoapi.extension",
]

autoapi_type = "python"
autoapi_dirs = ["../mre"]

templates_path = ["_templates"]

highlight_language = "python3"

add_module_names = False

autodoc_typehints = "signature"

exclude_patterns = []

html_theme = "alabaster"
html_static_path = []
