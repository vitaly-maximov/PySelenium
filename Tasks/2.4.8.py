from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price_header = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))

book_button = browser.find_element_by_css_selector("#book")
book_button.click()

span = browser.find_element_by_css_selector("#input_value")
x = float(span.text)

value = math.log(abs(12 * math.sin(x)), math.e)

textbox = browser.find_element_by_css_selector("#answer")
textbox.send_keys(str(value))

button = browser.find_element_by_css_selector("#solve")
button.click()
