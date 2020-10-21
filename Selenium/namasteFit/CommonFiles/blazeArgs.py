class BlazeArgs():
    def blazemeterArgsStart(self, driver, testSuiteName, testCaseName):
        # fill search filed
        self.driver = driver
        self.args = {'testSuiteName': testSuiteName, 'testCaseName': testCaseName, }
        self.driver.execute_script("/* FLOW_MARKER test-case-start */", self.args)

    def addArgs(self, status, message):
        self.args = {
            'status': status,
            'message': message,
        }

    def blazemeterArgsStop(self):
        self.driver.execute_script("/* FLOW_MARKER test-case-stop */", self.args)