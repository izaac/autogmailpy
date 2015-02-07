import unittest

from autogmailpy.pages.gmail_login import GmailLogin
from autogmailpy.helpers import *
from autogmailpy.tests.baseqa import BaseTest


class TestGmailLogin(BaseTest):

    def setUp(self):

        super(TestGmailLogin, self).setUp()
        self.driver.implicitly_wait(5)
        self.glogin = GmailLogin(self.driver)
        self.glogin.wait = self.wait


    @screenshot_on_error
    def test_invalid_login(self):

        self.glogin.driver.get(self.glogin.driver.base_url)
        self.assertTrue(self.glogin.login_invalid())

    @screenshot_on_error
    def test_valid_login(self):

        self.glogin.driver.get(self.glogin.driver.base_url)
        self.assertTrue(self.glogin.login_valid())

    def tearDown(self):

        self.driver.refresh()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
