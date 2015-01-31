import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from homepage import HomePage
from helpers import config

class GmailLogin(HomePage):

    def __init__(self, driver):
        super(GmailLogin, self).__init__(driver)
        self.email = None
        self.passwd = None
        self.driver.base_url = 'https://gmail.com'

    def _locate_loginform_elements(self):
        try:
            self.email = self.driver.find_element(By.ID, 'Email')
        except NoSuchElementException as nsee:
            print('No Email Element Located {0}'.format(nsee))
        try:
            self.passwd = self.driver.find_element(By.ID, 'Passwd')
        except NoSuchElementException as nsee:
            print('No Password Element Located {0}'.format(nsee))

    def _fill_loginform_elements(self, email_keys=config['email'], passwd_keys='invalid_pass'):
        self.email.clear()
        self.email.send_keys(email_keys)

        self.passwd.clear()
        self.passwd.send_keys(passwd_keys)

    def _click_loginform_login(self):
        sign_in = self.driver.find_element(By.ID, 'signIn')
        sign_in.click()

    def login_valid(self):

        element = self.wait.until(EC.visibility_of(self.driver.find_element(By.ID, 'signIn')))

        if element:
            self._locate_loginform_elements()

        self._fill_loginform_elements(passwd_keys=config['passwd_key'])
        self._click_loginform_login()

        try:
            self.wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, "//div[@id=':36']")))
        except NoSuchElementException as nsee:
            print('Couldnt locate element after valid login {0}'.format(nsee))
            inbox_present = False
        else:
            inbox_present = True

        return inbox_present

    def login_invalid(self):

        element = self.wait.until(EC.visibility_of(self.driver.find_element(By.ID, 'signIn')))
        if element:
            self._locate_loginform_elements()

        self._fill_loginform_elements()
        self._click_loginform_login()

        try:
            self.wait.until(EC.visibility_of(self.driver.find_element(By.ID, 'errormsg_0_Passwd')))
        except NoSuchElementException as nsee:
            print('No error message was visible {0}'.format(nsee))
            error_present = False
        else:
            error_present = True

        return error_present


if __name__ == '__main__':
    pass

    # driver.implicitly_wait(5)
    # base_url = ''
    # gmailbox = GmailInbox(driver)
    # gmailbox.wait = wait
    # gmailbox.driver.base_url = 'https://gmail.com'
    # gmailbox.driver.get(gmailbox.driver.base_url)
    # gmailbox.go_inbox()

