# VLC REST API  Here's list of APIS  
## `rest_vlc.VLC.__module__`  
str(object='') -> str  
str(bytes_or_buffer[, encoding[, errors]]) -> str  
  
Create a new string object from the given object. If encoding or  
errors is specified, then the object must expose a data buffer  
that will be decoded using the given encoding and error handler.  
Otherwise, returns the result of object.__str__() (if defined)  
or repr(object).  
encoding defaults to sys.getdefaultencoding().  
errors defaults to 'strict'.
## `rest_vlc.VLC.__doc__`  
str(object='') -> str  
str(bytes_or_buffer[, encoding[, errors]]) -> str  
  
Create a new string object from the given object. If encoding or  
errors is specified, then the object must expose a data buffer  
that will be decoded using the given encoding and error handler.  
Otherwise, returns the result of object.__str__() (if defined)  
or repr(object).  
encoding defaults to sys.getdefaultencoding().  
errors defaults to 'strict'.
## `rest_vlc.VLC.is_playing`  
  
Check if VLC is playing or not  
:return: bool  

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

## `rest_vlc.VLC.is_loop_queue`  
  
A property to get the loop state of VLC  
:return: bool  

## `rest_vlc.VLC.is_fullscreen`  
  
Return the current state of VLC if VLC is in fullscreen returns true otherwise false  
:return: bool  

## `rest_vlc.VLC.is_paused`  
  
Check if the media is actually paused or not. Returns bool indicate media is paused or not  
:return: bool  

## `rest_vlc.VLC.time`  
  
Give the current time media is at (Unit seconds)  
:return: int, str  

## `rest_vlc.VLC.duration`  
  
Give how long media is. (Unit seconds)  
:return: int, str  

## `rest_vlc.VLC.position`  
  
Get current bar position (0,1)  
:return: float, str  

## `rest_vlc.VLC.state`  
  
Give current state of the playback.  
:return: str  

## `rest_vlc.VLC.volume`  
  
Get current playback's volume (0-512)  
:return: int  

## `rest_vlc.VLC.__dict__`  
dictionary for instance variables (if defined)
## `rest_vlc.VLC.__weakref__`  
list of weak references to the object (if defined)
  
## Async  
[Click this to go to the async version](https://rest-vlc.readthedocs.io/en/latest/async)