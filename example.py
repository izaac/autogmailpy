from selenium import webdriver
import autogmailpy
import uuid

__author__ = 'Jorge'

driver = webdriver.Firefox()
glogin = autogmailpy.GmailLogin(driver)
glogin.visit_login()
inbox = glogin.fill_in_email().click_next_button().fill_in_password().click_signin_button()
body = '{0}'.format(uuid.uuid4())
inbox.click_compose().fill_email(body=body).send_email().validate_new_email()
inbox.quit()
