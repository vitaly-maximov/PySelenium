from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration1.html")

firstNameInput = browser.find_element_by_css_selector('.first')
firstNameInput.send_keys("Vitaly")

lastNameInput = browser.find_element_by_css_selector('.second')
lastNameInput.send_keys("Maximov")

emailInput = browser.find_element_by_css_selector(".third")
emailInput.send_keys("vm@mail.ru")

button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(1)

text = browser.find_element_by_xpath('//h1')
assert "Поздравляем!" in text.text
