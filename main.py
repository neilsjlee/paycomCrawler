from driver_manager import DriverManager
from employee_data_crawler import EmployeeDataCrawler


class Main:

    def __init__(self):
        self.driver_manager = DriverManager()
        self.driver = None

    def get_session_ready(self) -> bool:
        login_result = self.driver_manager.login()
        if login_result == True:
            self.driver = self.driver_manager.driver_hand_over()
            return True
        else:
            return False


if __name__ == "__main__":
    main = Main()
    is_session_ready = main.get_session_ready()
    if is_session_ready == True:
        print("LOGIN SUCCESSFUL. SESSION IS READY.")
    else:
        print("ERROR. LOGIN FAILED. SESSION IS NOT READY.")
        exit()

    employee_data_crawler = EmployeeDataCrawler(main.driver_manager.driver_hand_over())
    fetched_data = employee_data_crawler.run()

    print(fetched_data)


