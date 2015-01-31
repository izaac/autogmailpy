__author__ = 'Jorge'

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from homepage import HomePage
from gmail_login import GmailLogin
from helpers import config


class GmailInbox(HomePage):

    def __init__(self, driver):
        super(GmailInbox, self).__init__(driver)
        self.element = None
        self._body = ""

    def go_inbox(self):

        login = GmailLogin(self.driver)
        login.wait = self.wait
        driver = self.driver

        driver.get('https://gmail.com')

        if login.login_valid():
            try:
                self.element = driver.find_element(By.XPATH, "//div[contains(text(),'COMPOSE')]")
            except NoSuchElementException as nsee:
                print('No Compose button {0}'.format(nsee))

    def compose(self):

        self.wait.until(EC.visibility_of(self.element))
        self.element.click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//td//img[2]")
        to_mail = self.driver.find_element(By.CLASS_NAME, "vO")
        to_mail.clear()
        to_mail.send_keys(config['email'])
        subject = self.driver.find_element(By.CLASS_NAME, "aoT")
        subject.clear()
        subject.send_keys("Hi!")

        actions = ActionChains(self.driver)
        actions.key_down(Keys.TAB)
        actions.send_keys(self.body)
        actions.perform()

        self.driver.find_element(By.XPATH, "//div[text()='Send']").click()

        self.wait.until(EC.visibility_of(self.driver.find_element(By.CLASS_NAME, 'vh')))
        self.quit()

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, obj):
        self._body = obj

if __name__ == '__main__':

    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    driver = webdriver.Firefox()
    gbox = GmailInbox(driver)
    wait = WebDriverWait(driver, timeout=60)
    driver.implicitly_wait(5)
    gbox.wait = wait
    gbox.go_inbox()
    gbox.compose()