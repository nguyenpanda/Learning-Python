class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Square(Shape):
    def draw(self):
        print("Drawing Square")

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()

################################
################################
################################

from abc import ABCMeta, abstractstaticmethod

class IPerson (metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method():
        ''' Interface Method '''

class Student (IPerson):
    def __init__(self):
        self.name = "Basic Student Name"
    def person_method(self):
        print("I am a student")

class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher Name"
    
    def person_method(self):
        print("I am teacher")

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student ()
        if person_type == "Teacher":
            return Teacher()
        print ("Invalid Type")
        return -1
    
# if __name__ == '__main_':
# Sử dụng Factory Design Pattern
factory = ShapeFactory()
circle = factory.create_shape("circle")
circle.draw()  # Kết quả: "Drawing Circle"

square = factory.create_shape("square")
square.draw()  # Kết quả: "Drawing Square"

choice = input("What type of person do youwant to create? \n")
person = PersonFactory.build_person(choice)
person.person_method()