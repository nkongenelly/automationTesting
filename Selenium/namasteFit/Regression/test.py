class Test:
    def __init__(self):
        self.a = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        # self.driver = ''

    def forLoop(self):
        for self.b in self.a.values():
            print("b")
            self.driver.append(self.b)
        return self.driver


c = Test()
print(c.forLoop())
