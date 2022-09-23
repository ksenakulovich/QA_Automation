from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'Cover_Letter_updated.docx')  # добавляем к этому пути имя файла

    fname = browser.find_element(By.NAME, 'firstname')
    fname.send_keys('Ivan')
    lname = browser.find_element(By.NAME, 'lastname')
    lname.send_keys('Ivanov')
    mail = browser.find_element(By.NAME, 'email')
    mail.send_keys('ivan@mail.ru')
    upl_button = browser.find_element(By.ID, "file")
    upl_button.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()