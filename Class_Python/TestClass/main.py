import csv

class Student:
    allStudents = []
    index = 1
    totalStudents = 0
    
    def __init__(self, name: str, studentID: int, major: str):
        assert len(name) > 1, f'name must contain at least 2 letters, got {len(name)}'
        assert len(str(studentID)) == 7, f'studentID must contain 7 digits, got {len(str(studentID))} digit(s)'
        assert len(major), f'major must contain at least 2 letters, got {len(major)} letter(s)'
        
        self.__name = name.title()
        self.__studentID = studentID
        self.__major = major.upper()
        
        self.__index = Student.index
        Student.index += 1
        
        Student.totalStudents += 1
        Student.allStudents.append(self)
    
    def getIndex(self):
        return self.__index
    
    @property
    def getName(self):
        return self.__name
    
    def getStudentID(self):
        return self.__studentID
    
    def getMajor(self):
        return self.__major
    
    def isK22(self):
        return str(self.__studentID).startswith('22')
    
    def isK23(self):
        return str(self.__studentID).startswith('23')
    
    def academicYear(self):
        return int(str(self.__studentID)[0:2])
    
    def __str__(self):
        return f'{self.__name} - {self.__studentID} - {self.__major}'
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', '{self.__studentID}', '{self.__major}')"
    
    @classmethod
    def totalStudent(cls):
        return cls.totalStudents
    
    @classmethod
    def instantiate_from_csv(cls, file):  # cls stand for class
        with open(file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            students = list(reader)
        
        for item in students:
            Student(
                name=str(item.get('name')),
                studentID=int(item.get('id')),
                major=str(item.get('major')),
            )

Student.instantiate_from_csv('DataSet.csv')
print(Student.totalStudents)

# student1 = Student('tuong nguyen', 225001, 'CS1')
# student2 = Student('ha tuong nguyen', 225002, 'CS2')
# student3 = Student('Nguyen', 225003, 'CS3')
# student4 = Student('Nguyen', 225004, 'CS4')
# student5 = Student('Nguyen', 225005, 'CS5')
# student6 = Student('Nana nap ma', 235005, 'CHE')

# print(student1)
# print(student2)
# print(student4)
# print(student5)
# print(student6.academicYear())

# print(Student.totalStudents)
