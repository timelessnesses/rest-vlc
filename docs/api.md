
        VLC Class
        This class will initialize a VLC instance by connect to it using REST API w/ HTTP Basic Auth.
        This class is blocking.
        If you want to use asynchornous version please install
        `aiohttp <https://pypi.org/project/aiohttp/>`_
        :param url: VLC url
        :param auth: VLC auth
        :return: None
        
None

        Stop the current playing media and return back the boolean of the result
        :return: bool
        

        Clear the playlist and return back the boolean of the result
        :return: bool
        

        Play a media by uri and return back the boolean of the result if success or not
        :param uri: media uri
        :return: bool
        

        Append a media to the queue and return back the boolean of the result if success or not
        :param uri: media uri
        :return: bool
        

        Set the volume of VLC and return back the boolean of the result if success or not
        :param volume: volume value (0-512 = 0-200%)
        :return: bool
        

        Set the shuffle state of VLC and return back the boolean of the result if success or not
        :param random: random state
        :return: bool
        

        Set the repeat state of VLC and return back the boolean of the result if success or not
        :param repeat: repeat state
        :return: bool
        

        Set the loop state of VLC and return back the boolean of the result if success or not
        :param loop: loop state
        :return: bool
        

        Set the fullscreen state of VLC and return back the boolean of the result if success or not and the current state of the screen
        :return: bool, bool
        

        Set the subtitle file to show in the VLC and returns bool based on successful or not
        :return: bool
        

        Give the list of the files and return the dictionaries of XML
        :return: dict
        

        Revert to previous media and return if request was successful or not
        :return: bool
        

        Delete media off the playlist by finding with the specified URI. Returns bool indicate if request was successful or not
        

        Skip to next media and return if request was successful or not
        :return: bool
        

        Clear the histories. Returns boolean indicate request is successful or not
        :return: bool
        

        Pause the media playback. Returns bool indicate request was successful or not
        :return: bool
        

        Seeking between time in the media with required arg is time which is supported int,str and datetime.timedelta. Returns bool indicate requests was successful or not
        :return: bool
        
# VLC REST API  Here's list of APIS  
## `rest_vlc.VLC.__init__`  
        VLC Class
        This class will initialize a VLC instance by connect to it using REST API w/ HTTP Basic Auth.
        This class is blocking.
        If you want to use asynchornous version please install
        `aiohttp <https://pypi.org/project/aiohttp/>`_
        :param url: VLC url
        :param auth: VLC auth
        :return: None
          
## `rest_vlc.VLC.__encode_uri`  None  
## `rest_vlc.VLC.stop`  
        Stop the current playing media and return back the boolean of the result
        :return: bool
          
## `rest_vlc.VLC.clear_playlist`  
        Clear the playlist and return back the boolean of the result
        :return: bool
          
## `rest_vlc.VLC.play`  
        Play a media by uri and return back the boolean of the result if success or not
        :param uri: media uri
        :return: bool
          
## `rest_vlc.VLC.append_queue`  
        Append a media to the queue and return back the boolean of the result if success or not
        :param uri: media uri
        :return: bool
          
## `rest_vlc.VLC.set_volume`  
        Set the volume of VLC and return back the boolean of the result if success or not
        :param volume: volume value (0-512 = 0-200%)
        :return: bool
          
## `rest_vlc.VLC.set_random`  
        Set the shuffle state of VLC and return back the boolean of the result if success or not
        :param random: random state
        :return: bool
          
## `rest_vlc.VLC.set_repeat_media`  
        Set the repeat state of VLC and return back the boolean of the result if success or not
        :param repeat: repeat state
        :return: bool
          
## `rest_vlc.VLC.set_loop_queue`  
        Set the loop state of VLC and return back the boolean of the result if success or not
        :param loop: loop state
        :return: bool
          
## `rest_vlc.VLC.fullscreen`  
        Set the fullscreen state of VLC and return back the boolean of the result if success or not and the current state of the screen
        :return: bool, bool
          
## `rest_vlc.VLC.set_subtitle_file`  
        Set the subtitle file to show in the VLC and returns bool based on successful or not
        :return: bool
          
## `rest_vlc.VLC.browse`  
        Give the list of the files and return the dictionaries of XML
        :return: dict
          
## `rest_vlc.VLC.previous`  
        Revert to previous media and return if request was successful or not
        :return: bool
          
## `rest_vlc.VLC.delete`  
        Delete media off the playlist by finding with the specified URI. Returns bool indicate if request was successful or not
          
## `rest_vlc.VLC.next`  
        Skip to next media and return if request was successful or not
        :return: bool
          
## `rest_vlc.VLC.clear_history`  
        Clear the histories. Returns boolean indicate request is successful or not
        :return: bool
          
## `rest_vlc.VLC.pause`  
        Pause the media playback. Returns bool indicate request was successful or not
        :return: bool
          
## `rest_vlc.VLC.seek`  
        Seeking between time in the media with required arg is time which is supported int,str and datetime.timedelta. Returns bool indicate requests was successful or not
        :return: bool
          

