import requests
import xmltodict

class VLC:
    def __init__(
        self,
        url: str = "http://localhost:8080",
        auth: requests.auth.HTTPBasicAuth = requests.auth.HTTPBasicAuth("", ""),
    ):
        """ """
        self.url = url
        self.auth = auth
        if not self.connectable:
            raise Exception("VLC is not running or REST API is not enabled")

    @property
    def status(self):
        return xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text,
        )

    @property
    def playlist(self):
        return xmltodict.parse(
            requests.get(self.url + "/requests/playlist.xml", auth=self.auth).text
        )

    @property
    def connectable(self):
        return (
            requests.get(self.url + "/requests/status.xml", auth=self.auth).status_code
            == 200
        )

    def stop(self):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=pl_stop", auth=self.auth
            ).status_code
            == 200
        )

    def clear_playlist(self):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=pl_empty", auth=self.auth
            ).status_code
            == 200
        )

    def play(self, uri: str):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=in_play&input=" + uri,
                auth=self.auth,
            ).status_code
            == 200
        )

    def append_queue(self, uri: str):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=in_enqueue&input=" + uri,
                auth=self.auth,
            ).status_code
            == 200
        )

    def set_volume(self, volume: int):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=volume&val=" + str(volume),
                auth=self.auth,
            ).status_code
            == 200
        )

    @property
    def volume(self):
        content = xmltodict.parse(requests.get(self.url + "/requests/status.xml").text)
        return content["root"]["volume"]

    def set_random(self, random: bool):
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
    def is_random(self):
        content = xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text
        )
        return True if content["root"]["random"] == "1" else False

    def set_repeat_media(self, repeat: bool):
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
    def is_repeat_media(self):
        content = xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text
        )
        return True if content["root"]["repeat"] == "1" else False

    def set_loop_queue(self, loop: bool):
        return (
            requests.get(
                self.url + "/requests/status.xml?command=pl_loop&state=" + str(loop),
                auth=self.auth,
            ).status_code
            == 200
        )

    @property
    def is_loop_queue(self):
        content = xmltodict.parse(
            requests.get(self.url + "/requests/status.xml", auth=self.auth).text
        )
        return True if content["root"]["loop"] == "1" else False

    def fullscreen(self):
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
        return True if content["root"]["fullscreen"] == "1" else False

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
        print(content)
        return True if content["root"]["state"] in ("paused", "stopped") else False
