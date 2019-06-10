from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Actions(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, element_id, classname):
        if element_id and classname:
            raise RuntimeError("One one of element id or classname can be set!")

        if element_id:
            element = self.wait_for_element(element_id)
        if classname:
            element = self.wait_for_class(classname)

        return element

    def wait_for_element(self, element_id):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, element_id)))
        self.driver.implicitly_wait(0.5)
        return element

    def wait_for_class(self, classname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, classname)))
        self.driver.implicitly_wait(0.5)
        return element

    def input_text(self, text, element_id=None, classname=None):
        element = self.get_element(element_id, classname)
        element.clear()
        element.send_keys(text)

    def press_enter(self, element_id=None, classname=None):
        element = self.get_element(element_id, classname)
        element.send_keys(Keys.RETURN)

    def click_element(self, element_id=None, classname=None):
        element = self.get_element(element_id, classname)
        element.click()

    def check_for_elements(self, element_ids):
        for element_id in element_ids:
            element = self.driver.find_element_by_id(element_id)
            assert element is not None

    def page_contains_text(self, text):
        self.driver.implicitly_wait(1)
        assert (text in self.driver.page_source)
