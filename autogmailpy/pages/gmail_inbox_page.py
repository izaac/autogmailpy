from autogmailpy.pages.base_page import HomePage
from autogmailpy.helpers import config
__author__ = 'Jorge'


class GmailInbox(HomePage):

    selectors = dict(
        compose_button="//div[contains(text(),'COMPOSE')]",
        inbox="//a[contains(@title,'Inbox')]"
    )

    def __init__(self, driver):
        super(GmailInbox, self).__init__(driver)
        self._body = ""
        self._subject = "Hi!"
        self.driver = driver
        self.wait_for(self.find_by(self.By.XPATH, self.selectors['compose_button']))

    def _compose_frame_visible(self):
        self.find_by(self.By.XPATH, "//div[contains(text(),'COMPOSE')]")

    def _locate_send_button(self):
        return self.find_by(self.By.XPATH, "//div[text()='Send']")

    def _locate_sent_message(self):
        return self.find_by(self.By.CLASS_NAME, 'vh')

    def _locate_compose_subject(self):
        return self.find_by(self.By.CLASS_NAME, "aoT")

    def _locate_compose_to(self):
        return self.find_by(self.By.CLASS_NAME, "vO")

    def _locate_compose_body(self):
        return self.find_by(self.By.XPATH, "//div[contains(@aria-label, 'Message Body')]")
        # return self.find_by(self.By.CSS_SELECTOR, "css=div[aria-label~='Message Body']")

    def _locate_inbox_link(self):
        return self.find_by(self.By.XPATH, "//a[contains(@title,'Inbox')]")
        # return self.find_by(self.By.CSS_SELECTOR, "css=a[title~='Inbox']")

    def _locate_sent_link(self):
        return self.find_by(self.By.XPATH, "//a[contains(@title,'Sent Mail')]")
        # return self.find_by(self.By.CSS_SELECTOR, "css=a[title~='Sent Mail']")

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

    def _locate_email_counter_total_filter(self):
        return self.find_by(self.By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/"
                                      "div[1]/div[2]/div[1]/span/div[1]/span/b[3]")

    def _locate_compose_button(self):
        return self.find_by(self.By.XPATH, "//div[contains(text(),'COMPOSE')]")

    def _first_email_entry(self):
        return self.find_by(self.By.XPATH, "//span[contains(@class, 'yP')]")
        # return self.find_by(self.By.CSS_SELECTOR, "span[class~='yP']")

    def _first_email_entry_content(self):
        #return self.find_by(self.By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/div/div/"
        #                              "div/div/div/div/div/div/table/tbody/tr/td/div/div/div/span[2]")
        return self.find_by(self.By.CSS_SELECTOR, "html>body>div>div>div>div>div>div>div>div>div>div>div>"
                            "div>div>div>div>div>div>table>tbody>tr>td>div>div>div>span:nth-of-type(2)")

    def _first_email_entry_title(self):
        return self.find_by(self.By.XPATH, "//div[contains(@class, 'y6')]/descendant::span/b")

    def _first_element_checkbox(self):
        return self.find_by(self.By.XPATH, "//td[2]/div/div")

    def _first_element_checkbox_filter(self):
        return self.find_by(self.By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[1]/"
                                      "div[1]/div/div/div[5]/div[1]/div/table/tbody/tr[1]/td[2]/div")

    def _locate_delforever_button(self):
        return self.find_by(self.By.XPATH, "//div[contains(text(),'Delete forever')]")

    def _locate_delete_button(self):
        # return self.find_by(self.By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/"
        #                               "div[1]/div[1]/div/div/div[2]/div[3]")

        return self.find_by(self.By.CSS_SELECTOR, "html>body>div:nth-of-type(7)>div:nth-of-type(3)>div>div:nth-of-type(2)>"
                                             "div:nth-of-type(1)>div:nth-of-type(2)>div>div>div>div:nth-of-type(1)>"
                                             "div:nth-of-type(2)>div:nth-of-type(1)>div:nth-of-type(1)>div>div>"
                                             "div:nth-of-type(2)>div:nth-of-type(3)")

    def _locate_delforever_confirmation(self):
        return self.find_by(self.By.XPATH, "//div[contains(text(), 'The conversation has been deleted.')")

    def _locate_delete_confirmation(self):
        # return self.find_by(self.By.XPATH, "/html/body/div[7]/div[3]/div/div[1]/div[5]/div[1]/div[2]/div[3]/div/div/"
        #                               "div[2]/span[1]")
        return self.find_by(self.By.CSS_SELECTOR, "html>body>div:nth-of-type(7)>div:nth-of-type(3)>div>div:nth-of-type(1)>"
                                             "div:nth-of-type(5)>div:nth-of-type(1)>div:nth-of-type(2)>"
                                             "div:nth-of-type(3)>div>div>div:nth-of-type(2)>span:nth-of-type(1)")

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

    def click_inbox_link(self):
        self.click_element(self._locate_inbox_link())

    def click_sent_link(self):
        self.click_element(self._locate_sent_link())

    def click_spam_link(self):
        self.click_element(self._locate_spam_link())

    def click_compose_button(self):
        self.click_element(self._locate_compose_button())

    def click_send_button(self):
        self.click_element(self._locate_send_button())

    def click_delete_button(self):
        self.click_element(self._locate_delete_button())

    def click_delete_forever_button(self):
        self.click_element(self._locate_delforever_button())

    def click_check_spelling_button(self):
        self.click_element(self._locate_check_spelling_button())

    def click_more_options(self):
        self.click_element(self._locate_more_options())

    def get_first_element_text(self):
        return self.get_text_from_element(self._first_email_entry_content())