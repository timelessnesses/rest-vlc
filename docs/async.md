# Async VLC REST API  Here's list of async APIS  
## `await rest_vlc.VLC.is_playing`  
  
Check if VLC is playing or not  
:return: bool  

## `await rest_vlc.VLC.status`  
  
Show the status & configurations inform of a dictionaries  
:return: dict  

## `await rest_vlc.VLC.playlist`  
  
Show the playlist and configurations inform of a dictionaries  
:return: dict  

## `await rest_vlc.VLC.connectable`  
  
Check if VLC REST API is running  
:return: bool  

## `await rest_vlc.VLC.is_random`  
  
A property to get the random state of VLC  
:return: bool  

## `await rest_vlc.VLC.is_repeat_media`  
  
A property to get the repeat state of VLC  
:return: bool  

## `await rest_vlc.VLC.is_loop_queue`  
  
A property to get the loop state of VLC  
:return: bool  

## `await rest_vlc.VLC.is_fullscreen`  
  
Return the current state of VLC if VLC is in fullscreen returns true otherwise false  
:return: bool  

## `await rest_vlc.VLC.is_paused`  
  
Check if the media is actually paused or not. Returns bool indicate media is paused or not  
:return: bool  

## `await rest_vlc.VLC.time`  
  
Give the current time media is at (Unit seconds)  
:return: int, str  

## `await rest_vlc.VLC.duration`  
  
Give how long media is. (Unit seconds)  
:return: int, str  

## `await rest_vlc.VLC.position`  
  
Get current bar position (0,1)  
:return: float, str  

## `await rest_vlc.VLC.state`  
  
Give current state of the playback.  
:return: str  

## `await rest_vlc.VLC.volume`  
  
Get current playback's volume (0-512)  
If you want percentage returns then set the property of `volume_percentage` to `True`  
:return: int  

## `rest_vlc.VLC.__init__(self,url,auth)`  
  
VLC Class  
This class will initialize a VLC instance by connect to it using REST API w/ HTTP Basic Auth.  
This class is blocking.  
If you want to use asynchornous version please install  
`aiohttp <https://pypi.org/project/aiohttp/>`_  
:param url: VLC url  
:param auth: VLC auth  
:return: None  

## `await rest_vlc.Async_VLC.stop(self)`  
  
Stop the current playing media and return back the boolean of the result  
:return: bool  

## `await rest_vlc.Async_VLC.clear_playlist(self)`  
  
Clear the playlist and return back the boolean of the result  
:return: bool  

## `await rest_vlc.Async_VLC.play(self, uri)`  
  
Play a media by uri and return back the boolean of the result if success or not  
:param uri: media uri  
:return: bool  

## `await rest_vlc.Async_VLC.append_queue(self, uri)`  
  
Append a media to the queue and return back the boolean of the result if success or not  
:param uri: media uri  
:return: bool  

## `await rest_vlc.Async_VLC.set_volume(self, volume, percent)`  
  
Set the volume of VLC and return back the boolean of the result if success or not  
:param volume: volume value (0-512 = 0-200%)  
:param percent: option for volume is actually percentage or not  
:return: bool  

## `await rest_vlc.Async_VLC.set_random(self, random)`  
  
Set the shuffle state of VLC and return back the boolean of the result if success or not  
:param random: random state  
:return: bool  

## `await rest_vlc.Async_VLC.set_repeat_media(self, repeat)`  
  
Set the repeat state of VLC and return back the boolean of the result if success or not  
:param repeat: repeat state  
:return: bool  

## `await rest_vlc.Async_VLC.set_loop_queue(self, loop)`  
  
Set the loop state of VLC and return back the boolean of the result if success or not  
:param loop: loop state  
:return: bool  

## `await rest_vlc.Async_VLC.fullscreen(self)`  
  
Set the fullscreen state of VLC and return back the boolean of the result if success or not and the current state of the screen  
:return: (bool, bool)  

## `await rest_vlc.Async_VLC.browse(self, uri)`  
  
Give the list of the files and return the dictionaries of XML  
:return: dict  

## `await rest_vlc.Async_VLC.previous(self)`  
  
Revert to previous media and return if request was successful or not  
:return: bool  

## `await rest_vlc.Async_VLC.delete(self, uri)`  
  
Delete media off the playlist by finding with the specified URI. Returns bool indicate if request was successful or not  

## `await rest_vlc.Async_VLC.next(self)`  
  
Skip to next media and return if request was successful or not  
:return: bool  

## `await rest_vlc.Async_VLC.clear_history(self)`  
  
Clear the histories. Returns boolean indicate request is successful or not  
:return: bool  

## `await rest_vlc.Async_VLC.pause(self)`  
  
Pause the media playback. Returns bool indicate request was successful or not  
:return: bool  

## `await rest_vlc.Async_VLC.seek(self, time)`  
  
Seeking between time in the media with required arg is time which is supported int,str and datetime.timedelta. Returns bool indicate requests was successful or not  
:return: bool  

