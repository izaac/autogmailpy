__author__ = 'Jorge'
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from autogmailpy.homepage import HomePage
from autogmailpy.gmail_login import GmailLogin
from autogmailpy.helpers import config


class GmailInbox(HomePage):

    def __init__(self, driver):
        super(GmailInbox, self).__init__(driver)
        self.compose_button = None
        self._body = ""
        self.driver = driver

    def go_inbox(self):

        login = GmailLogin(self.driver)
        login.wait = self.wait
        login.driver = self.driver

        self.driver.get('https://gmail.com')

        if login.login_valid():
            try:
                self.compose_button = self.locate_compose_button()
            except NoSuchElementException as nsee:
                print('No Compose button {0}'.format(nsee))

    def compose(self):

        self.wait_for(self.locate_compose_button())
        self.compose_button.click()
        self.driver.implicitly_wait(10)
        self.compose_frame_visible()
        to_mail = self.locate_compose_to()
        to_mail.clear()
        to_mail.send_keys(config['email'])
        subject = self.locate_compose_subject()
        subject.clear()
        subject.send_keys("Hi!")

        actions = ActionChains(self.driver)
        actions.key_down(Keys.TAB)
        actions.send_keys(self.body)
        actions.perform()

        self.wait_for(self.locate_send_button())
        send = self.locate_send_button()
        send.click()
        self.wait_for(self.locate_sent_message())

    def get_inbox_total(self):

        inbox_link = self.locate_inbox_link()
        inbox_link.click()
        time.sleep(5)
        mail_counter = self.locate_email_counter()
        mail_counter = mail_counter.text.split()[-1]
        try:
            mail_counter = int(mail_counter)
        except ValueError:
            print("Not a number, can not convert to int")

        return mail_counter

    def check_in_sent(self):
        sent_link = self.locate_sent_link()
        sent_link.click()
        time.sleep(3)

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, obj):
        self._body = obj

    def compose_frame_visible(self):
        self.driver.find_by(By.XPATH, "//td//img[2]")

    def locate_send_button(self):
        return self.find_by(By.XPATH, "//div[text()='Send']")

    def locate_sent_message(self):
        return self.find_by(By.CLASS_NAME, 'vh')

    def locate_compose_subject(self):
        return self.find_by(By.CLASS_NAME, "aoT")

    def locate_compose_to(self):
        return self.find_by(By.CLASS_NAME, "vO")

    def locate_inbox_link(self):
        return self.find_by(By.XPATH, "//a[contains(@title,'Inbox')]")

    def locate_sent_link(self):
        return self.find_by(By.XPATH, "//a[contains(@title,'Sent Mail')]")

    def locate_email_counter(self):
        return self.find_by(By.CLASS_NAME, "Dj")

    def locate_compose_button(self):
        return self.find_by(By.XPATH, "//div[contains(text(),'COMPOSE')]")

    def first_email_entry(self):
        return self.find_by(By.XPATH, "//span[contains(@class, 'yP')]")

    def first_email_entry_content(self):
        return self.find_by(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/div/div/"
                                      "div/div/div/div/div/div/table/tbody/tr/td/div/div/div/span[2]")
        # return self.driver.find_element(By.XPATH, "//span[@class='y2']")

    def first_email_entry_title(self):
        return self.find_by(By.XPATH, "//div[contains(@class, 'y6')]/descendant::span/b")

    def all_mail_to_list(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class,'yW')]")

    def all_mail_body_list(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class,'y6')]")


if __name__ == '__main__':

    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait

    driver = webdriver.Firefox()
    gbox = GmailInbox(driver)
    wait = WebDriverWait(driver, timeout=60)
    driver.implicitly_wait(5)
    gbox.wait = wait
    gbox.go_inbox()
    # gbox.body = '{0}'.format(uuid.uuid4())
    # gbox.compose()
    # gbox.driver.switch_to.default_content()
    gbox.check_in_sent()
    gbox.wait_for(gbox.first_email_entry_content())
    print(gbox.first_email_entry_content().text)
    gbox.quit()