import sys
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from namasteFit.TestServer.Locators.locators import Locators

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


def getRowCount(file, client):
    sheet = client.open(file).sheet1
    return len(sheet.get_all_values())


def getColumnCount(file, client):
    sheet = client.open(file).sheet1
    return len(sheet.get_all_values()[0])


def readData(file, client, rowno, columno):
    sheet = client.open(file).sheet1
    return sheet.cell(rowno, columno).value


def writeData(file, client, rowno, columno, data):
    sheet = client.open(file).sheet1
    sheet.update_cell(rowno, columno, data)


def appendData(file, client, data):
    sheet = client.open(file).sheet1
    sheet.append_row(data)


def write_results(TestResults, browser, user_story):
    written = False
    print("3")
    print(TestResults)
    print(user_story)
    credentials = ServiceAccountCredentials.from_json_keyfile_name(Locators.credentials, Locators.scope)
    client = gspread.authorize(credentials)
    max_rows = getRowCount(Locators.userStoriesTestCases, client)
    print(max_rows)
    print(browser)
    print(browser == Locators.firefox_driver)

    if browser == Locators.firefox_driver:
        column = 3
        new_row = [user_story, "", TestResults, "", "", ""]
        addUnderBrowserTitle(max_rows, client, column, new_row, TestResults, user_story)

    elif browser == Locators.chrome_driver:
        column = 4
        new_row = [user_story, "", "", TestResults, "", ""]
        addUnderBrowserTitle(max_rows, client, column, new_row, TestResults, user_story)

    elif browser == Locators.microsoft_edge_driver:
        column = 5
        new_row = [user_story, "", "", "", TestResults, ""]
        addUnderBrowserTitle(max_rows, client, column, new_row, TestResults, user_story)


def addUnderBrowserTitle(max_rows, client, col, new_row, TestResults, user_story):
    written = False
    count = 0
    print("addUnderBrowserTitle")
    for row in range(max_rows + 1):
        print("row = ")
        print(row)
        row_value = readData(Locators.userStoriesTestCases, client, row + 1, 1)
        print("row_value")
        print(row_value)
        print("user story = ")
        print(user_story)
        print("compare")
        print(row_value == user_story)
        if row_value == user_story:
            writeData(Locators.userStoriesTestCases, client, row + 1, col, TestResults)
            written = True
            count += 1
            print("column")
            print(col)


    if count == max_rows and written is False:
        appendData(Locators.userStoriesTestCases, client, new_row)
