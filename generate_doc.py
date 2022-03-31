import sys

sys.path.append("..")

import rest_vlc
import inspect


def get_func_args(function):
    return inspect.getfullargspec(function).args


def remove_indentation(text):
    return text.replace("    ", "")


def doc_to_markdown(function):
    return f"## rest_vlc.VLC.{function.__name__}({','.join(get_func_args(function))})  \n{remove_indentation(function.__doc__)}\n"


markdown = "# VLC REST API  Here's list of APIS  \n"

for function in rest_vlc.VLC.__dict__.values():
    if callable(function) and function.__doc__:
        markdown += doc_to_markdown(function)
    elif function.__doc__:
        markdown += (
            f"## {function.__name__}  \n{remove_indentation(function.__doc__)}\n"
        )

markdown = markdown.lstrip()
print(markdown)
