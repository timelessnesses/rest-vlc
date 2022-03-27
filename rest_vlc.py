import requests
import xmltodict
import warnings

try:
    import aiohttp

    aiohttp_exists = True
except ImportError:
    aiohttp_exists = False


class VLC:
    def __init__(
        self,
        url: str = "http://localhost:8080",
        auth: requests.auth.HTTPBasicAuth = requests.auth.HTTPBasicAuth("", ""),
    ) -> None:
        """
        VLC Class
        This class will initialize a VLC instance by connect to it using REST API w/ HTTP Basic Auth.
        This class is blocking.
        If you want to use asynchornous version please install
        `aiohttp <https://pypi.org/project/aiohttp/>`_
        :param url: VLC url
        :param auth: VLC auth
        :return: None
        """
        self.url = url
        self.auth = auth
        if not self.connectable:
            raise Exception("VLC is not running or REST API is not enabled")

    @property
    def status(self) -> dict:
        """
        Show the status & configurations inform of a dictionaries
        :return: dict
        """
        return xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text,
        )

    @property
    def playlist(self) -> dict:
        """
        Show the playlist and configurations inform of a dictionaries
        :return: dict
        """
        return xmltodict.parse(
            requests.get(self.url + "/requests/playlist.xml", auth=self.auth).text
        )

    @property
    def connectable(self) -> bool:
        """
        Check if VLC REST API is running
        :return: bool
        """
        return (
            requests.get(self.url + "/requests/status.xml", auth=self.auth).status_code
            == 200
        )

    def stop(self) -> bool:
        """
        Stop the current playing media and return back the boolean of the result
        :return: bool
        """
        return (
            requests.get(
                self.url + "/requests/status.xml?command=pl_stop", auth=self.auth
            ).status_code
            == 200
        )

    def clear_playlist(self) -> bool:
        """
        Clear the playlist and return back the boolean of the result
        :return: bool
        """
        return (
            requests.get(
                self.url + "/requests/status.xml?command=pl_empty", auth=self.auth
            ).status_code
            == 200
        )

    def play(self, uri: str) -> bool:
        """
        Play a media by uri and return back the boolean of the result if success or not
        :param uri: media uri
        :return: bool
        """
        return (
            requests.get(
                self.url + "/requests/status.xml?command=in_play&input=" + uri,
                auth=self.auth,
            ).status_code
            == 200
        )

    def append_queue(self, uri: str) -> bool:
        """
        Append a media to the queue and return back the boolean of the result if success or not
        :param uri: media uri
        :return: bool
        """
        return (
            requests.get(
                self.url + "/requests/status.xml?command=in_enqueue&input=" + uri,
                auth=self.auth,
            ).status_code
            == 200
        )

    def set_volume(self, volume: int) -> bool:
        """
        Set the volume of VLC and return back the boolean of the result if success or not
        :param volume: volume value (0-512 = 0-200%)
        :return: bool
        """
        return (
            requests.get(
                self.url + "/requests/status.xml?command=volume&val=" + str(volume),
                auth=self.auth,
            ).status_code
            == 200
        )

    def set_random(self, random: bool) -> bool:
        """
        Set the shuffle state of VLC and return back the boolean of the result if success or not
        :param random: random state
        :return: bool
        """

        return (
            requests.get(
                self.url
                + "/requests/status.xml?command=pl_random&state="
                + str(random),
                auth=self.auth,
            ).status_code
            == 200
        )

    @property
    def is_random(self) -> bool:
        """
        A property to get the random state of VLC
        :return: bool
        """
        content = xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text
        )
        print(content["root"]["random"] in ("true", "1"))
        return True if content["root"]["random"] in ("true", "1") else False

    def set_repeat_media(self, repeat: bool) -> bool:
        """
        Set the repeat state of VLC and return back the boolean of the result if success or not
        :param repeat: repeat state
        :return: bool
        """
        return (
            requests.get(
                self.url
                + "/requests/status.xml?command=pl_repeat&state="
                + str(repeat),
                auth=self.auth,
            ).status_code
            == 200
        )

    @property
    def is_repeat_media(self) -> bool:
        """
        A property to get the repeat state of VLC
        :return: bool
        """
        content = xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text
        )
        return True if content["root"]["repeat"] in ("true", "1") else False

    def set_loop_queue(self, loop: bool) -> bool:
        """
        Set the loop state of VLC and return back the boolean of the result if success or not
        :param loop: loop state
        :return: bool
        """
        return (
            requests.get(
                self.url + "/requests/status.xml?command=pl_loop&state=" + str(loop),
                auth=self.auth,
            ).status_code
            == 200
        )

    @property
    def is_loop_queue(self) -> bool:
        """
        A property to get the loop state of VLC
        :return: bool
        """
        content = xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text
        )
        return True if content["root"]["loop"] in ("true", "1") else False

    def fullscreen(self) -> bool:
        """
        Set the fullscreen state of VLC and return back the boolean of the result if success or not
        :return: bool
        """
        return (
            requests.get(
                self.url + "/requests/status.xml?command=fullscreen", auth=self.auth
            ).status_code
            == 200
        )

    @property
    def is_fullscreen(self):
        content = xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text
        )
        print(content["root"]["fullscreen"] in ("true", "1"))
        return True if content["root"]["fullscreen"] in ("true", "1") else False

    def set_subtitle_file(self, uri: str):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=pl_enqueue&input=" + uri,
                auth=self.auth,
            ).status_code
            == 200
        )

    def set_audio_file(self, uri: str):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=pl_enqueue&input=" + uri,
                auth=self.auth,
            ).status_code
            == 200
        )

    def browse(self, uri: str):
        return xmltodict.parse(
            requests.get(self.url + "/requests/browse.xml?uri=" + uri).text
        )

    def previous(self):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=pl_previous", auth=self.auth
            ).status_code
            == 200
        )

    def delete(self, uri: str):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=pl_delete&id=" + uri,
                auth=self.auth,
            ).status_code
            == 200
        )

    def next(self):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=pl_next", auth=self.auth
            ).status_code
            == 200
        )

    def clear_history(self):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=pl_history&val=clear",
                auth=self.auth,
            ).status_code
            == 200
        )

    def pause(self):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=pl_pause", auth=self.auth
            ).status_code
            == 200
        )

    @property
    def is_paused(self):
        content = xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text
        )
        return True if content["root"]["state"] in ("paused", "stopped") else False

    def seek(self, time: int):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=seek&val=" + str(time),
                auth=self.auth,
            ).status_code
            == 200
        )

    @property
    def time(self):
        content = xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text
        )
        return content["root"]["time"]

    @property
    def duration(self):
        content = xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text
        )
        return content["root"]["duration"]

    @property
    def position(self):
        content = xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text
        )
        return content["root"]["position"]

    @property
    def state(self):
        content = xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text
        )
        return content["root"]["state"]

    @property
    def volume(self):
        content = xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text
        )
        return content["root"]["volume"]


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if not aiohttp_exists:
    warnings.warn(
        "aiohttp is not installed, so you can't use the async version of this library",
        RuntimeWarning,
    )
    Async_VLC = None
else:
    pass
