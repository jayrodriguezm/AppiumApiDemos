from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Base:

    def __init__(self, logger, ip="127.0.0.1", port="4723", path="/wd/hub"):
        self._logger = logger
        self._ip = ip
        self._port = port
        self._path = path
        self._command_executor = 'http://' + ip + ':' + port + path
        self._driver = None

    def initialize(self, app, platform_version, device_name):
        caps = {
            'app': app,
            'platformName': "Android",
            'deviceName': device_name,
            'platformVersion': platform_version,
            'appPackage': "io.appium.android.apis",
            'appActivity' : "io.appium.android.apis.ApiDemos",
            'autoGrantPermissions': 'true',
            "clearDeviceLogsOnStart": 'true'
        }
        try:
            self._driver = webdriver.Remote(
                command_executor=self._command_executor,
                desired_capabilities=caps)
            self._touch_action = TouchAction(self._driver)
            self._logger.info("Appium initialized successfully")
            return True
        except Exception as error:
            self._logger.error("Appium initialize failed with the following error: "
                               + str(error))
            return False

    def get_element_attribute(self, element, attribute):
        try:
            element_attribute = element.get_attribute(attribute)
        except Exception as e:
            self._logger.error(f'An error has been reported by Appium when retrieving {attribute} '
                               f'from {element}: {e}')
            return None
        else:
            self._logger.info(f'Attribute {attribute} retrieved successfully from {element}')
            return element_attribute

    def get_element_attribute_by_id(self, element_id, attribute):
        try:
            element = self._driver.find_element_by_id(element_id)
            element_attribute = element.get_attribute(attribute)
        except Exception as e:
            self._logger.error(f'An error has been reported by Appium when retrieving {attribute} '
                               f'from {element_id}: {e}')
            return None
        else:
            self._logger.info(f'Attribute {attribute} retrieved successfully from {element_id}')
            return element_attribute

    def get_element_attribute_by_xpath(self, element_xpath, attribute):
        try:
            element = self._driver.find_element_by_xpath(element_xpath)
            element_attribute = element.get_attribute(attribute)
        except Exception as e:
            self._logger.error(f'An error has been reported by Appium when retrieving {attribute} '
                               f'from {element_xpath}: {e}')
            return None
        else:
            self._logger.info(f'Attribute {attribute} retrieved successfully from {element_xpath}')
            return element_attribute

    def go_back(self):
        self._driver.back()

    def return_list_of_elements_by_id(self, element_id):
        try:
            elements_list = self._driver.find_elements_by_id(element_id)
        except Exception as e:
            self._logger.error(f'An error has been reported by Appium when retrieving a list of {element_id}: {e}')
            return None
        else:
            self._logger.info(f'List of {element_id} retrieved successfully')
            return elements_list

    def tap_element(self, element):
        try:
            self._touch_action.tap(element)
            self._touch_action.perform()
        except Exception as e:
            self._logger.error(f'An error has been reported by Appium when tapping {element}: {e}')
            return False
        else:
            self._logger.info(f'Element {element} tapped successfully')
            return True

    def tap_element_by_access_id(self, element_id):
        element_to_tap = self._driver.find_elements_by_accessibility_id(element_id)
        try:
            self._touch_action.tap(element_to_tap)
            self._touch_action.perform()
        except Exception as e:
            self._logger.error(f'An error has been reported by Appium when tapping {element_id}: {e}')
            return False
        else:
            self._logger.info(f'Element {element_id} tapped successfully')
            return True

    def tap_element_by_id(self, element_id):
        element_to_tap = self._driver.find_element_by_id(element_id)
        try:
            self._touch_action.tap(element_to_tap)
            self._touch_action.perform()
        except Exception as e:
            self._logger.error(f'An error has been reported by Appium when tapping {element_id}: {e}')
            return False
        else:
            self._logger.info(f'Element {element_id} tapped successfully')
            return True

    def tap_element_by_xpath(self, xpath):
        element_to_tap = self._driver.find_element_by_xpath(xpath)
        try:
            self._touch_action.tap(element_to_tap)
            self._touch_action.perform()
        except Exception as e:
            self._logger.error(f'An error has been reported by Appium when tapping the element'
                               f'given by {xpath}: {e}')
            return False
        else:
            self._logger.info(f'Element given by {xpath} tapped successfully')
            return True

    def tap_button(self, button):
        try:
            self.tap_element_by_id(button)
        except Exception as e:
            self._logger.error(f'An error has been reported by Appium when tapping {button}: {e}')
            return False
        else:
            self._logger.info(f'Button {button} tapped successfully')
            return True

    def type_by_id(self, element_id, text):
        element_to_type_in = self._driver.find_element_by_id(element_id)
        try:
            element_to_type_in.send_keys(text)
        except Exception as e:
            self._logger.error(f'An error has been reported by appium when typint "{text}": {e}')
            return False
        else:
            self._logger.info(f'Text "{text}" entered successfully')
            return True

    def quit_driver(self):
        if self._driver:
            success = self._driver.quit()
            self._logger.info("Driver quit successfully")
        else:
            self._logger.error("Driver failed to quit")
            return False
        if success:
            return True
        else:
            return False

    def wait_for_element_to_appear_by_id(self, element_id, timeout=10):
        try:
            WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located((By.ID, element_id)))
        except TimeoutException as ex:
            self._logger.error(f'Timeout waiting for element "{element_id}" to appear: {ex}')
            return False
        else:
            self._logger.info(f'The element "{element_id}" appeared successfully')
            return True

    def wait_for_element_to_appear_by_xpath(self, element_xpath, timeout=10):
        try:
            WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
        except TimeoutException as ex:
            self._logger.error(f'Timeout waiting for element with xpath "{element_xpath}" to appear: {ex}')
            return False
        else:
            self._logger.info(f'The element "{element_xpath}" appeared successfully')
            return True
