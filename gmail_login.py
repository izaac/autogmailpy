import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from homepage import HomePage
from helpers import config

class GmailLogin(HomePage):

    def __init__(self, driver):
        super(GmailLogin, self).__init__(driver)
        self.email = None
        self.passwd = None
        self.driver.base_url = 'https://gmail.com'

    def _locate_loginform_elements(self):
        self.email = self.locate_email_field()
        self.passwd = self.locate_passwd_field()

    def _fill_loginform_elements(self, email_keys=config['email'], passwd_keys='invalid_pass'):
        self.email.clear()
        self.email.send_keys(email_keys)

        self.passwd.clear()
        self.passwd.send_keys(passwd_keys)

    def _click_loginform_login(self):
        sign_in = self.locate_signin_button()
        sign_in.click()

    def login_valid(self):

        self.wait_for(self.locate_signin_button())
        self._locate_loginform_elements()

        self._fill_loginform_elements(passwd_keys=config['passwd_key'])
        self._click_loginform_login()

        try:
            self.wait_for(self.locate_inbox_link())
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
            self.wait_for(self.locate_error_message())
        except NoSuchElementException as nsee:
            print('No error message was visible {0}'.format(nsee))
            error_present = False
        else:
            error_present = True

        return error_present

    def locate_signin_button(self):
        return self.driver.find_element(By.ID, 'signIn')

    def locate_email_field(self):
        return self.driver.find_element(By.ID, 'Email')

    def locate_passwd_field(self):
        return self.driver.find_element(By.ID, 'Passwd')

    def locate_inbox_link(self):
        return self.driver.find_element(By.XPATH, "//a[contains(@title,'Inbox')]")

    def locate_error_message(self):
        return self.driver.find_element(By.ID, 'errormsg_0_Passwd')

if __name__ == '__main__':
    pass

    # driver.implicitly_wait(5)
    # base_url = ''
    # gmailbox = GmailInbox(driver)
    # gmailbox.wait = wait
    # gmailbox.driver.base_url = 'https://gmail.com'
    # gmailbox.driver.get(gmailbox.driver.base_url)
    # gmailbox.go_inbox()

