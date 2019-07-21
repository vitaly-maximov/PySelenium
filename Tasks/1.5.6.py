import math

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")

inputs = browser.find_elements_by_tag_name("input")
for input in inputs:
    input.send_keys("abc")

button = browser.find_element_by_tag_name("button")
button.click()
