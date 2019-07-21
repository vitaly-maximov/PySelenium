from selenium import webdriver
import time

browser = webdriver.Chrome()

pages = [
    "http://suninjuly.github.io/registration1.html", # test 1 should work
    "http://suninjuly.github.io/registration2.html"] # test 2 should fail

for page in pages:
    print("test: ", page)

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
    assert "Поздравляем!" in text.text