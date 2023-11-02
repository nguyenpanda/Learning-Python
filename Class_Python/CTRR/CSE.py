from Student import Student
import csv

class CSEStudent(Student):
    def __init__(self, full_name: str, student_id: int, student_class: str,
                 sed: float, is_bk_fc: bool, is_oisp_camp: bool):
        super().__init__(full_name, student_id, student_class, sed, is_bk_fc, is_oisp_camp)

    # def is_cse_class(self):
    #     return self.student_class.startswith("MT") or "KHM" in self.student_class or "KTM" in self.student_class

    @classmethod
    def extract_csv(cls, csv_name_file: str):
        with open(csv_name_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            cse_students = []

            for student in reader:
                full_name = student.get('Full name', 'N/A').title()
                student_id = int(student.get('ID', 'N/A'))
                student_class = student.get('Class', 'N/A').upper()
                sed = float(student.get('SED', 'N/A'))
                is_bk_fc = True if student.get('BK FC', '0') == '1' else False
                is_oisp_camp = True if student.get('OISP Camp', '0') == '1' else False

                if cls.is_cse_class(student_class):  # Using the method defined in the class
                    cse_student = cls(full_name, student_id, student_class, sed, is_bk_fc, is_oisp_camp)
                    cse_students.append(cse_student)
                else:
                    student_instance = Student(full_name, student_id, student_class, sed, is_bk_fc, is_oisp_camp)
                    cse_students.append(student_instance)

            cls.all_students.extend(cse_students)

    @classmethod
    def is_cse_class(cls, student_class):
        pass
