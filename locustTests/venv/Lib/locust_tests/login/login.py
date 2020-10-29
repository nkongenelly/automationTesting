import requests
from locust import TaskSet, task, HttpUser, constant
from locustTests.venv.Lib.locust_tests.sessionData import SessionData
from locustTests.venv.Lib.locust_tests.users import CREATE_EVENT

# locustTests>locust -f venv\Lib\locust_tests\login\login.py --host https://app.namastefit.one
#
class GoogleLogin(HttpUser):
    wait_time = constant(1)

    def on_start(self):
        if len(CREATE_EVENT) > 0:
            self.gmail, self.studio = CREATE_EVENT.pop()

    @task(1)
    def selectemail(self):
        s = requests.Session()
        s.get(self.gmail)
        response = s.get('https://app.namastefit.one/api/studio/'+self.studio)
        print("Response cookies = ", s.cookies)
        print("Response cookies = ", response.content)

