import unittest
from selenium import webdriver
import time

def register(page):
    browser = webdriver.Chrome()
    browser.get(page)

    first_name_input = browser.find_element_by_css_selector('input[placeholder="Введите имя"]')
    first_name_input.send_keys("Ivan")

    last_name_input = browser.find_element_by_css_selector('input[placeholder="Введите фамилию"]')
    last_name_input.send_keys("Ivanov")

    email_input = browser.find_element_by_css_selector('input[placeholder="Введите Email"]')
    email_input.send_keys("ii@mail.ru")

    button = browser.find_element_by_tag_name("button")
    button.click()

    time.sleep(1)

    text = browser.find_element_by_xpath('//h1')
    return text.text


class TestRegistration(unittest.TestCase):
    def test_register1(self):
        text = register("http://suninjuly.github.io/registration1.html")
        assert "Поздравляем!" in text
        
    def test_register2(self):
        text = register("http://suninjuly.github.io/registration2.html")
        assert "Поздравляем!" in text
        
if __name__ == "__main__":
    unittest.main()