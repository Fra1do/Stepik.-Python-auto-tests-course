import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    print(current_dir)
    file_path = os.path.join(current_dir, 'empty.txt')
    print(file_path)
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.XPATH, "//input[@name = 'firstname']").send_keys("firstName")
    browser.find_element(By.XPATH, "//input[@name = 'lastname']").send_keys("lastName")
    browser.find_element(By.XPATH, "//input[@name = 'email']").send_keys("test@test.ru")
    browser.find_element(By.XPATH, "//input[@name='file']").send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

