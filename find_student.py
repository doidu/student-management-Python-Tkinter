from student import *

class FindStudent:
    def __init__(self, allstudents):
        self.database = allstudents
        
    def searchStudent(self, id):
        for student in self.database.allstudents:
            if student.get_idnum() == id:
                return student
        print('Student not found.')
        return