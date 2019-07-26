from selenium import webdriver
import pytest
import math
import time

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.mark.parametrize("link", [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"])
def test_pages(browser, link):
    browser.get(link)

    time.sleep(2)

    answer = math.log(int(time.time()))

    textarea = browser.find_element_by_tag_name("textarea")
    textarea.send_keys(str(answer))

    button = browser.find_element_by_tag_name("button")
    button.click()

    time.sleep(2)

    hint = browser.find_element_by_css_selector(".smart-hints__hint")

    assert hint.text == "Correct!", hint.text

