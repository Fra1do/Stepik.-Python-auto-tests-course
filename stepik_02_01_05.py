from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(calc(browser.find_element(By.XPATH, "//span[@id='input_value']").text))
    browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    browser.find_element(By.XPATH, "//input[@id='robotsRule']").click()


    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()


