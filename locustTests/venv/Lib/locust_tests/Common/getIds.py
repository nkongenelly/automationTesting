import json

import requests
from locust import TaskSet, task, HttpUser
from venv.Lib.locust_tests.sessionData import SessionData


# http://app.namastefit.one/api/studio/39e1a685-0893-42fa-a895-ef3153a59179
# userData=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjdkN2NiMDBiLWZiZDMtNDIyMi1iZmM5LTkzNzI0Yjg2MWJiOSIsImlhdCI6MTYwMzUxMzM0OCwiZXhwIjoxNjAzNTk5NzQ4fQ.0bnz7aNatYIfTsIflU1_fKPFWD--QNZT-pdLHUcteCI

class GetIds(HttpUser):
    min_wait = 5000
    max_wait = 10000
    host = "https://app.namastefit.one"

    def __init__(self, parent):
        super().__init__(parent)
        self.userData = SessionData.userdataCookieUser1
        self.cookie = SessionData.secureCookieUser1
        self.userId = SessionData.user1Id


    @task(1)
    def get_my_studio(self):
        headers = {"userData:": self.cookie}
        s = requests.Session()
        response = s.get(url="https://app.namastefit.one/api/studio/" + self.userId, cookies={"userData": self.userData})
        # print(response.json())
        # jsonString = json.dumps(response.content)
        print(s.cookies)
        # jsonResponse = json.get('studio')
        # # jsonResponse = response.json().get('studio')
        #
        # # Responsee = response.json()
        # print("Response status code:", response.content)
        # # something if condition else something_else
        # print( "Response status code:", jsonResponse['domain']) if jsonResponse['domain'] else print("Empty")
        # print("Response status code:", jsonResponse['id']) if jsonResponse['domain'] else print("Empty")
        # # return jsonResponse['domain']
