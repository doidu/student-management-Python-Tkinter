from tkinter import *
from tkinter import ttk
from functools import partial
from add_student import AddStudent
from find_student import FindStudent
from all_students import StudentDatabase
from functions import *

stu_db = StudentDatabase()
search_stu = FindStudent(stu_db)
add_stu = AddStudent(stu_db)
add_stu.add_student_from_database('student_database.txt')

class SearchFrame:
    def __init__(self, root, btn_cmd, btn_txt):
        div = Frame(root, bg="#a1a69f", pady=20, padx=10, highlightbackground="#6c9d6c", highlightcolor="#6c9d6c", highlightthickness=5)
        div.pack(ipadx=5, anchor=CENTER, expand=TRUE)

        Label(div, text="Student ID:", font=("Comic Sans MS", 18), fg="#e5e9e2", bg="#a1a69f").pack(side=TOP, anchor=NW, pady=5, padx=10, expand=TRUE)
        self.txtbox = Entry(div, font=("Comic Sans MS", 18), fg="#e5e9e2", bg="#666b63")
        self.txtbox.pack(side=TOP, anchor=NW, pady=5, padx=10, expand=TRUE, ipady=5, ipadx=5)
        Button(div, text=f"{btn_txt}", font=("Comic Sans MS", 18), fg="#e5e9e2", bg="#a1a69f", command=btn_cmd, activebackground="#848882").pack(side=LEFT, anchor=NW, pady=5, padx=10, ipadx=3)
        self.error_label = Label(div, text="No Student Found", font=("Comic Sans MS", 16), fg="#be0000", bg="#a1a69f")

def create_student_info_grid(student, root, display_txt):
    arr = ["Name: ", student.get_name(), "Age: ", student.get_age(), "ID No: ", student.get_idnum(), "Email: ", student.get_email(), "Phone No: ", student.get_phone()]
    rownum = colnum = 0
    Label(root, text=f"{display_txt}", font=("Comic Sans MS", 16), bg="#a1a69f", justify=CENTER, underline=0).grid(sticky=N, row=rownum, column=colnum, columnspan=2, padx=5)
    for txt in arr:
        Label(root, text=txt, font=("Comic Sans MS", 16), fg="black", bg="#a1a69f").grid(sticky=W, row=rownum+1, column=colnum, padx=5)
        colnum += 1
        if colnum == 2:
            colnum = 0
            rownum += 1

# *** WIN WINDOW

win = Tk()
win.title("Student Management System")
win_width = 1280
win_height = 720
win.geometry(f"{win_width}x{win_height}+{(win.winfo_screenwidth() - win_width) // 2}+{(win.winfo_screenheight() - win_height) // 2}")

# *** BTN CMDS

def del_children(widget):
    for child in widget.winfo_children():
        child.destroy()

def forget_children(widget):
    for child in widget.winfo_children():
        child.forget()

def login():
    global user
    # user = findStudent(login_div.txtbox.get(), stu_db)
    user = search_stu.searchStudent(login_div.txtbox.get())
    if user:
        login_frame.forget()
        login_div.error_label.forget()
        login_div.txtbox.delete(0, END)
        main_frame.pack(fill=BOTH, expand=TRUE)
        welcome_label.config(text=f"Welcome {user.get_name()}!")
        welcome_label.pack(anchor=CENTER, expand=TRUE)
    else: login_div.error_label.pack(side=LEFT, pady=10, expand=TRUE)

def menubtn_view_my_info():
    forget_children(content_frame)
    del_children(display_frame)
    display_frame.pack(anchor=CENTER, expand=TRUE)
    create_student_info_grid(user, display_frame, "My Information")

def menubtn_view_student_info():
    def show_student():
        student = search_stu.searchStudent(search_student_div.txtbox.get())
        # student = findStudent(search_student_div.txtbox.get(), stu_db)
        if student:
            del_children(display_frame)        
            create_student_info_grid(student, display_frame, "Student Information")
            Button(display_frame, text="Search Again?", font=("Comic Sans MS", 16), fg="#e5e9e2", bg="#a1a69f", activebackground="#848882", relief=RAISED, command=partial(menubtn_view_student_info)).grid(row=7, column=0, columnspan=2, pady=15)
        else: search_student_div.error_label.pack(side=LEFT, pady=10, expand=TRUE)
    
    forget_children(content_frame)
    del_children(display_frame)
    display_frame.pack(anchor=CENTER, expand=TRUE)

    search_student_div = SearchFrame(display_frame, show_student, "Find")

def menubtn_add_student():
    def add_to_database():
        errs = ["Name is required", "Age is required", "ID No is required", "Email is required", "Phone No is required"]
        for i, txt in enumerate(stu_info):
            if not txt.get():
                stu_info_error[i].config(text=errs[i])
                continue
            stu_info_error[i].config(text="")
        check_error = [e for e in stu_info if not e.get()]
        if not check_error:
            new = add_stu.add_student(stu_info[0].get(), stu_info[1].get(), stu_info[2].get(), stu_info[3].get(), stu_info[4].get())
            del_children(display_frame)
            create_student_info_grid(new, display_frame, f"Student Added To Database")
            Button(display_frame, text="Add Another Student?", font=("Comic Sans MS", 16), fg="#e5e9e2", bg="#a1a69f", activebackground="#848882", relief=RAISED, command=menubtn_add_student).grid(row=7, column=0, columnspan=2, pady=15)

    forget_children(content_frame)
    del_children(display_frame)
    display_frame.pack(anchor=CENTER, expand=TRUE)
    stu_info = []
    stu_info_error = []
    rownum = colnum = 0
    Label(display_frame, text=f"Adding New Student", font=("Comic Sans MS", 16), fg="#e5e9e2", bg="#a1a69f", justify=CENTER).grid(row=rownum, column=colnum, columnspan=2, padx=5)
    for txt in head:
        Label(display_frame, text=f"{txt}:", font=("Comic Sans MS", 16), fg="#e5e9e2", bg="#a1a69f", justify=LEFT).grid(sticky=W, row=rownum+1, column=colnum, padx=5)
        add_student_error_label = Label(display_frame, text="", font=("Comic Sans MS", 11), fg="#be0000", bg="#a1a69f", justify=RIGHT)
        add_student_error_label.grid(sticky=E, row=rownum+1, column=colnum+1, padx=5)
        stu_info_error.append(add_student_error_label)
        rownum += 1
        txtbox = Entry(display_frame, font=("Comic Sans MS", 16), fg="#e5e9e2", bg="#666b63")
        txtbox.grid(row=rownum+1, column=0, columnspan=2, padx=5, pady=5)
        rownum +=1
        stu_info.append(txtbox)
    Button(display_frame, text="Add Student", font=("Comic Sans MS", 16), relief=RAISED, fg="#e5e9e2", bg="#a1a69f", activebackground="#848882", command=add_to_database).grid(row=rownum+2, column=colnum, columnspan=2, pady=10)

def menubtn_view_all_student():
    forget_children(content_frame)
    tree.delete(*tree.get_children())
    display_frame_allstudents.pack(fill=BOTH, anchor=CENTER, expand=TRUE)
    tree.pack(side=LEFT, fill=BOTH, expand=True)
    scroll.pack(side=RIGHT, fill=Y, anchor=E)
    for txt in head:
        tree.heading(txt, text=txt)
        tree.column(txt, width=75, minwidth=25, anchor=CENTER)
        if txt == "Email": tree.column(txt, width=200, anchor=CENTER)
    for student in stu_db.getAllStudent():
        tree.insert("", END, values=(student.get_name(), student.get_age(), student.get_idnum(), student.get_email(), student.get_phone()))
    tree.config(yscrollcommand=scroll.set)

def menubtn_logout():
    main_frame.forget()
    forget_children(content_frame)
    del_children(display_frame)
    login_frame.pack(fill=BOTH, expand=True)

# *** LOGIN FRAME CONTENT

login_frame = Frame(win, bg="#929892")
login_frame.pack(fill=BOTH, expand=TRUE)
Label(login_frame, text="Student Management System", font=("Comic Sans MS", 24), fg="#e5e9e2", bg="#929892", justify=CENTER).pack(fill=X, pady=15)
login_div = SearchFrame(login_frame, login, "Log-In")
Button(login_frame, text="Exit", font=("Comic Sans MS", 16), fg="#e5e9e2", bg="#ad0000", activebackground="#970000", relief=RAISED, command=exit).pack(anchor=SE, padx=10, pady=10, ipadx=10)

# *** MAIN FRAME

main_frame = Frame(win)

# *** MENU FRAME CONTENT

menu_frame = Frame(main_frame, bg="black")
menu_frame.pack(side=LEFT, fill=Y)

Label(menu_frame, text="Main Menu", fg="Black", relief=SUNKEN, bg="#84938A", font=("Comic Sans MS", 24), padx=30).pack(fill=X, padx=5, pady=5)
menu_txtcmd = {"View my info":menubtn_view_my_info, "View other student's info":menubtn_view_student_info, "Add new student":menubtn_add_student, "View all students info":menubtn_view_all_student, "Log out":menubtn_logout}

for key, value in menu_txtcmd.items():
    btn = Button(menu_frame, text=key, font=("Comic Sans MS", 16), relief=RAISED, command=value, bg="#84938A", activebackground="#B1BAA6")
    btn.pack(fill=BOTH, padx=5, pady=5, expand=True)
    if key == "Log out": btn.config(fg="#be0000")

# *** CONTENT FRAME CONTENT

head = ("Name", "Age", "ID No", "Email", "Phone No")

content_frame = Frame(main_frame, bg="#929892", relief=SOLID)
content_frame.pack(side=LEFT, fill=BOTH, expand=TRUE)

display_frame = Frame(content_frame, bg="#a1a69f", relief=SUNKEN, borderwidth=5, padx=100, pady=75)

welcome_label = Label(content_frame, text="Welcome!", fg="Black", relief=RIDGE, bg="#a1a69f", borderwidth=5, font=("Comic Sans MS", 32), padx=30, pady=5)

display_frame_allstudents = Frame(content_frame, bg="#929892", relief=FLAT, borderwidth=7, padx=30, pady=40)

style = ttk.Style()
style.theme_use("alt")
style.configure("Treeview.Heading", font=("Comic Sans MS", 10), background="#6c9d6c")
style.configure("Treeview", font=("Comic Sans MS", 10), background="#a1a69f", rowheight=40)
tree = ttk.Treeview(display_frame_allstudents, columns=head, show='headings')
scroll = Scrollbar(display_frame_allstudents, orient=VERTICAL, command=tree.yview)


win.mainloop()