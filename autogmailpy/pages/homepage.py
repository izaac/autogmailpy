__author__ = 'Jorge'
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage:

    def __init__(self, driver):
        self._driver = driver
        self._wait = None

    def quit(self):
        self.driver.quit()

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, obj):
        self._driver = obj

    @property
    def wait(self):
        return self._wait

    @wait.setter
    def wait(self, obj):
        self._wait = obj

    def wait_for(self, element):
        self.wait.until(EC.visibility_of(element))

    def find_by(self, *pars):
        return self.driver.find_element(*pars)

    @staticmethod
    def click_element(elem):
        elem.click()

    @staticmethod
    def get_text_from_element(elem):
        return elem.text

    @staticmethod
    def wait_secs(seconds):
        time.sleep(seconds)