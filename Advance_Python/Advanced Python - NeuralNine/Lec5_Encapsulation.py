class Person:
    def __init__(self, name: str, age: int, career: str) -> None:
        self.__name = name
        self.__age = age
        self.__career = career
    
    # Getter method for the 'Name' property.
    # This method allows accessing the private '__name' attribute when 'Name' property is called,
    # providing read-only access.
    # Usage: instance_name = object_instance.Name
    @property  # READ ONLY, clear code (without this '()' bracket)
    def Name(self):
        return self.__name
    
    # Setter method for the 'Name' property.
    # This method allows setting the value of the private '__name' attribute
    # when 'Name' property is assigned a new value.
    # Usage: object_instance.Name = new_name
    @Name.setter  # Use this decorator to overwrite the method
    def Name(self, name):
        self.__name = name
    
    # Static method to print 'Hello World'.
    # This method can be called on the class itself without creating an instance of the class.
    # Usage: ClassName.printHelloWorld()
    @staticmethod
    def printHelloWorld():
        print('Hello world')
    
    '''
    Missing @Classmethod, @Name.deleter, ...
    '''


nguyen = Person('Nguyen', 19, 'Computer Science')

print(nguyen.Name)
nguyen.set_name = 'Tuong Nguyen Ha'
print(nguyen.Name)

# Person.printHelloWorld()
