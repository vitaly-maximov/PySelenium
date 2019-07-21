from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")

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