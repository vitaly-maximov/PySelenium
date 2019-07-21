from selenium import webdriver
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

first_name_input = browser.find_element_by_css_selector("[name='firstname']")
first_name_input.send_keys("Vitaly")

last_name_input = browser.find_element_by_css_selector("[name='lastname']")
last_name_input.send_keys("Maximov")

email_input = browser.find_element_by_css_selector("[name='email']")
email_input.send_keys("vm@mail.ru")

file_button = browser.find_element_by_css_selector("#file")

file = os.path.join(os.path.dirname(__file__), "2.2.8.txt")
file_button.send_keys(file)

button = browser.find_element_by_tag_name("button")
button.click()
