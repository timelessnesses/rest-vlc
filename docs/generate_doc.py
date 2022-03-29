import sys

sys.path.append("..")

import rest_vlc

apis = "# API Listing\nHere's a listing of APIs\n"

desc = ""


def generate(func):
    global apis
    for key, val in rest_vlc.__dict__.items():
        if key.startswith("__") or key in ("url", "auth", "full_screen"):
            continue
        if key == func:
            apis += f"##  `rest_vlc.VLC.{func}`\nDescription:  \n{val.__doc__}"


a = dir(rest_vlc.VLC)
a.append("VLC")
for element in a:
    generate(element)

with open("api.md", "w") as fp:
    fp.write(apis)
