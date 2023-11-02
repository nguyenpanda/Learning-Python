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

    def is_k22(self):
        return str(self.__student_id).startswith('22')  # Check if student ID starts with 'CC'

    def is_cc_class(self):
        return self.__student_class.startswith('CC')  # Check if student class starts with 'CC'

    @classmethod
    def count_total_students(cls):
        return cls.index_counter  # Return the total number of students

    @classmethod
    def count_bk_fc(cls):
        count = sum(student.is_bk_fc for student in cls.all_students)  # Count students with BK FC participation
        return count

    @classmethod
    def count_oisp_camp(cls):
        count = sum(student.is_oisp_camp for student in cls.all_students)  # Count students with OISP Camp participation
        return count

    @classmethod
    def extract_csv(cls, csv_name_file: str):
        with open(csv_name_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)  # Read CSV data as dictionaries
            students = list(reader)

        for student in students:
            full_name = student.get('Full name', 'N/A')
            student_id = int(student.get('ID', 'N/A'))
            student_class = student.get('Class', 'N/A')
            sed = float(student.get('SED', 'N/A'))
            is_bk_fc = True if str(student.get('BK FC')) == '1' else False
            is_oisp_camp = True if str(student.get('OISP Camp')) == '1' else False

            Student(full_name=full_name, student_id=student_id, student_class=student_class,
                    sed=sed, is_bk_fc=is_bk_fc, is_oisp_camp=is_oisp_camp)

    def __str__(self):  # Display student information
        return f'{self.full_name} - {self.student_id}'

    def __repr__(self):  # Represent student instance as a string
        return (f'{self.__class__.__name__}("{self.full_name}", {self.student_id}, "{self.student_class}", {self.sed}, '
                f'{self.is_bk_fc}, {self.is_oisp_camp})')
