import math

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")

secret = str(math.ceil(math.pow(math.pi, math.e)*10000))
element = browser.find_element_by_link_text(secret)
element.click()

firstNameInput = browser.find_element_by_css_selector('[name="first_name"]')
firstNameInput.send_keys("Vitaly")

lastNameInput = browser.find_element_by_css_selector('[name="last_name"]')
lastNameInput.send_keys("Maximov")

cityInput = browser.find_element_by_css_selector(".city")
cityInput.send_keys("SPb")

countryInput = browser.find_element_by_css_selector("#country")
countryInput.send_keys("Russia")

submitButton = browser.find_element_by_css_selector(".btn")
submitButton.click()