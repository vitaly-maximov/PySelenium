from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

chest = browser.find_element_by_css_selector("#treasure")
x = float(chest.get_attribute("valuex"))

value = math.log(abs(12 * math.sin(x)), math.e)

textbox = browser.find_element_by_css_selector("#answer")
textbox.send_keys(str(value))

checkbox = browser.find_element_by_css_selector("#robotCheckbox")
checkbox.click()

radiobutton = browser.find_element_by_css_selector("#robotsRule")
radiobutton.click()

button = browser.find_element_by_tag_name("button")
button.click()
