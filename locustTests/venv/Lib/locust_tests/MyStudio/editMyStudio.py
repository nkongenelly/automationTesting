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
        self.userData = SessionData.userdataCookieUser1
        self.cookie = SessionData.secureCookieUser1
        self.userId = SessionData.user1Id


    @task(1)
    def get_my_studio(self):
        headers = {"set-cookie:": self.cookie}
        response = self.client.get(url="/api/studio/" + self.userId, cookies={"userData": self.userData})
        # jsonResponse = response.json().get('studio')

        # Responsee = response.json()
        print("Response status code:", response.content)
        # print("Response status code:", jsonResponse['domain'])
        # return jsonResponse['domain']

    # @task(1)
    # def get_specific_domain_studio(self):
    #     self.domain = self.get_my_studio()
    #     print('DOMAIN = ')
    #     print(self.domain)
    #     response = self.client.get(url="/api/studio/" + self.userId + "/" + self.domain,
    #                                cookies={"userData": self.userData})
    #     print("Response status code:", response.status_code)
    #
    # @task(5)
    # def edit_my_studio(self):
    #     self.domain = self.get_my_studio()
    #     response = self.client.put(url="/api/studio/" + self.userId,
    #                                cookies={"userData": self.userData},
    #                                data={"about": "Yoga lifestyle",
    #                                      "city": "",
    #                                      "country": "",
    #                                      "cover_photo_url": "https://namastedotfitstaging-public.s3.ap-south-1.amazonaws.com/yogacover/maryjoy-caballero-Um3NiahMQPY-unsplash.jpg",
    #                                      "domain": self.domain,
    #                                      "facebook_link": "",
    #                                      "insta_link": "",
    #                                      "name": "Yoga lifestyle",
    #                                      "profile_photo_url": "",
    #                                      "state": "",
    #                                      "status": "active",
    #                                      "website_link": "https://www.google.com",
    #                                      "youtube_link": ""})
    #     print("Response status code:", response.status_code)
