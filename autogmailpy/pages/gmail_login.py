from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from autogmailpy.pages.homepage import HomePage
from autogmailpy.helpers import config


class GmailLogin(HomePage):

    def __init__(self, driver):
        super(GmailLogin, self).__init__(driver)
        self.email = None
        self.passwd = None
        self.driver.base_url = 'https://gmail.com'

    def _locate_loginform_elements(self):
        self.email = self._locate_email_field()
        self.passwd = self._locate_passwd_field()

    def _fill_loginform_elements(self, email_keys=config['email'], passwd_keys='invalid_pass'):
        self.email.clear()
        self.email.send_keys(email_keys)

        self.passwd.clear()
        self.passwd.send_keys(passwd_keys)

    def _click_loginform_login(self):
        sign_in = self._locate_signin_button()
        sign_in.click()

    def login_valid(self):

        self.driver.implicitly_wait(20)
        self.wait_for(self._locate_signin_button())
        self._locate_loginform_elements()

        self._fill_loginform_elements(passwd_keys=config['passwd_key'])
        self._click_loginform_login()

        try:
            self.wait_for(self._locate_inbox_link())
        except NoSuchElementException as nsee:
            print('Couldnt locate element after valid login {0}'.format(nsee))
            inbox_present = False
        else:
            inbox_present = True

        return inbox_present

    def login_invalid(self):

        self._locate_loginform_elements()

        self._fill_loginform_elements()
        self._click_loginform_login()

        try:
            self.wait_for(self._locate_error_message())
        except NoSuchElementException as nsee:
            print('No error message was visible {0}'.format(nsee))
            error_present = False
        else:
            error_present = True

        return error_present

    def _locate_signin_button(self):
        return self.find_by(By.ID, 'signIn')

    def _locate_email_field(self):
        return self.find_by(By.ID, 'Email')

    def _locate_passwd_field(self):
        return self.find_by(By.ID, 'Passwd')

    def _locate_inbox_link(self):
        return self.find_by(By.XPATH, "//a[contains(@title,'Inbox')]")

    def _locate_error_message(self):
        return self.find_by(By.ID, 'errormsg_0_Passwd')
