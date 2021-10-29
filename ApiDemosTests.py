import unittest
import logging
import datetime
import Logger as logger
from ApiDemos import ApiDemos as ad
from time import sleep


class ApiDemosTests(unittest.TestCase):
    bs = None
    ad = None
    dt = datetime.datetime.now().time()
    logfile = logfile = "ApiDemos-" + '-' + str(dt) + ".log"
    log = logger.custom_logger(logging.DEBUG, file_name=logfile)
    app = "/Users/jrodrigu/Documents/github/Coding/Android-App-Demo/ApiDemos.apk"
    platform_version = "10.0"
    device_name = "Pixel 4"

    @classmethod
    def setUp(cls):
        cls.ad = ad(cls.log)
        cls.ad.initialize(app=cls.app, platform_version=cls.platform_version, device_name=cls.device_name)
        cls.ad.tap_continue_button()
        cls.ad.wait_for_ok_button_to_appear()
        cls.ad.tap_ok_button()

    def test_api(self):
        self.ad.wait_for_app_option_to_appear()
        self.ad.tap_app()
        self.ad.wait_for_activity_option_to_appear()
        self.ad.tap_activity()
        self.ad.wait_for_hello_world_option_to_appear()
        self.ad.tap_hello_world()
        print(self.ad.get_hello_world_text())

    @classmethod
    def tearDown(cls):
        # cls.bs.quit_driver()
        pass

    if __name__ == '__main__':
        unittest.main()
