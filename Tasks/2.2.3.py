from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

a = int(browser.find_element_by_css_selector("#num1").text)
b = int(browser.find_element_by_css_selector("#num2").text)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(a+b))

button = browser.find_element_by_tag_name("button")
button.click()
