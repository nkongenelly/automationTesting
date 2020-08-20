from namasteFit.TestServer.Locators.locators import Locators

drivers = [Locators.firefox_driver, Locators.chrome_driver]

for i in range(len(drivers)):
    print(drivers[i])

    def test_107(self):
        driver = self.driver
        # gc = gspread.service_account()
        #
        # sh = gc.open("userStoriesTestCases")
        #
        # print(sh.sheet1.get('A1'))

        credentials = ServiceAccountCredentials.from_json_keyfile_name(Locators.credentials, Locators.scope)
        client = gspread.authorize(credentials)

        sheet = client.open(Locators.userStoriesTestCases).sheet1
        max_rows = len(sheet.get_all_values())
        max_cols = len(sheet.get_all_values()[0])
        data = sheet.get_all_records()

        print(max_rows)
        print(max_cols)

    def test_01_data_driven_login(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        landingpage = LandingPage(driver)

        path = "/Users/nellynkonge/Documents/Documents – Nelly’s MacBook Pro/Nelly/QA/Data Driven Excels/loginDataTests.xlsx"
        rows = XUtils.getRowCount(path, 0)
        for r in range(2, rows + 1):
            namaste_username = XUtils.readData(path, 0, r, 1)
            namaste_password = XUtils.readData(path, 0, r, 2)
            print(namaste_username + "    ,   " + namaste_password)

            loginpage.enterEmail(namaste_username)
            time.sleep(2)
            loginpage.enterPassword(namaste_password)
            loginpage.clickLogin()
            print("isLogginSuccessful = ")
            print(landingpage.isLoginSuccessful())

            time.sleep(3)
            if landingpage.isLoginSuccessful():
                XUtils.writeData(path, 0, r, 5, "PASS")
                landingpage.signOut()
                print("Login Successful")
                time.sleep(1)

            elif not landingpage.isLoginSuccessful():
                XUtils.writeData(path, 0, r, 5, "FAIL")
                print("Login Failed")
                time.sleep(1)
