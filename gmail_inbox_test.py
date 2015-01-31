__author__ = 'Jorge'

import sys
import unittest
from locale import LC_ALL, setlocale
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from helpers import *
from gmail_inbox import GmailInbox

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
        self.glogin = GmailInbox(self.driver)
        self.glogin.wait = self.wait

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
