from dotenv import load_dotenv

load_dotenv()
import os
import sys
import time
import pytest

sys.path.append("..")  # pytest problem?
import rest_vlc

vlc = rest_vlc.Async_VLC(auth=("", os.environ["VLC_PASSWORD"]))


@pytest.fixture
def x():
    print("Start testing")
    time.sleep(0.8)


async def test_low_volume():
    assert await vlc.set_volume(0), "Failed to set volume to 0"


async def test_up_volume():
    assert await vlc.set_volume(256), "Failed to set volume to 100"


async def test_pause():
    assert await vlc.pause(), "Failed to pause"


async def test_stop():
    assert await vlc.stop(), "Failed to stop"


async def test_clear_playlist():
    assert await vlc.clear_playlist(), "Failed to clear playlist"


async def test_play():
    assert await vlc.play(os.environ["VLC_URI"]), "Failed to play"


async def test_append():
    assert await vlc.append_queue(os.environ["VLC_URI2"]), "Failed to append"


async def test_random():
    assert await vlc.set_random(True), "Failed to set random"
    assert vlc.is_random, "Failed to set random"


async def test_repeat():
    assert await vlc.set_repeat_media(True), "Failed to set repeat"
    assert vlc.is_repeat_media, "Failed to set repeat"


async def test_loop():
    assert await vlc.set_loop_queue(True), "Failed to set loop"
    assert vlc.is_loop_queue, "Failed to set loop"


async def test_fullscreen():
    assert await vlc.fullscreen(), "Failed to set fullscreen"
    assert vlc.is_fullscreen, "Failed to set fullscreen"
    assert await vlc.fullscreen(), "Failed to set fullscreen"  # revert
    assert not vlc.is_fullscreen, "Failed to set fullscreen"  # revert


async def test_browse():
    assert await vlc.browse(os.environ["VLC_FOLDER"]), "Failed to browse"


async def test_previous():
    assert await vlc.previous(), "Failed to previous"


async def test_next():
    assert await vlc.next(), "Failed to next"


async def test_delete():
    assert await vlc.delete(os.environ["VLC_URI"]), "Failed to delete"


async def test_clear_history():
    assert await vlc.clear_history(), "Failed to clear history"


async def test_seeking():
    assert await vlc.seek(69), "Failed to seek"
