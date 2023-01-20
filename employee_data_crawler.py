from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import time
import requests


class EmployeeDataCrawler:

    def __init__(self, selenium_driver: webdriver):
        self.driver: webdriver = selenium_driver

        self.run()

    def run(self):
        self.driver.get("https://www.paycomonline.net/v4/cl/web.php/employee/changes")
        delay = 10
        WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'css-vkr5jj')))
        print("'Make Employee Changes' page loaded")
        # html = self.driver.page_source
        # print(html)
        '''
        print("#########################################################################\n\n\n\n\n")

        session = requests.Session()
        selenium_user_agent = self.driver.execute_script("return navigator.userAgent;")
        session.headers.update({"user-agent": selenium_user_agent})

        for cookie in self.driver.get_cookies():
            session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])

        response = session.get("https://www.paycomonline.net/v4/cl/web.php/employee/changes")
        print(response.content)
        '''

        self.driver.find_element(By.CLASS_NAME, 'css-vkr5jj').click()

        # WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'jssEEFormsRewrite64 css-1a2a2s7')))
        time.sleep(3)

        self.driver.find_element(By.CLASS_NAME, 'jssEEFormsRewrite64 css-yjkc7l').click()
        time.sleep(3)

        print(self.driver.find_element(By.CLASS_NAME, 'jssEEFormsRewrite1 jssEEFormsRewrite9 jssEEFormsRewrite32').text)
