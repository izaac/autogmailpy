import unittest
from autogmailpy.pages.gmail_login_page import GmailLogin
from autogmailpy.helpers import screenshot_on_error
from autogmailpy.tests.baseqa import BaseTest


class TestGmailLogin(BaseTest):

    def setUp(self):

        super(TestGmailLogin, self).setUp()
        self.glogin = GmailLogin(self.driver)

    @screenshot_on_error
    def test_valid_login(self):

        self.glogin.driver.get(self.glogin.driver.base_url)
        inbox = self.glogin.fill_in_email().click_next_button().fill_in_password().click_signin_button()
        inbox.click_compose().fill_email().send_email().validate_new_email()

    def tearDown(self):

        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
