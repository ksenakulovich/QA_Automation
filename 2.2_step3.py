from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(n1, n2):
  return str(sum([int(n1), int(n2)]))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_element = browser.find_element(By.ID, 'num1').text
    second_element = browser.find_element(By.ID, 'num2').text
    result = calc(first_element, second_element)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(result)

    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()