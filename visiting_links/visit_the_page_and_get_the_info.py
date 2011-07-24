"""
Simply visit a URL to get some information,
just for improve in future, adding various ways to get
data from page with splinter API
"""
from splinter.browser import Browser

browser = Browser()
# Visit URL
url = "http://splinter.cobrateam.info/"
browser.visit(url)

# by property
print 'URL:', browser.url
print 'Page Title:', browser.title
# method
print 'H1:', browser.find_by_tag('h1').first.value
print 'Total Links:', len(browser.find_by_tag('a'))

browser.quit()