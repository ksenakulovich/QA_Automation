from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value').text
    y = calc(x_element)

    text_field = browser.find_element(By.ID, 'answer')
    text_field.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    chbox = browser.find_element(By.XPATH, '//input[@type="checkbox"]')
    chbox.click()
    rb = browser.find_element(By.ID, "robotsRule")
    rb.click()
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()