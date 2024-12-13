class StudentInfo:
    # def __init__(self):
    #     # self.name = name
    #     # self.age = age
    #     # self.idnum = idnum
    #     # self.email = email
    #     # self.phone = phone
    #     # self.allstudents = allstudents

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_idnum(self, idnum):
        self.idnum = idnum

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_idnum(self):
        return self.idnum
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nID Number: {self.idnum}\nEmail: {self.email}\nPhone: {self.phone}"
    
    # def add_student(self, name):
    #     self.allstudents.append(name)
    #     # print(f"Added student: {name.name} to the list")

    # def printAllStudent(self):
    #     print("="*10 , "All Student's Information", "="*10, "\n")
    #     for student in self.allstudents:
    #         print(student)
    #     print("="*15 , "Nothing Follows", "="*15)
