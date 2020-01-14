import os
import time
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

from appium import webdriver

# appium config
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['app'] = '{0}/app-debug.apk'.format(
    os.environ.get("APK_DIR", ''))
desired_caps['appPackage'] = 'com.phonegap.helloworld'
desired_caps['appActivity'] = 'com.phonegap.helloworld.MainActivity'
desired_caps['noReset'] = "false"


class App(Resource):
    def post(self, device_name):
        '''Install APK endpoint

        This endpoint installs an existing apk on a connected Android device or emulator, once the apk is installed launches the app and takes a screenshot.

        Arguments:
            device_name {string} -- [connected device name]
        Return:
            http 200
            {response: ok} if everything's ok (launch app and take a screenshot).
            {response: nok} if device not exist, couldn't take a screenshot, or raise an Exception
        '''
        driver = None
        response = 'nok'
        try:
            desired_caps['udid'] = device_name
            driver = webdriver.Remote(
                "http://localhost:4723/wd/hub", desired_caps)
            driver.launch_app()
            time.sleep(5)
            screenshot_created = driver.get_screenshot_as_file(
                '/code/screenshoots/{0}{1}'.format(device_name, '.png'))
            driver.quit()
            if screenshot_created:
                response = 'ok'
        except Exception:
            pass
        return {'response': response}


def create_app(config=None):
    app = Flask(__name__)
    api = Api(app)

    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})
    CORS(app)

    api.add_resource(App, '/install/<string:device_name>')

    return app


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)
