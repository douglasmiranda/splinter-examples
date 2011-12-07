"""
taking screenshots
"""
from splinter.browser import Browser

browser = Browser('chrome')

url = "http://splinter.cobrateam.info/"
browser.visit(url)

browser.driver.save_screenshot('screenshot.png')

browser.quit()