from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/execute_script.html")

span = browser.find_element_by_css_selector("#input_value")
x = float(span.text)

value = math.log(abs(12 * math.sin(x)), math.e)

textbox = browser.find_element_by_css_selector("#answer")
textbox.send_keys(str(value))

checkbox = browser.find_element_by_css_selector("#robotCheckbox")
browser.execute_script("arguments[0].scrollIntoView(true)", checkbox)
checkbox.click()

radiobutton = browser.find_element_by_css_selector("#robotsRule")
browser.execute_script("arguments[0].scrollIntoView(true)", radiobutton)
radiobutton.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("arguments[0].scrollIntoView(true)", button)
button.click()
