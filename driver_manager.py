from selenium_driver_updater import DriverUpdater
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import os
import time
import pickle

CLIENT_CODE = '0UE96'
USERNAME = 'sangjunlee'
PASSWORD = 'btiNeh@85246'


class DriverManager:

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        self.filename = DriverUpdater.install(path=self.base_dir, driver_name=DriverUpdater.chromedriver, upgrade=True, check_driver_is_up_to_date=True, old_return=False)

        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:\\Path")  # Path to your chrome profile

        # self.driver = webdriver.Chrome(self.filename, options=options)
        self.driver = webdriver.Chrome(service=Service(self.filename), options=options)


    def login(self) -> bool:
        self.driver.get('https://www.paycomonline.net/v4/cl/')
        self.driver.find_element(By.ID, 'clientcode').send_keys(CLIENT_CODE)
        self.driver.find_element(By.ID, 'username').send_keys(USERNAME)
        self.driver.find_element(By.ID, 'password').send_keys(PASSWORD)

        self.driver.find_element(By.ID, 'btnSubmit').click()

        delay = 4

        try:
            myElem = WebDriverWait(self.driver, delay).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'welcomeText')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")


    def load_cookies(self):
        pass


if __name__ == '__main__':

    driver_manager = DriverManager()
    driver_manager.login()

    time.sleep(200)