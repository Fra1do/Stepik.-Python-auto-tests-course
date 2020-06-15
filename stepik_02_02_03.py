from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



try:
    oldLink = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = (int)(browser.find_element(By.XPATH, "//span[@id='num1']").text)
    num2 = (int)(browser.find_element(By.XPATH, "//span[@id='num2']").text)
    browser.find_element(By.XPATH, "//select[@id='dropdown']").click()
    select=Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text((str)(num1+num2))

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()