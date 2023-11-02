# student_id = 2150013
# student_class = 'CC22KHM1'
# student_name = 'hà TườNg NguYên'

import csv
# class AutoAttrs:
#     def __init__(self):
#         self.values = []
#
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value
#         if hasattr(instance, 'values'):
#             instance.values.append(self.name)

import csv

class Student:
    # Class-level attributes
    all_students = []  # List to store all student instances
    index_counter = 0  # Counter to keep track of student index

    def __init__(self, full_name: str, student_id: int, student_class: str,
                 sed: float, is_bk_fc: bool, is_oisp_camp: bool):
        # Validate inputs
        assert len(full_name) >= 5, f'Length of full name must be greater than 5, received {full_name}'
        assert student_id >= 1600000, f'{student_id} must be greater than 1600000'
        assert sed >= 0, f'{sed} must be greater than 0'

        # Assign attributes
        self.__full_name = full_name.title()
        self.__student_id = student_id
        self.__student_class = student_class.replace(" ", "").upper()
        self.__sed = sed
        self.__is_bk_fc = is_bk_fc  # Flag indicating BK FC participation
        self.__is_oisp_camp = is_oisp_camp  # Flag indicating OISP Camp participation
        self.index = Student.index_counter

        # Update class-level attributes
        Student.all_students.append(self)
        Student.index_counter += 1

    @property
    def full_name(self):
        return self.__full_name

    @property
    def student_id(self):
        return self.__student_id

    @property
    def student_class(self):
        return self.__student_class

    @property
    def sed(self):
        return self.__sed

    @property
    def is_bk_fc(self):
        return self.__is_bk_fc

    @property
    def is_oisp_camp(self):
        return self.__is_oisp_camp


student1 = Student()
