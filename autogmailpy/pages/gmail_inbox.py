__author__ = 'Jorge'
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from autogmailpy.pages.homepage import HomePage
from autogmailpy.pages.gmail_login import GmailLogin
from autogmailpy.helpers import config


class GmailInbox(HomePage):

    def __init__(self, driver):
        super(GmailInbox, self).__init__(driver)
        self.compose_button = None
        self._body = ""
        self._subject = "Hi!"
        self.driver = driver

    def go_inbox(self):

        login = GmailLogin(self.driver)
        login.wait = self.wait
        login.driver = self.driver

        self.driver.get('https://gmail.com')

        if login.login_valid():
            self.driver.implicitly_wait(5)
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
        subject.send_keys(self.subject)

        body = self._locate_compose_body()
        body.send_keys(self.body)

        self.wait_for(self._locate_send_button())
        send = self._locate_send_button()
        send.click()
        self.wait_for(self._locate_sent_message())

    def get_current_total(self, inbox=False):

        if inbox:
            inbox_link = self._locate_inbox_link()
            inbox_link.click()

        self.driver.implicitly_wait(5)

        if inbox:
            mail_counter = self._locate_email_counter_total(inbox=True)
        else:
            mail_counter = self._locate_email_counter_total()
        mail_counter = mail_counter.text

        try:
            mail_counter = int(mail_counter)
        except ValueError:
            print("Not a number, can not convert to int")

        return mail_counter

    def check_in_sent(self):
        sent_link = self._locate_sent_link()
        sent_link.click()
        self.driver.implicitly_wait(3)

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

            total_spam_items = self.get_current_total()
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

            if total_spam_items > self.get_current_total():
                return True
            else:
                return False
        else:
            # Empty
            return True

    def delete_from_filter(self):

        more_less_button = self._locate_more_less()
        more_less_button.click()
        self.wait_for(self._locate_test_link())
        test_link = self._locate_test_link()
        test_link.click()

        not_empty = True
        try:
            self._locate_no_email_filter()
        except NoSuchElementException as nsee:
            print('There are emails in the filter {0}'.format(nsee))
        else:
            not_empty = False

        if not_empty:

            self.driver.implicitly_wait(5)
            total_filter_items = self.get_current_total()
            first_element = self._first_element_checkbox_filter()
            first_element.click()
            self.driver.implicitly_wait(3)
            self.wait_for(self._locate_delete_button())
            delete = self._locate_delete_button()
            delete.click()
            self.driver.implicitly_wait(3)
            self.wait_for(self._locate_delete_confirmation())

            try:
                self._locate_no_email_filter()
            except NoSuchElementException as nsee:
                print('No emails in this filter'.format(nsee))
            else:
                return True if total_filter_items > 0 else False

            if total_filter_items > self.get_current_total():
                return True
            else:
                return False
        else:
            # Empty
            return True

    def check_compose_spelling(self):

        self.driver.implicitly_wait(20)
        self.wait_for(self._locate_compose_button())
        compose = self._locate_compose_button()
        compose.click()
        message = self._locate_compose_body()
        message.send_keys(self.body)
        mopts = self._locate_more_options()
        mopts.click()
        check_spelling = self._locate_check_spelling_button()
        check_spelling.click()
        self.driver.implicitly_wait(5)

        bad_words = False
        try:
            self._locate_bad_spelled()
        except NoSuchElementException as nsee:
            print('No Bad Words detected {0}'.format(nsee))
        else:
            bad_words = True

        return bad_words

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, obj):
        self._body = obj

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, obj):
        self._subject = obj

    def _compose_frame_visible(self):
        self.find_by(By.XPATH, "//div[contains(text(),'COMPOSE')]")

    def _locate_send_button(self):
        return self.find_by(By.XPATH, "//div[text()='Send']")

    def _locate_sent_message(self):
        return self.find_by(By.CLASS_NAME, 'vh')

    def _locate_compose_subject(self):
        return self.find_by(By.CLASS_NAME, "aoT")

    def _locate_compose_to(self):
        return self.find_by(By.CLASS_NAME, "vO")

    def _locate_compose_body(self):
        return self.find_by(By.XPATH, "//div[contains(@aria-label, 'Message Body')]")

    def _locate_inbox_link(self):
        return self.find_by(By.XPATH, "//a[contains(@title,'Inbox')]")

    def _locate_sent_link(self):
        return self.find_by(By.XPATH, "//a[contains(@title,'Sent Mail')]")

    def _locate_test_link(self):
        return self.find_by(By.XPATH, "//a[contains(@title,'testx')]")

    def _locate_spam_link(self):
        return self.find_by(By.XPATH, "//a[contains(@title,'Spam')]")

    def _locate_no_spam(self):
        return self.find_by(By.XPATH, "//td[contains(text(), 'Hooray, no spam here!')]")

    def _locate_no_email_filter(self):
        return self.find_by(By.XPATH, "//td[contains(text(), 'There are no conversations with this label')]")

    def _locate_email_counter_total(self, inbox=False):
        if inbox:
            return self.find_by(By.XPATH, "//span[contains(@class, 'Dj')]/b[3]")
        else:
            return self.find_by(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/"
                                          "div[1]/div[2]/div[1]/span/div[1]/span/b[3]")

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

    def _first_element_checkbox_filter(self):
        return self.find_by(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[1]/"
                                      "div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[1]/td[2]/div")

    def _locate_delforever_button(self):
        return self.find_by(By.XPATH, "//div[contains(text(),'Delete forever')]")

    def _locate_delete_button(self):
        return self.find_by(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/"
                                      "div[1]/div[1]/div/div/div[2]/div[3]")

    def _locate_delforever_confirmation(self):
        return self.find_by(By.XPATH, "//div[contains(text(), 'The conversation has been deleted.')")

    def _locate_delete_confirmation(self):
        return self.find_by(By.XPATH, "/html/body/div[7]/div[3]/div/div[1]/div[5]/div[1]/div[2]/div[3]/div/div/"
                                      "div[2]/span[1]")

    def _locate_more_less(self):
        return self.find_by(By.CLASS_NAME, "CJ")

    def _locate_more_options(self):
        return self.find_by(By.XPATH, "//div[contains(@aria-label, 'More options')]")

    def _locate_check_spelling_button(self):
        return self.find_by(By.XPATH, "//div[contains(text(),'Check spelling')]")

    def _locate_bad_spelled(self):
        self.find_by(By.XPATH, "//span[@data-g-spell-status]")