"""
In this example will see how to:
- visit one page
- get all links contained therein
- visit on by one to test if any of them is broken
or with some http error

NOTE: you maybe want to change the webdriver, " Browser() ",
and add your prefered driver, Browser('webdriver.chrome') for example,
but by default is always set as webdriver.firefox

NOTE: choose one url that contains broken links to see the
response

NOTE: this is a basic code, you can improve it and do what  you want,
believe, you could do almost everything :)

More information, see the docs: http://splinter.cobrateam.info/docs/
"""
from splinter.browser import Browser
from splinter.request_handler.status_code import HttpResponseError

browser = Browser()
# Visit URL
url = "http://splinter.cobrateam.info/"
browser.visit(url)
# Get all links in this page
urls = [a['href'] for a in browser.find_by_tag('a')]
# Visit each one link and verify if is ok
for url in urls:
	try:
		browser.visit(url)
		if browser.status_code.is_success():
			print '(', browser.status_code.code,') visit to', url, 'was a success!'
	except HttpResponseError, e:
		print '(', e.status_code,') visit to', url, 'was fail! Error:', e.reason

browser.quit()