__author__ = 'Jorge'

import os
import sys
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

bin_path = os.environ.get('BIN_PATH')


class BaseTest(TestCase):

    driver = None
    wait = None

    def setUp(self):

        if not bin_path:
            self.driver = webdriver.Firefox()
        else:
            ffbin = FirefoxBinary(firefox_path=bin_path, log_file=sys.stdout)
            self.driver = webdriver.Firefox(firefox_binary=ffbin)

        self.wait = WebDriverWait(self.driver, timeout=60)
