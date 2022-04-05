import sys

sys.path.append("..")

import inspect

import rest_vlc


def get_func_args(function):
    return inspect.getfullargspec(function).args


def remove_indent_and_new_line(text):
    return text.replace("    ", "").replace("\n","  \n")


def doc_to_markdown(function):
    return f"## `rest_vlc.VLC.{function.__name__}({','.join(get_func_args(function))})`  \n{remove_indent_and_new_line(function.__doc__)}\n"


markdown = "# VLC REST API  Here's list of APIS  \n"

properties = {
    "status": """
        Show the status & configurations inform of a dictionaries
        :return: dict
        """,
    "playlist": """
        Show the playlist and configurations inform of a dictionaries
        :return: dict
        """,
    "connectable": """
        Check if VLC REST API is running
        :return: bool
        """,
    "is_random": """
        A property to get the random state of VLC
        :return: bool
        """,
    "is_repeat_media": """
        A property to get the repeat state of VLC
        :return: bool
        """,
    "is_fullscreen": """
        Show the fullscreen status of VLC
        :return: bool
        """,
    "is_loop_queue": """
        A property to get the loop state of VLC
        :return: bool
        """,
    "is_paused": """
        Check if the media is actually paused or not. Returns bool indicate media is paused or not
        :return: bool
        """,
    "is_playing": """
        Show the playing status of VLC
        :return: bool
        """,
    "time": """
        Show the time of VLC
        :return: int
        """,
    "volume": """
        Show the volume of VLC
        :return: int
        """,
    "position": """
        Show the position of VLC
        :return: int
        """,
    "duration": """
        Show the duration of VLC
        :return: int
        """,
    "state": """
        Show the state of VLC
        :return: rest_vlc.VLC_State
        """,
}  # hard code this due to the fact that i can't access any of the properties of the class :(


for property in properties:
    markdown += (
        f"## `rest_vlc.VLC.{property}`  \n{remove_indent_and_new_line(properties[property])}\n"
    )

for function in rest_vlc.VLC.__dict__.values():
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


for property in properties:
    markdown += f"## `rest_vlc.Async_VLC.{property}`  \n{remove_indent_and_new_line(properties[property])}\n"

for function in rest_vlc.Async_VLC.__dict__.values():
    if callable(function) and function.__doc__:
        markdown += async_doc_to_markdown(function)

with open("./docs/async.md", "w") as f:
    f.write(markdown)
