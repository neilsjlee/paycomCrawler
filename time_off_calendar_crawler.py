from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime
import util


class TimeOffCalendarCrawler:

    def __init__(self, selenium_driver: webdriver):
        self.driver: webdriver = selenium_driver

    def run(self) -> list:
        self.driver.get("https://www.paycomonline.net/v4/cl/web.php/pto/calendar")
        delay = 10
        WebDriverWait(self.driver, delay).until(
            expected_conditions.presence_of_element_located((By.ID, 'calendar')))
        print("'Time-Off Calendar' page loaded")
        time.sleep(2)
        return self.fetch_time_off_info()

    def fetch_time_off_info(self) -> list:
        number_of_previous_months = 2
        number_of_next_months = 2

        calendar = self.driver.find_element(By.ID, 'calendar')
        prev_month_button = calendar.find_element(By.CLASS_NAME, 'fc-button-prev')
        next_month_button = calendar.find_element(By.CLASS_NAME, 'fc-button-next')

        for cnt in range(number_of_previous_months):
            prev_month_button.click()
            time.sleep(3)

        result = []
        for cnt in range(number_of_previous_months + number_of_next_months + 1):

            month = datetime.strptime(self.driver.find_element(By.CLASS_NAME, 'fc-header-title').text, "%B %Y")

            this_month_calendar = self.driver.find_element(By.CLASS_NAME, 'fc-content')
            this_month_events = this_month_calendar.find_elements(By.CLASS_NAME, 'fc-event')

            for idx in range(len(this_month_events)):

                this_month_events[idx].click()
                time.sleep(2.5)

                date = datetime.strptime(self.driver.find_element(By.ID, 'daydesc').text, "%B %d %Y")
                if month.strftime("%b") == date.strftime("%b"):
                    requests_tab = self.driver.find_element(By.ID, 'requests')
                    requests = requests_tab.find_elements(By.CLASS_NAME, 'table-responsive')
                    for each_request in requests:
                        request_data = {}
                        request_data['Date'] = date.strftime("%Y-%m-%d")
                        table = each_request.find_element(By.CLASS_NAME, 'middle')
                        rows = table.find_elements(By.TAG_NAME, 'tr')
                        for each_row in rows:
                            single_column_data_cnt = 0
                            columns = each_row.find_elements(By.TAG_NAME, 'td')
                            if len(columns) == 1:
                                request_data['single_column_data' + str(single_column_data_cnt)] = util.name_formatter(columns[0].text)
                            elif len(columns) == 2:
                                request_data[columns[0].text] = columns[1].text
                        result.append(request_data)

                this_month_events = self.driver.find_elements(By.CLASS_NAME, 'fc-event')

            next_month_button.click()
            time.sleep(3)

        return result




