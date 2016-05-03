import unittest
import uuid

from autogmailpy.helpers import *
from autogmailpy.pages.gmail_inbox_page import GmailInbox
from autogmailpy.tests.baseqa import BaseTest


class TestGmailInbox(BaseTest):

    def setUp(self):

        pass

    @screenshot_on_error
    def test_compose_email(self):

        pass

    @screenshot_on_error
    def test_validate_sent_item(self):

        pass

    @screenshot_on_error
    def test_validate_spam_delete(self):

        pass

    @screenshot_on_error
    def test_validate_compose_spelling(self):

        pass


    @screenshot_on_error
    def test_validate_delete_from_filter(self):

        pass

    def tearDown(self):

        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
