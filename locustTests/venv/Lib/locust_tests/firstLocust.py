from locust import TaskSet, task, HttpUser
from venv.Lib.locust_tests.sessionData import SessionData

class MyUser(HttpUser):

    min_wait = 5000
    max_wait = 10000
    host = "https://app.namastefit.one"

    def __init__(self, parent):
        super().__init__(parent)
        self.cookie = SessionData.secureCookieUser1

    @task(1)
    def login_post(self):
        headers = {"set-cookie:": self.cookie}
        response = self.client.get("/home/get-started", headers)
        print("Response status code:", response.status)
        print("Response status code:", response.content)
