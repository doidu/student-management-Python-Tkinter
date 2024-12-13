class StudentDatabase:
    def __init__(self):
        self.allstudents = []

    def printAllStudent(self):
        # print("="*10 , "All Student's Information", "="*10, "\n")
        for student in self.allstudents:
            print(student)
        # print("="*15 , "Nothing Follows", "="*15)
    
    def getAllStudent(self):
        return self.allstudents