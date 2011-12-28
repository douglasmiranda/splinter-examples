"""
This example shows how to test web interface with splinter API with mouse interactions.

In this page (http://douglasmiranda.com/labs/projetos/)
when the mouse is over an element, it shows a description of itself.

So let's automate the test to verify if this is ok.

PS: This is a mouse interaction, so when you execute this script, you should stop moving the mouse :)
"""
from splinter.browser import Browser

browser = Browser('chrome')
browser.visit('http://douglasmiranda.com/labs/projetos/')

li = browser.find_by_css('#ultimos-projetos li').first

li.mouse_over()
print 'When the mouse is over the description is visible? ', li.find_by_css('.descricao').visible

li.mouse_out()
print '...and when the mouse is out the description is visible? ', li.find_by_css('.descricao').visible

browser.quit()