from driver_manager import DriverManager
from employee_data_crawler import EmployeeDataCrawler
from time_off_calendar_crawler import TimeOffCalendarCrawler
from uploader import Uploader
import os
import sys


class Main:

    def __init__(self):
        self.driver_manager = DriverManager()
        self.driver = None

        if getattr(sys, 'frozen', False):
            self.base_dir = os.path.dirname(sys.executable)
        else:
            self.base_dir = os.path.dirname(__file__)

    def get_session_ready(self) -> bool:
        username, password = self.username_password_input()
        login_result = self.driver_manager.login(username, password)
        if login_result == True:
            self.driver = self.driver_manager.driver_hand_over()
            return True
        else:
            return False

    def username_password_input(self) -> (str, str):
        print('Client - Paycom Username:')
        username = input()
        print('Client - Paycom Password')
        password = input()
        return username, password

    def terminate(self):
        self.driver.quit()


if __name__ == "__main__":
    main = Main()
    is_session_ready = main.get_session_ready()
    if is_session_ready == True:
        print("LOGIN SUCCESSFUL. SESSION IS READY.")
    else:
        print("ERROR. LOGIN FAILED. SESSION IS NOT READY.")
        exit()

    employee_data_crawler = EmployeeDataCrawler(main.driver_manager.driver_hand_over())
    fetched_employee_data = employee_data_crawler.run()

    print(fetched_employee_data)
    f = open("RESULT_paycom_employee_data.txt", "w")
    f.write(str(fetched_employee_data))
    f.close()

    time_off_calendar_crawler = TimeOffCalendarCrawler(main.driver_manager.driver_hand_over())
    fetched_time_off_calendar_data = time_off_calendar_crawler.run()

    print(fetched_time_off_calendar_data)
    f = open("RESULT_paycom_time_off_calendar_data.txt", "w")
    f.write(str(fetched_time_off_calendar_data))
    f.close()

    # uploader = Uploader()
    # uploader.upload_employee_data(fetched_employee_data)

    main.terminate()

