import unittest
import uuid

from autogmailpy.helpers import *
from autogmailpy.pages.gmail_inbox import GmailInbox
from autogmailpy.tests.baseqa import BaseTest


class TestGmailInbox(BaseTest):

    def setUp(self):

        super(TestGmailInbox, self).setUp()
        self.gbox = GmailInbox(self.driver)
        self.gbox.wait = self.wait

    @screenshot_on_error
    def test_compose_email(self):

        self.gbox.go_inbox()
        self.gbox.body = 'This is the Email Body'
        total_emails_before = self.gbox.get_inbox_total()
        self.gbox.compose()
        total_emails_after = self.gbox.get_inbox_total()
        self.assertLess(total_emails_before, total_emails_after)

    @screenshot_on_error
    def test_validate_sent_item(self):

        self.gbox.go_inbox()
        self.gbox.body = '{0}'.format(uuid.uuid4())
        self.gbox.compose()
        self.gbox.check_in_sent()
        self.gbox.wait_for(self.gbox._first_email_entry_content())
        first_sent_entry = self.gbox._first_email_entry_content().text
        self.assertEqual(first_sent_entry[3:], self.gbox.body)

    @screenshot_on_error
    def test_validate_spam_delete(self):

        self.gbox.go_inbox()
        self.assertTrue(self.gbox.delete_from_spam())

    def tearDown(self):

        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
