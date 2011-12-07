"""
interact via javascript, send, get and manipule DOM
splinter allows you to execute javascript code to send, get and manipule
the DOM.
In this example we will:
- send code to be executed on browser
- manipulate the DOM with javascript code with splinter
- get the data from javascript
NOTE: You will see the example code more advanced and organized in:
javascript_advanced_and_organized_code.py
"""
from splinter.browser import Browser

browser = Browser('chrome')
# Visit URL
url = "http://splinter.cobrateam.info/"
browser.visit(url)
# 1 - Send code to webpage to be executed
# you can execute a simple javascript code
browser.execute_script('alert("Hello World")')
# assign variable
javascript_code = 'message = "After this alert, the body tag will disappear";'
javascript_code += 'alert(message);'
browser.execute_script(javascript_code)
# you just can execute any javascript code, like,
# for example, manupulate dom
# javascript snippet to hidden the body
browser.execute_script('document.getElementsByTagName("body")[0].style.display = "none"')
# 2 - Getting data returned from javascript code execution
# getting value of the 'display' attribute from the body tag
value_of_display = browser.evaluate_script('document.getElementsByTagName("body")[0].style.display')
browser.execute_script('alert("As you could see, the body disappeared, so the display is set as: %s");' % value_of_display)
browser.execute_script('alert("..but now");')
# back to the normal, that is, display:block
browser.execute_script('document.getElementsByTagName("body")[0].style.display = "block"')

value_of_display = browser.evaluate_script('document.getElementsByTagName("body")[0].style.display')
browser.execute_script('alert("back to the normal! And display is set as: %s");' % value_of_display)
# NOTE: you can use the jQuery, or any snippet of any
# javascript framework, you simply include it before execute