# VLC REST API  Here's list of APIS  
## `rest_vlc.VLC.status`  

Show the status & configurations inform of a dictionaries
:return: dict

## `rest_vlc.VLC.playlist`  

Show the playlist and configurations inform of a dictionaries
:return: dict

## `rest_vlc.VLC.connectable`  

Check if VLC REST API is running
:return: bool

## `rest_vlc.VLC.is_random`  

A property to get the random state of VLC
:return: bool

## `rest_vlc.VLC.is_repeat_media`  

A property to get the repeat state of VLC
:return: bool

## `rest_vlc.VLC.is_fullscreen`  

Show the fullscreen status of VLC
:return: bool

## `rest_vlc.VLC.is_loop_queue`  

A property to get the loop state of VLC
:return: bool

## `rest_vlc.VLC.is_paused`  

Check if the media is actually paused or not. Returns bool indicate media is paused or not
:return: bool

## `rest_vlc.VLC.is_playing`  

Show the playing status of VLC
:return: bool

## `rest_vlc.VLC.time`  

Show the time of VLC
:return: int

## `rest_vlc.VLC.volume`  

Show the volume of VLC
:return: int

## `rest_vlc.VLC.position`  

Show the position of VLC
:return: int

## `rest_vlc.VLC.duration`  

Show the duration of VLC
:return: int

## `rest_vlc.VLC.state`  

Show the state of VLC
:return: rest_vlc.VLC_State

## `rest_vlc.VLC.__init__(self,url,auth)`  

VLC Class
This class will initialize a VLC instance by connect to it using REST API w/ HTTP Basic Auth.
This class is blocking.
If you want to use asynchornous version please install
`aiohttp <https://pypi.org/project/aiohttp/>`_
:param url: VLC url
:param auth: VLC auth
:return: None

## `rest_vlc.VLC.stop(self)`  

Stop the current playing media and return back the boolean of the result
:return: bool

## `rest_vlc.VLC.clear_playlist(self)`  

Clear the playlist and return back the boolean of the result
:return: bool

## `rest_vlc.VLC.play(self,uri)`  

Play a media by uri and return back the boolean of the result if success or not
:param uri: media uri
:return: bool

## `rest_vlc.VLC.append_queue(self,uri)`  

Append a media to the queue and return back the boolean of the result if success or not
:param uri: media uri
:return: bool

## `rest_vlc.VLC.set_volume(self,volume,percent)`  

Set the volume of VLC and return back the boolean of the result if success or not
:param volume: volume value (0-512 = 0-200%)
:param percent: option for volume is actually percentage or not
:return: bool

## `rest_vlc.VLC.set_random(self,random)`  

Set the shuffle state of VLC and return back the boolean of the result if success or not
:param random: random state
:return: bool

## `rest_vlc.VLC.set_repeat_media(self,repeat)`  

Set the repeat state of VLC and return back the boolean of the result if success or not
:param repeat: repeat state
:return: bool

## `rest_vlc.VLC.set_loop_queue(self,loop)`  

Set the loop state of VLC and return back the boolean of the result if success or not
:param loop: loop state
:return: bool

## `rest_vlc.VLC.fullscreen(self)`  

Set the fullscreen state of VLC and return back the boolean of the result if success or not and the current state of the screen
:return: bool, bool

## `rest_vlc.VLC.set_subtitle_file(self,uri)`  

Set the subtitle file to show in the VLC and returns bool based on successful or not
:return: bool

## `rest_vlc.VLC.browse(self,uri)`  

Give the list of the files and return the dictionaries of XML
:return: dict

## `rest_vlc.VLC.previous(self)`  

Revert to previous media and return if request was successful or not
:return: bool

## `rest_vlc.VLC.delete(self,uri)`  

Delete media off the playlist by finding with the specified URI. Returns bool indicate if request was successful or not

## `rest_vlc.VLC.next(self)`  

Skip to next media and return if request was successful or not
:return: bool

## `rest_vlc.VLC.clear_history(self)`  

Clear the histories. Returns boolean indicate request is successful or not
:return: bool

## `rest_vlc.VLC.pause(self)`  

Pause the media playback. Returns bool indicate request was successful or not
:return: bool

## `rest_vlc.VLC.seek(self,time)`  

Seeking between time in the media with required arg is time which is supported int,str and datetime.timedelta. Returns bool indicate requests was successful or not
:return: bool

  
## Async  
[Click this to go to the async version](https://rest-vlc.readthedocs.io/en/latest/async)