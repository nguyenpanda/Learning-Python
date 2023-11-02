import csv
class Test:
    def __init__(self, a):
        self.__a = a

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

class SubTest(Test):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    @property
    def b(self):
        return self.__a

    @b.setter
    def b(self, value):
        self.__b = value

testcase1 = Test(1)
testcase2 = SubTest(1, 2)





