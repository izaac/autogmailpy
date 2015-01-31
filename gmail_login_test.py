import sys
import unittest
from locale import LC_ALL, setlocale
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from gmail_login import GmailLogin
from helpers import *

setlocale(LC_ALL, '')
bin_path = os.environ.get('BIN_PATH')


class TestGmailLogin(unittest.TestCase):

    def setUp(self):

        if not bin_path:
            self.driver = webdriver.Firefox()
        else:
            ffbin = FirefoxBinary(firefox_path=bin_path, log_file=sys.stdout)
            self.driver = webdriver.Firefox(firefox_binary=ffbin)

        self.wait = WebDriverWait(self.driver, timeout=60)
        self.driver.implicitly_wait(5)
        self.glogin = None

    def _setup_driver(self):
        self.glogin = GmailLogin(self.driver)
        self.glogin.wait = self.wait

    @screenshot_on_error
    def test_invalid_login(self):
        self._setup_driver()
        self.glogin.driver.get(self.glogin.driver.base_url)
        self.assertTrue(self.glogin.login_invalid())

    @screenshot_on_error
    def test_valid_login(self):
        self._setup_driver()
        self.glogin.driver.get(self.glogin.driver.base_url)
        self.assertTrue(self.glogin.login_valid())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
