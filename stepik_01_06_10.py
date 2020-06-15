from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class, 'first')]").send_keys("firstName")
    browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class, 'second')]").send_keys("lastName")
    browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class, 'third')]").send_keys("test@test.ru")
    browser.find_element(By.XPATH, "//div[@class='second_block']//input[contains(@class, 'first')]").send_keys("88005553555")
    browser.find_element(By.XPATH, "//div[@class='second_block']//input[contains(@class, 'second')]").send_keys("Moscow")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()