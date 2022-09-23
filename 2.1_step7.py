from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.TAG_NAME, 'img')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    text_field = browser.find_element(By.ID, 'answer')
    text_field.send_keys(y)
    chbox = browser.find_element(By.XPATH, '//input[@type="checkbox"]')
    chbox.click()
    rb = browser.find_element(By.ID, "robotsRule")
    rb.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()