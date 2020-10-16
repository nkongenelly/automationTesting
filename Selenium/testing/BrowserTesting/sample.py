from namasteFit.TestServer.Locators.locators import Locators
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import namasteFit.CommonFiles.googleSheetsUtils as sheetsUtils




def write_results(TestResults):
    written = False
    print("3")
    print(TestResults)
    credentials = ServiceAccountCredentials.from_json_keyfile_name(Locators.credentials, Locators.scope)
    client = gspread.authorize(credentials)
    max_rows = sheetsUtils.getRowCount(Locators.userStoriesTestCases, client)

    print(max_rows)
    for row in range(max_rows + 1):
        print(row)
        row_value = sheetsUtils.readData(Locators.userStoriesTestCases, client, row + 1, 1)
        if row_value == "107":
            sheetsUtils.writeData(Locators.userStoriesTestCases, client, row + 1, 2, TestResults)
            written = True

    if written == False:
        new_row = ["107", TestResults, "", "", ""]
        sheetsUtils.appendData(Locators.userStoriesTestCases, client, new_row)


write_results("FAIL")
