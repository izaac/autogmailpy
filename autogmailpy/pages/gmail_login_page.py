from autogmailpy.pages.base_page import HomePage
from autogmailpy.helpers import config
from autogmailpy.pages.gmail_inbox_page import GmailInbox


class GmailLogin(HomePage):

    selectors = {
        'email_field': 'Email',
        'next_button': 'next',
        'email_text': 'email-display',
        'pass_field': 'Passwd',
        'signin_button': 'signIn',
        'stay_signin_checkbox': 'PersistentCookie'
    }

    def __init__(self, driver):
        super(GmailLogin, self).__init__(driver)
        self.email = None
        self.passwd = None
        self.driver.base_url = 'https://gmail.com'

    def click_next_button(self):
        next_button = self.find_by(self.By.ID, self.selectors['next_button'])
        self.click_element(next_button)
        return self

    def click_signin_button(self):
        signin_button = self.find_by(self.By.ID, self.selectors['signin_button'])
        self.click_element(signin_button)
        return GmailInbox(self.driver)

    def fill_in_email(self):
        self.fill_in(self.By.ID, self.selectors['email_field'], config['email'])
        return self

    def fill_in_password(self):
        self.fill_in(self.By.ID, self.selectors['pass_field'], config['passwd_key'])
        return self

