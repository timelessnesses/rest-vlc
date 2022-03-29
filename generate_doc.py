import sys

sys.path.append("..")

import rest_vlc


def doc_to_markdown(function):

    return f"## `rest_vlc.VLC.{str(function.__name__)}`  {str(function.__doc__)}  \n"


markdown = "# VLC REST API  Here's list of APIS  \n"

for function in rest_vlc.VLC.__dict__.values():
    if callable(function):
        print(function.__doc__)
        markdown += doc_to_markdown(function)

print(markdown)
