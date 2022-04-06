import sys

sys.path.append("..")

import inspect

import rest_vlc


def get_func_args(function):
    return inspect.getfullargspec(function).args


def remove_indent_and_new_line(text):
    return text.replace("    ", "").replace("\n", "  \n")


def doc_to_markdown(function):
    return f"## `rest_vlc.VLC.{function.__name__}({','.join(get_func_args(function))})`  \n{remove_indent_and_new_line(function.__doc__)}\n"


markdown = "# VLC REST API  Here's list of APIS  \n"


for property, val in rest_vlc.VLC.__dict__.items():
    if not callable(val):
        markdown += f"## `rest_vlc.VLC.{property}`  \n{remove_indent_and_new_line(val.__doc__)}\n"

for function in rest_vlc.VLC.__dict__.items():
    if callable(function) and function.__doc__:
        markdown += doc_to_markdown(function)
markdown += "  \n## Async  \n[Click this to go to the async version](https://rest-vlc.readthedocs.io/en/latest/async)"
markdown = markdown.lstrip()
with open("./docs/api.md", "w") as f:
    f.write(markdown)

# ---------------------------------------------

markdown = "# Async VLC REST API  Here's list of async APIS  \n"


def async_doc_to_markdown(function):
    return f"## `await rest_vlc.Async_VLC.{function.__name__}({', '.join(get_func_args(function))})`  \n{remove_indent_and_new_line(function.__doc__)}\n"


for property, val in rest_vlc.VLC.__dict__.items():
    if not callable(val):
        markdown += f"## `rest_vlc.VLC.{property}`  \n{remove_indent_and_new_line(val.__doc__)}\n"

for function in rest_vlc.Async_VLC.__dict__.values():
    if callable(function) and function.__doc__ and inspect.isawaitable(function):
        markdown += async_doc_to_markdown(function)
    elif callable(function) and function.__doc__:
        markdown += doc_to_markdown(function)

with open("./docs/async.md", "w") as f:
    f.write(markdown)
