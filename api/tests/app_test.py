import os
from os import path
import pytest
from ..main import create_app


emu_android_device = os.environ.get("EMU_ANDROID", '')
android_device = os.environ.get("ANDROID_DEVICE", '')


@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    return app.test_client()


def test_install_apk_android_emulator_device(app):
    res = app.post("/install/{0}".format(emu_android_device))
    screenshoot_file = '/code/screenshoots/{0}{1}'.format(emu_android_device, '.png')

    if path.exists(screenshoot_file):
        assert True
        os.remove(screenshoot_file)
    else:
        assert False
    assert res.status_code == 200
    assert b"ok" in res.data


def test_install_apk_android_device(app):
    res = app.post("/install/{0}".format(android_device))
    screenshoot_file = '/code/screenshoots/{0}{1}'.format(android_device, '.png')

    if path.exists(screenshoot_file):
        assert True
        os.remove(screenshoot_file)
    else:
        assert False
    assert res.status_code == 200
    assert b"ok" in res.data


def test_install_apk_wrong_device_uid(app):
    res = app.post("/install/WRONGUID")
    assert res.status_code == 200
    assert b"nok" in res.data
