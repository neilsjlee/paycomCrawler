from selenium_driver_updater import DriverUpdater
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import os
import time

CLIENT_CODE = '0UE96'
USERNAME = 'sangjunlee'
PASSWORD = 'btiNeh@85246'


class DriverManager:

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        print("temp test")
        self.filename = DriverUpdater.install(path=self.base_dir, driver_name=DriverUpdater.chromedriver, upgrade=True, check_driver_is_up_to_date=True, old_return=False)

        options = webdriver.ChromeOptions()
        print("Chrome User Data Path:", os.path.abspath(os.path.join(os.path.dirname(__file__), 'chrome_user_data')))
        options.add_argument("user-data-dir=" + os.path.abspath(os.path.join(os.path.dirname(__file__), 'chrome_user_data')))

        self.__driver = webdriver.Chrome(service=Service(self.filename), options=options)

    def try_login(self) -> bool:
        self.__driver.get('https://www.paycomonline.net/v4/cl/')
        self.__driver.find_element(By.ID, 'clientcode').send_keys(CLIENT_CODE)
        self.__driver.find_element(By.ID, 'username').send_keys(USERNAME)
        self.__driver.find_element(By.ID, 'password').send_keys(PASSWORD)

        self.__driver.find_element(By.ID, 'btnSubmit').click()

        try:
            delay = 60
            WebDriverWait(self.__driver, delay).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'welcomeText')))
            print("logged in")
            return True
        except TimeoutException:
            print("logging in took too much time!")
            return False

    def login(self) -> bool:
        login_result = self.try_login()
        login_trial_count = 0
        if login_result != True:
            while (self.try_login() != True):
                login_trial_count = login_trial_count + 1
                print(login_trial_count)
                if login_trial_count >= 2:
                    print("Tried logging in 3 times, but failed :(")
                    break

        return login_result

    def driver_hand_over(self):
        return self.__driver


if __name__ == '__main__':

    test_driver_manager = DriverManager()
    test_result = test_driver_manager.login()



