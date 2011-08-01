"""
interact with forms, test if element exists in a page

This example:
- Try to login on Google Accounts
- do this over and over again
- until the captcha appear

Just for try if after many attempts to login, Google show the captcha
for the safe of the system.
"""
from splinter.browser import Browser

browser = Browser('webdriver.chrome')
browser.visit('https://www.google.com/accounts/ServiceLogin')
# just a counter
i = 0
# while not appear the captcha input, try login with wrong account
while True:
	browser.fill('Email', 'buzzcreativeweb')
	browser.fill('Passwd', 'p455w942')
	browser.find_by_css('#signIn').first.click()
	i += 1
	if browser.is_element_present_by_id('logincaptcha'):
		break

print 'After', i, 'attempts the captcha appeared!'