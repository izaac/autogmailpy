from autogmailpy.pages.base_page import HomePage
from autogmailpy.helpers import config
__author__ = 'Jorge'


class GmailInbox(HomePage):

    selectors = dict(
        compose_button="//div[contains(text(),'COMPOSE')]",
        inbox_css="a[title|='Inbox']",
        new_message="//div[contains(text(),'New Message')]",
        to_text_field="textarea[aria-label='To'][name='to']",
        subject_text_field="input[placeholder='Subject'][aria-label='Subject'][name='subjectbox']",
        body_text_field="div[aria-label|='Message Body']",
        send_button="div[aria-label~='Send']",
    )

    def __init__(self, driver):
        super(GmailInbox, self).__init__(driver)
        self._body = ""
        self._subject = "Hi!"
        self.driver = driver
        self.wait_for(self.find_by(self.By.CSS_SELECTOR, self.selectors['inbox_css']))

    def click_compose(self):
        self.click_element(self.find_by(self.By.XPATH, self.selectors['compose_button']))
        self.wait_for(self.find_by(self.By.XPATH, self.selectors['new_message']))
        return self

    def fill_email(self, to=config['email'], subject='test', body='test'):
        self.fill_in(self.By.CSS_SELECTOR, self.selectors['to_text_field'], to)
        self.find_by(self.By.CSS_SELECTOR, self.selectors['to_text_field']).send_keys(self.Keys.TAB)
        self.fill_in(self.By.CSS_SELECTOR, self.selectors['subject_text_field'], subject)
        self.find_by(self.By.CSS_SELECTOR, self.selectors['subject_text_field']).send_keys(self.Keys.TAB)
        self.fill_in(self.By.CSS_SELECTOR, self.selectors['body_text_field'], body)
        self.force_wait(3)
        return self

    def send_email(self):
        self.click_element(self.find_by(self.By.CSS_SELECTOR, self.selectors['send_button']))
        self.force_wait(3)
        self

    def _locate_sent_message(self):
        return self.find_by(self.By.CLASS_NAME, 'vh')

    def _locate_compose_subject(self):
        return self.find_by(self.By.CLASS_NAME, "aoT")

    def _locate_compose_to(self):
        return self.find_by(self.By.CLASS_NAME, "vO")

    def _locate_test_link(self):
        return self.find_by(self.By.XPATH, "//a[contains(@title,'testx')]")

    def _locate_spam_link(self):
        return self.find_by(self.By.XPATH, "//a[contains(@title,'Spam')]")
        # return self.find_by(self.By.CSS_SELECTOR, "css=a[title~='Spam']")

    def _locate_no_spam(self):
        return self.find_by(self.By.XPATH, "//td[contains(text(), 'Hooray, no spam here!')]")

    def _locate_no_email_filter(self):
        return self.find_by(self.By.XPATH, "//td[contains(text(), 'There are no conversations with this label')]")

    def _locate_email_counter_total(self):
        return self.find_by(self.By.CSS_SELECTOR, ".Dj>b:nth-of-type(3)")

    def _locate_compose_button(self):
        return self.find_by(self.By.XPATH, "//div[contains(text(),'COMPOSE')]")

    def _first_email_entry(self):
        return self.find_by(self.By.XPATH, "//span[contains(@class, 'yP')]")
        # return self.find_by(self.By.CSS_SELECTOR, "span[class~='yP']")

    def _first_email_entry_title(self):
        return self.find_by(self.By.XPATH, "//div[contains(@class, 'y6')]/descendant::span/b")

    def _first_element_checkbox(self):
        return self.find_by(self.By.XPATH, "//td[2]/div/div")

    def _locate_delforever_button(self):
        return self.find_by(self.By.XPATH, "//div[contains(text(),'Delete forever')]")

    def _locate_delforever_confirmation(self):
        return self.find_by(self.By.XPATH, "//div[contains(text(), 'The conversation has been deleted.')")

    def _locate_more_less(self):
        return self.find_by(self.By.CLASS_NAME, "CJ")

    def _locate_more_options(self):
        return self.find_by(self.By.XPATH, "//div[contains(@aria-label, 'More options')]")

    def _locate_check_spelling_button(self):
        return self.find_by(self.By.XPATH, "//div[contains(text(),'Check spelling')]")

    def _locate_bad_spelled(self):
        self.find_by(self.By.XPATH, "//span[@data-g-spell-status]")

    def wait_seconds(self, seconds):
        self.wait_secs(self.driver, seconds)

    def click_spam_link(self):
        self.click_element(self._locate_spam_link())

    def click_compose_button(self):
        self.click_element(self._locate_compose_button())

    def click_delete_forever_button(self):
        self.click_element(self._locate_delforever_button())

    def click_check_spelling_button(self):
        self.click_element(self._locate_check_spelling_button())

    def click_more_options(self):
        self.click_element(self._locate_more_options())