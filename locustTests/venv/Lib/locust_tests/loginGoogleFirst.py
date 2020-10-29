import json
import unittest
from locustTests.venv.Lib.locust_tests.Common.googleLogin import Google as AuthLogin

# suite = unittest.TestSuite()
# suite.addTest(AuthLogin('setUp'))
# suite.addTest(AuthLogin('test_login'))
# print(suite)
# unittest.TextTestRunner().run(suite)
class LoginGoogle():
    def logingoogle(self):
        # if __name__ == '__main__':
        authLogin = AuthLogin()
        authLogin.setUp()
        authLogin1 = authLogin.test_login()
        print("authLogin1 = ", authLogin1)


        with open('userData.json', 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)

        # print(json_object['userData'])
        return json_object['userData']


        # print(type(json_object))


LoginGoogle().logingoogle()
