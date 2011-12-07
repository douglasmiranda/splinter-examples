"""
interact with forms, send data, get data in html
In this example we will:
- visit the google's web page
- do a search with the terms: the answer to life the universe and everything
- get the specific data using the css selectors
NOTE: Using the webdriver.firefox there a strange behavior,
for some reason is used the suggestion of google in the search,
that is, i want to search:
"the answer to life the universe and everything"
and because of the suggestion is auto choosen:
"the answer to life the universe and everything else"
I mean, for me is happening this...
"""
from splinter.browser import Browser

browser = Browser('chrome')
browser.visit('http://google.com')
# Note: 'q' is the value of the atribute 'name', not the 'id'
# <input type='text' name='q'...
browser.fill('q', 'the answer to life the universe and everything')
# find the submit buttom by the class atribute and click it
browser.find_by_css('.lsb').first.click()
# Note: find_by_css find elements in html using css selectors
# like we use in a css file
print browser.find_by_css('#topstuff .std h2').first.value

browser.quit()