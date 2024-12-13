from student import *

class AddStudent:
    def __init__(self, allstudents):
        # self.student_data = student
        self.database = allstudents

    def add_student(self, name, age, idnum, email, phone):
        new_stu = StudentInfo()
        new_stu.set_name(name)
        new_stu.set_age(age)
        new_stu.set_idnum(idnum)
        new_stu.set_email(email)
        new_stu.set_phone(phone)
        self.database.getAllStudent().append(new_stu)
        print(f'Added Student: {new_stu.get_name()} to the list.')

        try:
            with open('student_database.txt', 'a+') as file:
                file.write(f'{new_stu.get_name()}, {new_stu.get_age()}, {new_stu.get_idnum()}, {new_stu.get_email()}, {new_stu.get_phone()}\n')
                file.close()
        except:
            print('Error: Failed to save data to file.')

        return new_stu

    def add_student_from_database(self, database):
        try:
            with open(str(database), 'r') as file:
                lines = file.readlines()
                print(lines)
                if len(lines) == 0:
                    print('Warning: No student data found in database.')
                for line in lines:
                    name, age, idnum, email, phone = line.strip().split(', ')
                    new_stu = StudentInfo()
                    new_stu.set_name(name)
                    new_stu.set_age(age)
                    new_stu.set_idnum(idnum)
                    new_stu.set_email(email)
                    new_stu.set_phone(phone)
                    self.database.getAllStudent().append(new_stu)
                    print(f'Added Student: {new_stu.get_name()} to the list.')
        except FileNotFoundError:
            print('Error: File does not exitst.')
            
    