from locust import TaskSet, task, HttpUser, User, constant, user
from venv.Lib.locust_tests.sessionData import SessionData
from venv.Lib.locust_tests.users import USER_CREDENTIALS
import logging, sys


# http://app.namastefit.one/api/studio/39e1a685-0893-42fa-a895-ef3153a59179
# userData=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjdkN2NiMDBiLWZiZDMtNDIyMi1iZmM5LTkzNzI0Yjg2MWJiOSIsImlhdCI6MTYwMzUxMzM0OCwiZXhwIjoxNjAzNTk5NzQ4fQ.0bnz7aNatYIfTsIflU1_fKPFWD--QNZT-pdLHUcteCI

class RegisterForEvent(TaskSet):
    wait_time = constant(1)
    email = "EMPTY"
    name = "EMPTY"
    phone = "EMPTY"

    def __init__(self, parent):
        super().__init__(parent)
        # self.userId = SessionData.user1Id

    def on_start(self):
        if len(USER_CREDENTIALS) > 0:
            self.email, self.name, self.phone = USER_CREDENTIALS.pop()

    @task
    def login(self):
        response = self.client.post(
            "/api/eventRegister/08c61670-6aba-4de8-b208-429028088948/ff3d8a13-f694-486e-b176-c0ea51e37b57", {
                "email": self.email,
                "name": self.name,
                "phone": self.phone
            })
        print("Response status code:", response)
        # print("Response status code:", response.content)
        logging.info('Registration  with %s email and %s name and %s phone number', self.email, self.name, self.phone)


class LoginWithUniqueUsersTest(HttpUser):
    tasks = {RegisterForEvent:2}
    host = "https://nellyyogas.namastefit.one"
    # sock = None
    min_wait = 5000
    max_wait = 10000

    # def __init__(self, parent):
    #     super(LoginWithUniqueUsersTest, self).__init__(parent)
