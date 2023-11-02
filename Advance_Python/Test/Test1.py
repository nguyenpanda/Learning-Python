class Person:
    def __init__(self, name, age, career) -> None:
        self.__name = name
        self.__age = age
        self.__career = career
     
    def get_name(self):
         return self.__name
     
    def set_name(self, name):
         self.__name = name
     
a = Person('Nguyen', 19, 'Math')
print(a.get_name())
a.set_name('TNguyen')
print(a.get_name())
    
    