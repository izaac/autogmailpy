from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

__author__ = 'Jorge'


class HomePage:

    def __init__(self, driver):
        self.NoSuchElementException = NoSuchElementException
        self.By = By
        self.Keys = Keys
        self.ActionChains = ActionChains
        self._driver = driver
        self._driver.implicitly_wait(10)
        self._wait = WebDriverWait(driver, 10)

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

    def have_content(self, content):
        result = self.driver.find_elements_by_xpath("//*[contains(text(),'"+content+"')]")
        if result:
            return True
        return False

    @staticmethod
    def click_element(elem):
        elem.click()

    @staticmethod
    def get_text_from_element(elem):
        return elem.text

    @staticmethod
    def wait_secs(driver, seconds):
        driver.implicitly_wait(seconds)

    @staticmethod
    def force_wait(seconds):
        time.sleep(seconds)

    def fill_in(self, by, selector, content):
        element = self.find_by(by, selector)
        element.send_keys(content)
