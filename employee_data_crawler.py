from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import time


class EmployeeDataCrawler:

    def __init__(self, selenium_driver: webdriver):
        self.driver: webdriver = selenium_driver
        self.run()

    def run(self):
        self.driver.get("https://www.paycomonline.net/v4/cl/web.php/employee/changes")
        delay = 10
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'css-vkr5jj')))
        print("'Make Employee Changes' page loaded")
        self.fetch_one_employee_info()

    def fetch_one_employee_info(self):

        users = self.driver.find_elements(By.CLASS_NAME, 'css-vkr5jj')
        for idx in range(len(users) - 1):
            user = users[idx]
            user.find_element(By.TAG_NAME, 'button').click()
            name = self.driver.find_element(By.CLASS_NAME, 'css-ewvkoh').find_element(By.CLASS_NAME, 'jssEEFormsRewrite17').text
            position = self.driver.find_element(By.CLASS_NAME, 'css-eix830').text

            print(name)
            print(position)

            time.sleep(1)
            users = self.driver.find_elements(By.CLASS_NAME, 'css-vkr5jj')






        # self.driver.find_element(By.CLASS_NAME, 'css-vkr5jj').click()
        #
        # # time.sleep(3)
        #
        # one_employee_panel = self.driver.find_element(By.CLASS_NAME, 'css-927gzi')
        #
        # for elem in one_employee_panel.find_elements(By.CLASS_NAME, 'jssEEFormsRewrite237') :
        #     elem.click()
        #
        #     elem
        #     time.sleep(2)
        #
        #
        #
        #
        #
        # # WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'jssEEFormsRewrite64 css-1a2a2s7')))
        # for each in one_employee_panel.find_elements(By.CLASS_NAME, 'jssEEFormsRewrite1.jssEEFormsRewrite17'):
        #     print(each.text)
        #
        # # print(one_employee_panel.find_element(By.CLASS_NAME, 'css-eix830').text)
        #
        # print(one_employee_panel.find_element(By.CSS_SELECTOR, '.jssEEFormsRewrite64.css-yjkc7l').text)
        # # one_employee_panel.find_element(By.CSS_SELECTOR, '.jssEEFormsRewrite64.css-yjkc7l').click()
        # time.sleep(3)
        #
        # print(one_employee_panel.find_element(By.CLASS_NAME, 'css-djbxmn').text)
        # time.sleep(3)
        #
        # one_employee_panel.find_element(By.CSS_SELECTOR, '.jssEEFormsRewrite64.css-yjkc7l').click()
        # time.sleep(3)
        #
        # print(one_employee_panel.find_element(By.CLASS_NAME, 'css-djbxmn').text)
        # time.sleep(3)
        #
        # one_employee_panel.find_element(By.CSS_SELECTOR, '.jssEEFormsRewrite64.css-yjkc7l').click()
        #
        # time.sleep(3)


