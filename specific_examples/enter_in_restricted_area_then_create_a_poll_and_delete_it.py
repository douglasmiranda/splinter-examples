"""
interact with forms, send data, get data
and click on links that contains javascript actions

This is a specific example to test a Poll App powered with django
This example consists in:
- Acess the admin area, with username and password
- Access the link to add a now Poll
- Add a new Poll with your choices
- Save the Poll
- Find the link of the Poll inserted before
- Choice the "delete option" and confirm delete in the next page
- Get the info from the operation

This example will works perfectly if you completed the second part of the
django tutorial: https://docs.djangoproject.com/en/dev/intro/tutorial02/

For more information, just check: https://docs.djangoproject.com/en/dev/intro/tutorial01/
NOTE: This was tested when the version of the tutorial was for Django 1.3
"""
from splinter.browser import Browser

browser = Browser()
# You may change this url to the current url from your Poll App
browser.visit('http://127.0.0.1:8000/admin/')
# You may change the username and password too
browser.fill('username', 'douglas')
browser.fill('password', '123456')
# do login
browser.find_by_css('.submit-row input').first.click()
# add a new poll
browser.find_link_by_href('polls/poll/add/').first.click()

browser.fill('question', 'Does this test is completed successfully?')
# if you follow the instructions from the tutorial, this is will show
# the datetime options from the poll
browser.find_by_css('.collapse-toggle').first.click()
datetime_fields = browser.find_by_css('.datetimeshortcuts')
datetime_fields[0].find_by_tag('a').first.click()
datetime_fields[1].find_by_tag('a').first.click()
# fill the choices
browser.fill('choice_set-0-choice', 'Yup!')
browser.fill('choice_set-0-votes', '0')
browser.fill('choice_set-1-choice', 'Nope!')
browser.fill('choice_set-1-votes', '0')
browser.fill('choice_set-2-choice', 'Maybe...')
browser.fill('choice_set-2-votes', '0')
# submit the poll
browser.find_by_name('_save').first.click()
# find the poll by the title
browser.find_link_by_text('Does this test is completed successfully?').first.click()
# choose the "delete option"
browser.find_link_by_href('delete/').first.click()
# confirm delete
browser.find_by_css('input[type=submit]').first.click()
# get the result info
print browser.find_by_css('.messagelist').first.text

browser.quit()