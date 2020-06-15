import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 15).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    book = browser.find_element(By.ID, "book")
    book.click()
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(calc(browser.find_element(By.XPATH, "//span[@id='input_value']").text))
    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()