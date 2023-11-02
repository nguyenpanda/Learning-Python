from colorama import *
from Student import Student
from CSE import CSEStudent

student1 = Student('hà TườNg NgUyên', 2250013, 'ct22HC1', 8, True, False)
cse_student = CSEStudent("John Doe", 2212345, "MT22KH01", 3.5, True, False)

print(Back.BLACK, Style.BRIGHT, Fore.GREEN)
print(f"All class level: {[i for i in Student.__dict__]}\n")  # All class level
print(f"All instance level: {[i for i in student1.__dict__]}\n")  # All instance level
print(Style.RESET_ALL)

# # After extracting data from CSV
# Student.extract_csv('FINAL_BK.csv')

# Example usage
# print(cse_student.is_cse_class())  # Output: True

print(student1.is_k22())
print(len(Student))
