import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]").click()
    # Приняли confirm
    alert = browser.switch_to.alert
    alert.accept()
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(calc(browser.find_element(By.XPATH, "//span[@id='input_value']").text))


    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

