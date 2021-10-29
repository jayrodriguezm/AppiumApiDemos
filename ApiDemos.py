from Base import Base

class ApiDemos(Base):

    _app_element_xpath = '//android.widget.TextView[@content-desc="App"]'
    _activity_element_xpath = '//android.widget.TextView[@content-desc="Activity"]'
    _hello_world_element_xpath = '//android.widget.TextView[@content-desc="Hello World"]'
    _app_continue_button_id = "com.android.permissioncontroller:id/continue_button"
    _hello_world_text_id = 'io.appium.android.apis:id/text'
    _ok_button_id = "android:id/button1"

    def get_hello_world_text(self):
        return self.get_element_attribute_by_id(self._hello_world_text_id, "text")

    def tap_app(self):
        return self.tap_element_by_xpath(self._app_element_xpath)

    def tap_activity(self):
        return self.tap_element_by_xpath(self._activity_element_xpath)

    def tap_hello_world(self):
        return self.tap_element_by_xpath(self._hello_world_element_xpath)

    def tap_continue_button(self):
        return self.tap_element_by_id(self._app_continue_button_id)

    def tap_ok_button(self):
        return self.tap_element_by_id(self._ok_button_id)

    def wait_for_app_option_to_appear(self):
        return self.wait_for_element_to_appear_by_xpath(self._app_element_xpath)

    def wait_for_activity_option_to_appear(self):
        return self.wait_for_element_to_appear_by_xpath(self._activity_element_xpath)

    def wait_for_hello_world_option_to_appear(self):
        return self.wait_for_element_to_appear_by_xpath(self._hello_world_element_xpath)

    def wait_for_ok_button_to_appear(self):
        return self.wait_for_element_to_appear_by_id(self._ok_button_id, timeout=20)

    def wait_for_hello_world_text_to_appear(self):
        return self.wait_for_element_to_appear_by_xpath(self._hello_world_text_xpath)

