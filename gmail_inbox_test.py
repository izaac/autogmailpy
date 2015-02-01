__author__ = 'Jorge'

import sys
import unittest
import uuid
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
        self.gbox = None

    def _setup_driver(self):
        self.gbox = GmailInbox(self.driver)
        self.gbox.wait = self.wait

    @screenshot_on_error
    def test_compose_email(self):
        self._setup_driver()
        self.gbox.go_inbox()
        self.gbox.body = 'This is the Email Body'
        total_emails_before = self.gbox.get_inbox_total()
        self.gbox.compose()
        total_emails_after = self.gbox.get_inbox_total()
        self.assertLess(total_emails_before, total_emails_after)

    @screenshot_on_error
    def test_validate_sent_item(self):
        self._setup_driver()
        self.gbox.go_inbox()
        self.gbox.body = '{0}'.format(uuid.uuid4())
        self.gbox.compose()
        self.gbox.check_in_sent()
        self.gbox.wait_for(self.gbox.first_email_entry_content())
        first_sent_entry = self.gbox.first_email_entry_content().text
        self.assertEqual(first_sent_entry[3:], self.gbox.body)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
