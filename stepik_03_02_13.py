import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestAbs(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_reg1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = self.driver
        browser.get(link)
        browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class, 'first')]").send_keys(
            "firstName")
        browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class, 'second')]").send_keys(
            "lastName")
        browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class, 'third')]").send_keys(
            "test@test.ru")
        browser.find_element(By.XPATH, "//div[@class='second_block']//input[contains(@class, 'first')]").send_keys(
            "88005553555")
        browser.find_element(By.XPATH, "//div[@class='second_block']//input[contains(@class, 'second')]").send_keys(
            "Moscow")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        text = browser.find_element(By.XPATH, "//h1").text
        self.assertEqual(text, "Congratulations! You have successfully registered!")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = self.driver
        browser.get(link)
        browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class, 'first')]").send_keys(
            "firstName")
        browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class, 'second')]").send_keys(
            "lastName")
        browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class, 'third')]").send_keys(
            "test@test.ru")
        browser.find_element(By.XPATH, "//div[@class='second_block']//input[contains(@class, 'first')]").send_keys(
            "88005553555")
        browser.find_element(By.XPATH, "//div[@class='second_block']//input[contains(@class, 'second')]").send_keys(
            "Moscow")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        text = browser.find_element(By.XPATH, "//h1").text
        self.assertEqual(text, "Congratulations! You have successfully registered!")

        def tearDown(self):
            self.driver.close()




if __name__ == "__main__":
    unittest.main()