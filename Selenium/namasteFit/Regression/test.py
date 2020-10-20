class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value

    def add(self, key, value):
        self[key] = value

drivers = my_dictionary()
drivers['chrome'] = "chrome_driver"
drivers['chromeMobile'] = "chrome_mobile_driver"
drivers['firefox'] = "firefox_driver"
drivers['edge'] = "edge_driver"

for driverOptions in drivers:
    # time.sleep(10)
    # print("again")
    # print(driverOptions)
    print(drivers[driverOptions])
    # print(drivers[])

end = 0.1200015
start = 0.0200015
result ="success"
message = "browser status message for this account is : " + result + " \n And login in time is :" + str(end - start) + " seconds"
print(message)