from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import time
import util


class EmployeeDataCrawler:

    def __init__(self, selenium_driver: webdriver):
        self.driver: webdriver = selenium_driver

    def run(self) -> list:
        self.driver.get("https://www.paycomonline.net/v4/cl/web.php/employee/changes")
        delay = 10
        WebDriverWait(self.driver, delay).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'css-vkr5jj')))
        print("'Make Employee Changes' page loaded")
        return self.fetch_one_employee_info()

    def fetch_one_employee_info(self) -> list:
        result = []

        users = self.driver.find_elements(By.CLASS_NAME, 'css-vkr5jj')
        for idx in range(len(users)):
            result_dict = {}

            user = users[idx]
            user.find_element(By.TAG_NAME, 'button').click()
            time.sleep(2)
            result_dict['name'] = util.name_formatter(
                self.driver.find_element(By.CLASS_NAME, 'css-ewvkoh').find_element(By.CLASS_NAME,
                                                                                   'jssEEFormsRewrite17').text)
            result_dict['position'] = self.driver.find_element(By.CLASS_NAME, 'css-eix830').text

            phones_emails_managers = self.driver.find_elements(By.CLASS_NAME, 'css-1uf4nsy')
            for index_no in range(3):
                phones_emails_managers[index_no].click()
                time.sleep(0.5)
                lines = self.driver.find_element(By.CLASS_NAME, 'css-djbxmn').text.splitlines()
                key, key_prefix, value = "", "", ""
                if index_no == 0:
                    key_prefix = "Phone Number"
                if index_no == 1:
                    key_prefix = "Email"
                if index_no == 2:
                    key_prefix = "Manager"
                cnt = 0
                for each in lines:
                    if index_no < 2:
                        if cnt % 2 == 0:
                            key = key_prefix + " - " + each
                        if cnt % 2 == 1:
                            value = each
                            result_dict[key] = value
                    else:
                        if cnt % 4 == 0:
                            key = key_prefix + " - " + each
                        if cnt % 4 == 2:
                            value = each
                            result_dict[key] = util.name_formatter(value)
                    cnt = cnt + 1
            left_tab_components = self.driver.find_element(By.CLASS_NAME, 'css-tol3un').find_elements(By.CLASS_NAME, 'css-j486mh')
            for each in left_tab_components:
                lines = each.text.splitlines()
                key, value = "", ""
                cnt = 0
                for line in lines:
                    if cnt%4 == 0:
                        key = line
                    if cnt%4 == 1:
                        value = line
                    cnt = cnt + 1
                result_dict[key] = util.name_formatter(value)

            employment_table = self.driver.find_element(By.CLASS_NAME, 'css-18hyvxw')
            contents = employment_table.find_elements(By.CLASS_NAME, 'css-j486mh')
            for each in contents:
                str_lines = each.text.splitlines()
                result_dict[str_lines[0]] = str_lines[1]

            result.append(result_dict)

            # users = self.driver.find_elements(By.CLASS_NAME, 'css-vkr5jj')

        return result
