import unittest
import uuid

from autogmailpy.helpers import *
from autogmailpy.pages.gmail_inbox_page import GmailInbox
from autogmailpy.tests.baseqa import BaseTest


class TestGmailInbox(BaseTest):

    def setUp(self):

        super(TestGmailInbox, self).setUp()
        self.gbox = GmailInbox(self.driver)
        self.gbox.wait = self.wait
        self.gbox.wait_seconds(20)
        self.gbox.go_inbox()

    @screenshot_on_error
    def test_compose_email(self):

        self.gbox.body = 'This is the Email Body'
        total_emails_before = self.gbox.get_current_total()
        self.gbox.compose()
        self.gbox.click_inbox_link()
        self.gbox.force_wait(5)
        total_emails_after = self.gbox.get_current_total()
        self.assertLess(total_emails_before, total_emails_after)

    @screenshot_on_error
    def test_validate_sent_item(self):

        self.gbox.body = '{0}'.format(uuid.uuid4())
        self.gbox.compose()
        self.gbox.check_in_sent()
        self.gbox.wait_for(self.gbox._first_email_entry_content())
        first_sent_entry = self.gbox.get_first_element_text()
        self.assertEqual(first_sent_entry[3:], self.gbox.body)

    @screenshot_on_error
    def test_validate_spam_delete(self):

        self.assertTrue(self.gbox.delete_from_spam())

    @screenshot_on_error
    def test_validate_compose_spelling(self):

        self.gbox.body = "bad sfdfdfdf"
        self.assertTrue(self.gbox.check_compose_spelling())

    @screenshot_on_error
    def test_validate_delete_from_filter(self):

        uuid_gen = uuid.uuid4()
        self.gbox.body = '{0}'.format(uuid_gen)
        self.gbox.subject = '[test] {0}'.format(uuid_gen)
        self.gbox.compose()
        self.assertTrue(self.gbox.delete_from_filter())

    def tearDown(self):

        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
