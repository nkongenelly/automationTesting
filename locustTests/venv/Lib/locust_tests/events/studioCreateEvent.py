import json

import requests
from locust import TaskSet, task, HttpUser, constant
from locustTests.venv.Lib.locust_tests.sessionData import SessionData
from locustTests.venv.Lib.locust_tests.sessionData import SessionData
from locustTests.venv.Lib.locust_tests.loginGoogleFirst import LoginGoogle
from locustTests.venv.Lib.locust_tests.users import USER_STUDIO_IDS
from locustTests.venv.Lib.locust_tests.users import CREATE_EVENT

class MyAuth(requests.auth.AuthBase):
    def __call__(self, r):
        # Implement my authentication
      return r

# >>> url = 'https://httpbin.org/get'
# >>> requests.get(url, auth=MyAuth())
class MyUser(HttpUser):
    wait_time = constant(1)
    min_wait = 5000
    max_wait = 10000
    host = "https://app.namastefit.one"



    # def on_start(self):
        # if len(CREATE_EVENT) > 0:
        #     self.gmail, self.studio = CREATE_EVENT.pop()
        #
        # if len(USER_STUDIO_IDS) > 0:
        #     self.userId, self.studioId = USER_STUDIO_IDS.pop()

    @task(1)
    def login_post(self):
        s = requests.Session()
        auth = LoginGoogle().logingoogle()
        print("cookie saved now is =", auth)
        # Note that domain keyword parameter is the only optional parameter here
        cookie_obj = requests.cookies.create_cookie(domain='app.namastefit.one', name='userData',
                                                    value=auth)
        s.cookies.set_cookie(cookie_obj)
        # s.get(self.gmail, auth=MyAuth())
        # s.get('https://app.namastefit.one/home/studio/')
        print(s.cookies)
        print(s.headers)
        print(MyAuth())
        # print(json.loads(s.cookies))

        # response = s.get('https://app.namastefit.one/api/studio/' + self.studio)
        # s.post('https://localhost/login.py', login_data)
        # logged in! cookies saved for future requests.
        # r2 = s.get('https://localhost/profile_data.json', ...)
        # cookies sent automatically!
        # do whatever, s will keep your cookies intact :)
        # response = self.client.post("/api/event/" + self.userId, headersCookie, params={
        s.headers["Referer"] = "https://app.namastefit.one/home/create-event"
        response = s.post("https://app.namastefit.one/api/event/" + self.studio, s.cookies,
        {
            "user_id": self.userId,
            "studio_id": self.studioId,
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
        print("Response status code:", response.content)
        # print("Response status code:", response.content)
