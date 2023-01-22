import requests
import json
import re


class Uploader:

    def __init__(self):
        self.API_URL = "https://api.monday.com/v2"
        self.API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjIyNzA0Njg1OSwidWlkIjozODMwMzYxOSwiaWFkIjoiMjAyMy0wMS0yMVQxODoxMDoyNC4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTQyMjEwNTEsInJnbiI6InVzZTEifQ.i68dD8tqnRb2iomIapJgyWRoqYT5Nmmmr1s8FzFp5s8"
        self.PEOPLE_BOARD_ID = '3834651575'
        self.headers = {"Content-Type" : "application/json", "Authorization": self.API_KEY}

    def upload_employee_data(self, input_from_paycom: list):
        for each in input_from_paycom:
            name = each['name']
            if each['Status'] == 'Active':
                status = 'Working'
            else:
                status = ""
            for key in each.keys():
                if 'Phone Number' in key:
                    phone = re.sub('[\s()-]', "", each[key])
            bti_email = each['Email - Work']
            personal_email = each['Email - Personal']
            temp_date_list = each['Hire Date'].split('/')
            start_date = temp_date_list[2] + "-" + temp_date_list[0] + "-" + temp_date_list[1]
            title = each['position']

            query = 'mutation ($myItemName: String!, $columnVals: JSON!) { create_item (board_id:' + self.PEOPLE_BOARD_ID + 'item_name:$myItemName, column_values:$columnVals) { id } }'

            vars = {
                'myItemName': name,
                'columnVals': json.dumps({
                    'status': {'label': status},
                    'phone4': {'phone': phone, 'countryShortName': 'US'},
                    'email1': {'email': bti_email, 'text': bti_email},
                    'email17': {'email': personal_email, 'text': personal_email},
                    'date4': {'date': start_date},
                    'text1': {'text': title}
                })
            }

            data = {'query': query, 'variables': vars}

            r = requests.post(url=self.API_URL, json=data, headers=self.headers)
            print(r.json)
            print(r.text)

    def get_all_boards(self):
        query = '{ boards {name id} }'
        data = {'query': query}

        r = requests.post(url=self.API_URL, json=data, headers=self.headers)
        print(r.json)
        print(r.text)

    def get_single_board_data(self, board_id):
        query2 = '{boards(ids: ' + board_id + ') { name id description items { name id column_values{title id type text } } } }'
        data = {'query': query2}

        r = requests.post(url=self.API_URL, json=data, headers=self.headers)
        print(r.json)
        print(r.text)


if __name__ == '__main__':
    TEST_DATA = [{'name': 'Patrick An', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Cell)': '+1 (847) 858-2294', 'Email - Work': 'patrick.an@emp.btisolutions.com', 'Email - Personal': 'patrickan101@gmail.com', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Kiwook Kang', 'Manager - Tertiary': 'Sang Hun Lee', 'Manager - Time Off': 'Sangjun Lee', 'Hire Date': '07/25/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'patrickan101@gmail.com', 'Primary Org': 'Mobis [54]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-4797]', 'Works-In State': 'Michigan', 'Lives-In State': 'Michigan', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': '1', 'Document Group': 'All Employees [ALL]', 'Date Added to Paycom': '07/21/2022'}, {'name': 'Min Woo Choi', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Cell)': '+1 (213) 598-4053', 'Email - Work': 'min.choi@emp.btisolutions.com', 'Email - Personal': 'minwcqa@gmail.com', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Kiwook Kang', 'Manager - Time Off': 'Sangjun Lee', 'Hire Date': '04/18/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'minwcqa@gmail.com', 'Primary Org': 'HAEA [61]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-0684]', 'Works-In State': 'California', 'Lives-In State': 'California', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': 'N/A', 'Document Group': 'All Employees [ALL]', 'Date Added to Paycom': '04/14/2022'}, {'name': 'Jaeho Han', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Cell)': '+1 (909) 963-8128', 'Email - Work': 'jaeho.han@emp.btisolutions.com', 'Email - Personal': 'gkswogh7220@gmail.com', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Jae Ho Jung', 'Manager - Tertiary': 'Sang Hun Lee', 'Manager - Time Off': 'Sangjun Lee', 'Hire Date': '02/01/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'gkswogh7220@gmail.com', 'Primary Org': 'HAEA [61]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-1934]', 'Works-In State': 'California', 'Lives-In State': 'California', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': '2', 'Document Group': 'All Employees [ALL]', 'Date Added to Paycom': '01/19/2022'}, {'name': 'Ha Young Kim', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Cell)': '+1 (864) 986-1633', 'Email - Work': 'hayoung.kim@emp.btisolutions.com', 'Email - Personal': 'rlagkdud0129@gmail.com', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Kiwook Kang', 'Manager - Tertiary': 'Sang Hun Lee', 'Manager - Time Off': 'Sangjun Lee', 'Hire Date': '03/28/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'rlagkdud0129@gmail.com', 'Primary Org': 'Mobis [54]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-4153]', 'Works-In State': 'Michigan', 'Lives-In State': 'Michigan', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': '1', 'Document Group': 'All Employees [ALL]', 'Date Added to Paycom': '03/23/2022'}, {'name': 'Hyunah Kim', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Cell)': '+1 (732) 519-2563', 'Email - Work': 'hyunah.kim@emp.btisolutions.com', 'Email - Personal': 'kunique74@gmail.com', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Jae Ho Jung', 'Manager - Tertiary': 'Sang Hun Lee', 'Manager - Time Off': 'Kiwook Kang', 'Hire Date': '03/28/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'kunique74@gmail.com', 'Primary Org': 'Mobis [54]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-4383]', 'Works-In State': 'Michigan', 'Lives-In State': 'Michigan', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': '1', 'Document Group': 'All Employees [ALL]', 'Date Added to Paycom': '03/23/2022'}, {'name': 'Jiwon Kim', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Cell)': '+1 (248) 752-8638', 'Email - Work': 'jiwon.kim@emp.btisolutions.com', 'Email - Personal': 'jiwonee27@gmail.com', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Kiwook Kang', 'Manager - Tertiary': 'Jae Ho Jung', 'Manager - Time Off': 'Sangjun Lee', 'Hire Date': '10/17/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'jiwonee27@gmail.com', 'Primary Org': 'Mobis [54]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-5740]', 'Works-In State': 'Michigan', 'Lives-In State': 'Michigan', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': 'N/A', 'Document Group': 'N/A', 'Date Added to Paycom': '10/11/2022'}, {'name': 'Siwon Kim', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Cell)': '+1 (951) 776-7993', 'Email - Work': 'siwon.kim@emp.btisolutions.com', 'Email - Personal': 'si1kim001@gmail.com', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Kiwook Kang', 'Manager - Tertiary': 'Sang Hun Lee', 'Manager - Time Off': 'Sangjun Lee', 'Hire Date': '02/01/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'si1kim001@gmail.com', 'Primary Org': 'HAEA [61]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-8209]', 'Works-In State': 'Michigan', 'Lives-In State': 'Michigan', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': 'N/A', 'Document Group': 'All Employees [ALL]', 'Date Added to Paycom': '01/27/2022'}, {'name': 'Sungwoo Kim', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Cell)': '+1 (479) 571-0372', 'Email - Work': 'sungwoo.kim@emp.btisolutions.com', 'Email - Personal': 'sk074@uark.edu', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Kiwook Kang', 'Manager - Tertiary': 'Sang Hun Lee', 'Manager - Time Off': 'Sangjun Lee', 'Hire Date': '07/04/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'sk074@uark.edu', 'Primary Org': 'Mobis [54]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-0002]', 'Works-In State': 'Michigan', 'Lives-In State': 'Michigan', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': 'N/A', 'Document Group': 'All Employees [ALL]', 'Date Added to Paycom': '06/30/2022'}, {'name': 'Johannes Lee', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Home)': '+1 (919) 741-3700', 'Email - Work': 'johannes.lee@emp.btisolutions.com', 'Email - Personal': 'sangjae321@gmail.com', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Kiwook Kang', 'Manager - Tertiary': 'Sang Hun Lee', 'Manager - Time Off': 'Sangjun Lee', 'Hire Date': '03/28/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'johanneslee47@gmail.com', 'Primary Org': 'Mobis [54]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-9020]', 'Works-In State': 'Michigan', 'Lives-In State': 'Michigan', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': '1', 'Document Group': 'All Employees [ALL]', 'Date Added to Paycom': '03/23/2022'}, {'name': 'Junho Lee', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Other)': '+1 (979) 393-8894', 'Email - Work': 'junho.lee@emp.btisolutions.com', 'Email - Personal': 'leej0956@tamu.edu', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Kiwook Kang', 'Manager - Tertiary': 'Sang Hun Lee', 'Manager - Time Off': 'Sangjun Lee', 'Hire Date': '07/25/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'leej0956@tamu.edu', 'Primary Org': 'Mobis [54]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-6249]', 'Works-In State': 'Michigan', 'Lives-In State': 'Michigan', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': 'N/A', 'Document Group': 'All Employees [ALL]', 'Date Added to Paycom': '07/22/2022'}, {'name': 'Seungdeok Lim', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Cell)': '+1 (312) 241-0728', 'Email - Work': 'seungdeok.lim@emp.btisolutions.com', 'Email - Personal': 'slim20@hawk.iit.edu', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Kiwook Kang', 'Manager - Time Off': 'Sangjun Lee', 'Hire Date': '02/15/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'slim20@hawk.iit.edu', 'Primary Org': 'AVAE [62]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-0236]', 'Works-In State': 'Michigan', 'Lives-In State': 'Michigan', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': '1', 'Document Group': 'All Employees [ALL]', 'Date Added to Paycom': '02/09/2022'}, {'name': 'Tae Young Moon', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Other)': '+1 (332) 216-8908', 'Email - Work': 'taeyoung.moon@emp.btisolutions.com', 'Email - Personal': 'tym3628@gmail.com', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Kiwook Kang', 'Manager - Tertiary': 'Sang Hun Lee', 'Manager - Time Off': 'Sangjun Lee', 'Hire Date': '06/06/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'tym3628@gmail.com', 'Primary Org': 'Mobis [54]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-4442]', 'Works-In State': 'Michigan', 'Lives-In State': 'Michigan', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': '1', 'Document Group': 'All Employees [ALL]', 'Date Added to Paycom': '05/19/2022'}, {'name': 'Minkyu Song', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Other)': '+1 (320) 339-3122', 'Email - Work': 'minkyu.song@emp.btisolutions.com', 'Email - Personal': 'minkyusongmn@outlook.com', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Kiwook Kang', 'Manager - Time Off': 'Sangjun Lee', 'Hire Date': '07/18/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'minkyusongmn@outlook.com', 'Primary Org': 'Mobis [54]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-1257]', 'Works-In State': 'Michigan', 'Lives-In State': 'Michigan', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': 'N/A', 'Document Group': 'All Employees [ALL]', 'Date Added to Paycom': '07/14/2022'}, {'name': 'Junghwan Yim', 'position': 'Network Engineer- Telematics Validation', 'Phone Number - Primary (Cell)': '+1 (716) 429-6355', 'Email - Work': 'junghwan.yim@emp.btisolutions.com', 'Email - Personal': 'jyim@buffalo.edu', 'Manager - Primary': 'Sangjun Lee', 'Manager - Secondary': 'Kiwook Kang', 'Manager - Time Off': 'Sangjun Lee', 'Hire Date': '10/31/2022', 'Primary Supervisor': 'Sangjun Lee', 'Status': 'Active', 'Pay Type': 'Hourly', 'ESS Login': 'jyim@buffalo.edu', 'Primary Org': 'HAEA [61]', 'Manager': 'Sangjun Lee [EM03]', 'Division': 'Division-S [1-2]', 'Terminal': 'TG3', 'Schedule Group': 'N/A', 'Badge Number': 'N/A', 'Pay Frequency': 'Bi-Weekly', 'Most Recent Check': '01/20/2023', 'ESS Access Profile': 'Use Default Profile', 'Last 4 Digits of SSN': '[XXX-XX-0290]', 'Works-In State': 'Michigan', 'Lives-In State': 'Michigan', 'Exempt Status': 'Non-Exempt', 'Last Position Change Date': '12/27/2022', 'Pending Time-Off Requests': 'N/A', 'On-Leave Start': 'N/A', 'On-Leave End': 'N/A', '401(k) Eligibility Date': 'N/A', 'Outstanding Checklists': '1', 'Document Group': 'N/A', 'Date Added to Paycom': '10/27/2022'}]

    uploader = Uploader()

    uploader.get_all_boards()
    uploader.get_single_board_data('3850742138')
    # uploader.upload_employee_data(TEST_DATA)
