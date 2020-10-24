# from locust import TaskSet, task, HttpLocust
# from venv.Lib.locust_tests.sessionData import SessionData

# class UserBehaviour(TaskSet):
#     @task
#     def login_post(self):
#         self.cookie = ""
#         headersDict = {":authority": "play.google.com",
#                         ":method": "POST",
#                         ":path": "/log?format=json&hasfast=true",
#                         ":scheme": "https",
#                         "accept": "*/*",
#                         "accept-encoding": {"gzip", "deflate", "br"},
#                         "accept-language":{" en-KE","en-US","q=0.9","en","q=0.8"},
#                         "authorization": "SAPISIDHASH 6267d3b4a9d4e7e34d7ff62260ee5121fd186308",
#                         "content-length": 1396,
#                         "content-type": "application/x-www-form-urlencoded","charset=UTF-8",
#                         "cookie": CONSENT=YES+KE.en+20170618-09-0; PLAY_ACTIVE_ACCOUNT=ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=nkongenelly94@gmail.com; _ga=GA1.3.1567416131.1602102410; OTZ=5663307_34_34__34_; SEARCH_SAMESITE=CgQI_ZAB; HSID=AcJlLK99MfeZdLSNp; SSID=AWS-PBzTf137itLRg; APISID=Lkw7gArAoGlFzn9F/AshBZihRlMxk0UYo4; SAPISID=YLO7yNXZi9KVhvKn/AKhF_dxZ0csBxnUWB; __Secure-3PAPISID=YLO7yNXZi9KVhvKn/AKhF_dxZ0csBxnUWB; SID=2wf2D2sql9UosS7wyTFUseWiW1hxe4ugr34OQ4HJEEOw_qMhZZu_EGzzUI2UDXBMLg8pvQ.; __Secure-3PSID=2wf2D2sql9UosS7wyTFUseWiW1hxe4ugr34OQ4HJEEOw_qMh_KwNzF6i962fSSAQmcSjdA.; NID=204=tBLf7muY-GvEqmkSCa2JCxhWZpCuP7pPl--7KxJPZGNw_UrTbWA8eC6HYU-OeoBYsmFtPnyaZqMMCxYcOpix4uGpaXp0DMr0ogeEufbAXhCvCoaI9D83sW_YXYHpjeO_sb1wNzOgdl_I77ULvDatDZKCWOtGLFd8Mt90rnpv1EGnnQTALlATu32OcpLA8ahy9s7dYphCWj15Fb3h9qb9Hwnk8SSeAkB24UfM32V6vE5krARNU4B6I_jZGPZiLTguDRN7oOToul7I0N6GRQMY31CWyc_BMTtaFMYiinwrgsF7hCJ8tgeXeo8GRtHvcMMm8NVeAl3FTb8PO8AR5ckcS0tKlRLwXAYYn8nlFPajYgQyvScvWqsiNwl2sHclaiGQmxxLVQkyPrp22ZDzaxSdwhtmd00no2sMmQPu520; 1P_JAR=2020-10-24-04; SIDCC=AJi4QfFh9vwlzatEqoCgUdshVE2_I2w4BrSYCsNgWz9Ml43s1vmS3E8uuzqbcmyDPi6RlWLgeeBC; __Secure-3PSIDCC=AJi4QfEWyIU3tQSwt8xEdw4bcnDD3hqXsuuBPvYaMMkqt6Mb1ZAllziMB9_SQaFlRvCjoQtUzgg
#                         origin: https://accounts.google.com
#                         referer: https://accounts.google.com/
#                         sec-fetch-dest: empty
#                         sec-fetch-mode: cors
#                         sec-fetch-site: same-site
#                         user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
#                         x-client-data: CIe2yQEIprbJAQjBtskBCKmdygEIlLjKAQisx8oBCPXHygEI58jKAQjpyMoBCLTLygEI3NXKAQi02MoBGIrBygE=
#                         Decoded:
#                         message ClientVariations {
#                           // Active client experiment variation IDs.
#                           repeated int32 variation_id = [3300103, 3300134, 3300161, 3313321, 3316756, 3318700, 3318773, 3318887, 3318889, 3319220, 3320540, 3320884];
#                           // Active client experiment variation IDs that trigger server-side behavior.
#                           repeated int32 trigger_variation_id = [3317898];
#                         }
#                                }
#         response = self.client.post(
#             url ="/home/get-started",
#             headers = headersDict)
#         print("Response status code:", response.status)
#         print("Response status code:", response.content)
#
# class User(HttpLocust):
#     task_set = UserBehaviour
#     min_wait = 5000
#     max_wait = 10000
#     host = "https://app.namastefit.one"