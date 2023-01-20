from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
import time


class Crawler:

    def __init__(self, selenium_driver: webdriver):
        self.driver = selenium_driver
        self.url = ""

    def fetch_text(self, parent_element: WebElement, selector_type, selector) -> str:
        parent_element

