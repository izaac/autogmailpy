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
                self.compose_button = self._locate_compose_button()
            except NoSuchElementException as nsee:
                print('No Compose button {0}'.format(nsee))

    def compose(self):

        self.wait_for(self._locate_compose_button())
        self.compose_button.click()
        self.driver.implicitly_wait(10)
        self._compose_frame_visible()
        to_mail = self._locate_compose_to()
        to_mail.clear()
        to_mail.send_keys(config['email'])
        subject = self._locate_compose_subject()
        subject.clear()
        subject.send_keys("Hi!")

        actions = ActionChains(self.driver)
        actions.key_down(Keys.TAB)
        actions.send_keys(self.body)
        actions.perform()

        self.wait_for(self._locate_send_button())
        send = self._locate_send_button()
        send.click()
        self.wait_for(self._locate_sent_message())

    def get_inbox_total(self):

        inbox_link = self._locate_inbox_link()
        inbox_link.click()
        time.sleep(5)
        mail_counter = self._locate_email_counter()
        mail_counter = mail_counter.text.split()[-1]
        try:
            mail_counter = int(mail_counter)
        except ValueError:
            print("Not a number, can not convert to int")

        return mail_counter

    def check_in_sent(self):
        sent_link = self._locate_sent_link()
        sent_link.click()
        time.sleep(3)

    def delete_from_spam(self):

        more_less_button = self._locate_more_less()
        more_less_button.click()
        self.wait_for(self._locate_spam_link())
        spam_link = self._locate_spam_link()
        spam_link.click()

        not_empty = True
        try:
            self._locate_no_spam()
        except NoSuchElementException as nsee:
            print('There is Spam {0}'.format(nsee))
        else:
            not_empty = False

        if not_empty:

            total_spam_items = self.get_inbox_total()
            first_element = self._first_element_checkbox()
            first_element.click()
            self.wait_for(self._locate_delforever_button())
            del_forever = self._locate_delforever_button()
            del_forever.click()
            self.wait_for(self._locate_delforever_confirmation())

            try:
                self._locate_no_spam()
            except NoSuchElementException as nsee:
                print('There is Spam {0}'.format(nsee))
            else:
                return True if total_spam_items > 0 else False

            if total_spam_items > self.get_inbox_total():
                return True
            else:
                return False
        else:
            # Empty
            return True

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, obj):
        self._body = obj

    def _compose_frame_visible(self):
        self.driver.find_by(By.XPATH, "//td//img[2]")

    def _locate_send_button(self):
        return self.find_by(By.XPATH, "//div[text()='Send']")

    def _locate_sent_message(self):
        return self.find_by(By.CLASS_NAME, 'vh')

    def _locate_compose_subject(self):
        return self.find_by(By.CLASS_NAME, "aoT")

    def _locate_compose_to(self):
        return self.find_by(By.CLASS_NAME, "vO")

    def _locate_inbox_link(self):
        return self.find_by(By.XPATH, "//a[contains(@title,'Inbox')]")

    def _locate_sent_link(self):
        return self.find_by(By.XPATH, "//a[contains(@title,'Sent Mail')]")

    def _locate_spam_link(self):
        return self.find_by(By.XPATH, "//a[contains(@title,'Spam')]")

    def _locate_no_spam(self):
        return self.find_by(By.XPATH, "//td[contains(text(), 'Hooray, no spam here!')]")

    def _locate_email_counter(self):
        return self.find_by(By.CLASS_NAME, "Dj")

    def _locate_compose_button(self):
        return self.find_by(By.XPATH, "//div[contains(text(),'COMPOSE')]")

    def _first_email_entry(self):
        return self.find_by(By.XPATH, "//span[contains(@class, 'yP')]")

    def _first_email_entry_content(self):
        return self.find_by(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/div/div/"
                                      "div/div/div/div/div/div/table/tbody/tr/td/div/div/div/span[2]")
        # return self.driver.find_element(By.XPATH, "//span[@class='y2']")

    def _first_email_entry_title(self):
        return self.find_by(By.XPATH, "//div[contains(@class, 'y6')]/descendant::span/b")

    def _all_mail_to_list(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class,'yW')]")

    def _all_mail_body_list(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class,'y6')]")

    def _first_element_checkbox(self):
        return self.find_by(By.XPATH, "//td[2]/div/div")

    def _locate_delforever_button(self):
        return self.find_by(By.XPATH, "//div[contains(text(),'Delete forever')]")

    def _locate_delforever_confirmation(self):
        return self.find_by(By.XPATH, "//div[contains(text(), 'The conversation has been deleted.')")

    def _locate_more_less(self):
        return self.find_by(By.CLASS_NAME, "CJ")