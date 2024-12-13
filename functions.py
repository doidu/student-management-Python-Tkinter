import os

def printInfo(student):
    if student is not None:
        print("="*12 , "Student's Information", "="*12, "\n")
        print(student)
        print("="*15 , "Nothing Follows", "="*15)
    else: return Exception

def findStudent(id, db):
    for student in db.allstudents:
        if student.idnum == id:
            return student
    print('Student not found.')
    return

# def inputStudentInfo(text):
#     return input(f"Enter Student's {text}: ")

inputStudentInfo = lambda text: input(f"Enter Student's {text}: ")

clr = lambda : os.system('cls')

#* GUI functions

