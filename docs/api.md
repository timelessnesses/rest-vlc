# API Lists
Here's the full list of APIs:

## `rest_vlc.VLC`

This is our main class that wraps VLC REST api together.

### `rest_vlc.VLC.__init__(self,url:str,auth:requests.auth.BasicAuth=requests.auth.BasicAuth("",""))`

Initializes the class with the url of the VLC instance and the authentication.  
Will raise the `Exception` if the url is not valid or it is unconnectable.

### `rest_vlc.VLC.status(self) -> dict:`

A property that returns the status of the VLC instance as a dictionary.  
Here's an example of the returned dictionary:
```json
{
    "root": {
        "fullscreen": "0",
        "audiodelay": "0",
        "apiversion": "3",
        "currentplid": "3",
        "time": "73",
        "volume": "256",
        "length": "149",
        "random": "false",
        "audiofilters": {
            "filter_0": null
        },
        "rate": "1",
        "videoeffects": {
            "hue": "0",
            "saturation": "1",
            "contrast": "1",
            "brightness": "1",
            "gamma": "1"
        },
        "state": "playing",
        "loop": "true",
        "version": "3.0.16 Vetinari",
        "position": "0.49520301818848",
        "repeat": "false",
        "subtitledelay": "0",
        "equalizer": null,
        "information": {
            "category": [
                {
                    "@name": "meta",
                    "info": [
                        {
                            "@name": "date",
                            "#text": "1998"
                        },
                        {
                            "@name": "artwork_url",
                            "#text": "file:///C:/Users/moopi/AppData/Roaming/vlc/art/artistalbum/%E5%BA%83%E7%80%AC%E9%A6%99%E7%BE%8E/THE%20BEST%20_Love%20Winters_/art"
                        },
                        {
                            "@name": "artist",
                            "#text": "\u00e5\u00ba\u0083\u00e7\u0080\u00ac\u00e9\u00a6\u0099\u00e7\u00be\u008e"
                        },
                        {
                            "@name": "album",
                            "#text": "THE BEST &quot;Love Winters&quot;"
                        },
                        {
                            "@name": "track_number",
                            "#text": "8"
                        },
                        {
                            "@name": "filename",
                            "#text": "get down bitch.mp3"
                        },
                        {
                            "@name": "title",
                            "#text": "Promise"
                        },
                        {
                            "@name": "genre",
                            "#text": "JPop"
                        }
                    ]
                },
                {
                    "@name": "Stream 0",
                    "info": [
                        {
                            "@name": "Bitrate",
                            "#text": "192 kb/s"
                        },
                        {
                            "@name": "Codec",
                            "#text": "MPEG Audio layer 1/2 (mpga)"
                        },
                        {
                            "@name": "Channels",
                            "#text": "Stereo"
                        },
                        {
                            "@name": "Bits per sample",
                            "#text": "32"
                        },
                        {
                            "@name": "Sample rate",
                            "#text": "44100 Hz"
                        },
                        {
                            "@name": "Type",
                            "#text": "Audio"
                        }
                    ]
                }
            ]
        },
        "stats": {
            "lostabuffers": "0",
            "readpackets": "1761",
            "lostpictures": "0",
            "demuxreadbytes": "1801821",
            "demuxbitrate": "0.024042280390859",
            "playedabuffers": "2872",
            "demuxcorrupted": "0",
            "sendbitrate": "0",
            "sentbytes": "0",
            "displayedpictures": "0",
            "demuxreadpackets": "0",
            "sentpackets": "0",
            "inputbitrate": "0.024165192618966",
            "demuxdiscontinuity": "0",
            "averagedemuxbitrate": "0",
            "decodedvideo": "0",
            "averageinputbitrate": "0",
            "readbytes": "1803264",
            "decodedaudio": "5745"
        }
    }
}
```
This will make it easier to access the values.

### `rest_vlc.VLC.playlist(self) -> dict:`

This property returns the playlist as a dictionary.  

Here's an example of the returned dictionary:
```json
{
    "node": {
        "@ro": "rw",
        "@name": "",
        "@id": "0",
        "node": [
            {
                "@ro": "ro",
                "@name": "Playlist",
                "@id": "1",
                "leaf": {
                    "@ro": "rw",
                    "@name": "Promise",
                    "@id": "3",
                    "@duration": "149",
                    "@uri": "file:///F:/Desktop/music/get%20down%20bitch.mp3",
                    "@current": "current"
                }
            },
            {
                "@ro": "ro",
                "@name": "Media Library",
                "@id": "2"
            }
        ]
    }
}
```
This will make it easier to access the values.

### `rest_vlc.VLC.connectable(self) -> bool:`

This property returns `True` if the VLC instance is connectable and `False` otherwise.

### `rest_vlc.VLC.stop(self) -> bool:`

This function returns `True` if the media playback was stopped and `False` otherwise.

