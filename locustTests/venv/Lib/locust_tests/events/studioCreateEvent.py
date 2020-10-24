from locust import TaskSet, task, HttpUser
from venv.Lib.locust_tests.sessionData import SessionData

# http://app.namastefit.one/api/studio/39e1a685-0893-42fa-a895-ef3153a59179
# userData=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjdkN2NiMDBiLWZiZDMtNDIyMi1iZmM5LTkzNzI0Yjg2MWJiOSIsImlhdCI6MTYwMzUxMzM0OCwiZXhwIjoxNjAzNTk5NzQ4fQ.0bnz7aNatYIfTsIflU1_fKPFWD--QNZT-pdLHUcteCI

class MyUser(HttpUser):
    min_wait = 5000
    max_wait = 10000
    host = "https://app.namastefit.one"

    def __init__(self, parent):
        super().__init__(parent)
        self.cookie =SessionData.userdataCookieUser1
        self.userId = SessionData.user1Id

    @task(1)
    def login_post(self):
        headersCookie = {"Cookie:": self.cookie}
        response = self.client.post("/api/event/" + self.userId, headersCookie, params={
            "about": "Yoga 101",
            "confLink": "https://zoom.us/",
            "duration": "60",
            "eventCost": "",
            "freeEvent": "true",
            "frequency": 4,
            "name": "Yoga 101",
            "startTime": "2020-10-24T11:06",
            "status": "active",
            "stratDate": "2020-10-24T05:36:52.464Z",
            "timezone": "Asia/Kolkata"
        })
        print("Response status code:", response)
        # print("Response status code:", response.content)
