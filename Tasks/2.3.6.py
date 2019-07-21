from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

first_button = browser.find_element_by_tag_name("button")
first_button.click()

browser.switch_to.window(browser.window_handles[1])

span = browser.find_element_by_css_selector("#input_value")
x = float(span.text)

value = math.log(abs(12 * math.sin(x)), math.e)

textbox = browser.find_element_by_css_selector("#answer")
textbox.send_keys(str(value))

button = browser.find_element_by_tag_name("button")
button.click()
