from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import autogmailpy
import uuid

__author__ = 'Jorge'

driver = webdriver.Firefox()
gbox = autogmailpy.GmailInbox(driver)
wait = WebDriverWait(driver, timeout=60)
driver.implicitly_wait(5)
gbox.wait = wait
gbox.go_inbox()
gbox.body = '{0}'.format(uuid.uuid4())
gbox.compose()
gbox.check_in_sent()
gbox.quit()
