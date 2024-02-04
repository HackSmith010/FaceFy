from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
import cv2
import threading


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # # =======================Variables===============
        self.var_Dep = StringVar()
        self.var_Course = StringVar()
        self.var_Year = StringVar()
        self.var_Sem = StringVar()
        self.var_Std_id = StringVar()
        self.var_Std_name = StringVar()
        self.var_RollNo = StringVar()
        self.var_Gender = StringVar()
        self.var_DOB = StringVar()
        self.var_email = StringVar()
        self.var_Phone = StringVar()
        self.var_Address = StringVar()
        self.var_Teacher_names = StringVar()

        # text_label

        t_lbl = Label(
            self.root,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="green",
        )
        t_lbl.place(x=0, y=0, width=1366, height=45)

        # bg_image
        img1 = Image.open("Images/bgImg1.jpeg")
        img1 = img1.resize((1366, 723))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_lbl = Label(self.root, image=self.photoimg1)
        bg_lbl.place(x=0, y=45, width=1366, height=768)

        # main frame
        main_frame = Frame(bg_lbl, bd=2)
        main_frame.place(x=18, y=17, width=1331, height=670)

        # left label frame
        detail_frame = LabelFrame(
            main_frame,
            bd=7,
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 20, "bold"),
            highlightbackground="cyan",
        )
        detail_frame.place(x=10, y=15, width=650, height=640)

        # current_course_1
        sub_detail_frame1 = LabelFrame(
            detail_frame,
            bd=4,
            relief=RIDGE,
            text="Current Course Information",
            font=("times new roman", 15, "bold"),
        )
        sub_detail_frame1.place(x=10, y=5, width=600, height=150)

        # department label
        dep_lbl = Label(
            sub_detail_frame1,
            text="Department",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        dep_lbl.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(
            sub_detail_frame1,
            textvariable=self.var_Dep,
            font=("times new roman", 12, "bold"),
            width=20,
            state="readonly",
        )
        dep_combo["values"] = (
            "Select Department",
            "Computer",
            "Mechanical",
            "AIML",
            "EXTC",
            "Electrical",
            "Civil",
        )
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course label
        course_lbl = Label(
            sub_detail_frame1,
            text="Course",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        course_lbl.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(
            sub_detail_frame1,
            textvariable=self.var_Course,
            font=("times new roman", 12, "bold"),
            width=20,
            state="readonly",
        )
        course_combo["values"] = ("Select course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year label

        year_lbl = Label(
            sub_detail_frame1,
            text="Year",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        year_lbl.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(
            sub_detail_frame1,
            textvariable=self.var_Year,
            font=("times new roman", 12, "bold"),
            width=20,
            state="readonly",
        )
        year_combo["values"] = (
            "Select Year",
            "2020-21",
            "2021-22",
            "2022-23",
            "2023-24",
        )
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester label
        sem_lbl = Label(
            sub_detail_frame1,
            text="Semester",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        sem_lbl.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(
            sub_detail_frame1,
            textvariable=self.var_Sem,
            font=("times new roman", 12, "bold"),
            width=20,
            state="readonly",
        )
        sem_combo["values"] = ("Select Semester", "Sem I", "Sem II")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # #student_details
        sub_detail_frame2 = LabelFrame(
            detail_frame,
            bd=4,
            relief=RIDGE,
            text="Student Information",
            font=("times new roman", 15, "bold"),
        )
        sub_detail_frame2.place(x=10, y=170, width=600, height=400)

        # student_id
        l1_lbl = Label(
            sub_detail_frame2,
            text="Student Id :",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        l1_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        l1_entry = ttk.Entry(
            sub_detail_frame2,
            textvariable=self.var_Std_id,
            width=18,
            font=("times new roman", 12, "bold"),
        )
        l1_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # student_name
        l2_lbl = Label(
            sub_detail_frame2,
            text="Student Name:",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        l2_lbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        l2_entry = ttk.Entry(
            sub_detail_frame2,
            textvariable=self.var_Std_name,
            width=18,
            font=("times new roman", 12, "bold"),
        )
        l2_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Roll no
        l3_lbl = Label(
            sub_detail_frame2,
            text="Roll No :",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        l3_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        l3_entry = ttk.Entry(
            sub_detail_frame2,
            textvariable=self.var_RollNo,
            width=18,
            font=("times new roman", 12, "bold"),
        )
        l3_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Gender
        l4_lbl = Label(
            sub_detail_frame2,
            text="Gender:",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        l4_lbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        l4_combo = ttk.Combobox(
            sub_detail_frame2,
            textvariable=self.var_Gender,
            font=("times new roman", 12, "bold"),
            width=16,
            state="readonly",
        )
        l4_combo["values"] = (
            "Select Gender",
            "Male",
            "Female",
            "Others",
        )
        l4_combo.current(0)
        l4_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # DOB
        l5_lbl = Label(
            sub_detail_frame2,
            text="DOB :",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        l5_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        l5_entry = DateEntry(
            sub_detail_frame2,
            textvariable=self.var_DOB,
            width=18,
            background="darkblue",
            foreground="white",
            borderwidth=2,
            date_pattern="dd/mm/yyyy",
        )
        l5_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Email
        l6_lbl = Label(
            sub_detail_frame2,
            text="Email:",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        l6_lbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        l6_entry = ttk.Entry(
            sub_detail_frame2,
            textvariable=self.var_email,
            width=18,
            font=("times new roman", 12, "bold"),
        )
        l6_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Phone no
        l7_lbl = Label(
            sub_detail_frame2,
            text="Phone No :",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        l7_lbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        l7_entry = ttk.Entry(
            sub_detail_frame2,
            textvariable=self.var_Phone,
            width=18,
            font=("times new roman", 12, "bold"),
        )
        l7_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Address
        l8_lbl = Label(
            sub_detail_frame2,
            text="Address:",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        l8_lbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        l8_entry = ttk.Entry(
            sub_detail_frame2,
            textvariable=self.var_Address,
            width=18,
            font=("times new roman", 12, "bold"),
        )
        l8_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Teacher_Name
        l9_lbl = Label(
            sub_detail_frame2,
            text="Teacher Name :",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        l9_lbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        l9_entry = ttk.Entry(
            sub_detail_frame2,
            textvariable=self.var_Teacher_names,
            width=18,
            font=("times new roman", 12, "bold"),
        )
        l9_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Radio Buttons

        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            sub_detail_frame2,
            variable=self.var_radio1,
            text="Take Photo Sample",
            value="Yes",
        )
        radiobtn1.grid(row=5, column=0, pady=25)

        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(
            sub_detail_frame2,
            variable=self.var_radio1,
            text="No Photo Sample",
            value="No",
        )
        radiobtn2.grid(row=5, column=1)

        # button Frame
        btn_frame = Frame(sub_detail_frame2, relief=RIDGE, bd=2, bg="White")
        btn_frame.place(x=5, y=250, width=580, height=40)

        save_btn = Button(
            btn_frame,
            command=self.addData,
            text="Save",
            width=15,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        save_btn.grid(row=0, column=0)

        update_btn = Button(
            btn_frame,
            command=self.updateData,
            text="Update",
            width=15,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        update_btn.grid(row=0, column=1)

        delete_btn = Button(
            btn_frame,
            command=self.deleteData,
            text="Delete",
            width=15,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(
            btn_frame,
            command=self.resetData,
            text="Reset",
            width=15,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        reset_btn.grid(row=0, column=3, pady=2)

        btn_frame1 = Frame(sub_detail_frame2, relief=RIDGE, bd=2, bg="White")
        btn_frame1.place(x=5, y=300, width=580, height=40)

        take_pho_btn = Button(
            btn_frame1,
            command=self.generateDs,
            text="Take Photo Sample",
            width=30,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        take_pho_btn.grid(row=1, column=0)

        update_pho_btn = Button(
            btn_frame1,
            text="Update Photo Sample",
            width=30,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        update_pho_btn.grid(row=1, column=1, padx=16, pady=2)

        # right label frame
        right_frame = LabelFrame(
            main_frame,
            bd=7,
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 20, "bold"),
        )
        right_frame.place(x=670, y=15, width=650, height=640)

        # Search System
        search_frame = LabelFrame(
            right_frame,
            bd=4,
            relief=RIDGE,
            text="Search System",
            font=("times new roman", 15, "bold"),
        )
        search_frame.place(x=10, y=5, width=610, height=120)

        search_lbl = Label(
            search_frame,
            text="Search By : ",
            font=("times new roman", 15, "bold"),
            bg="grey",
            fg="white",
        )
        search_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(
            search_frame,
            font=("times new roman", 12, "bold"),
            width=15,
            state="readonly",
        )
        search_combo["values"] = ("Select ", "Roll No", "Student Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(
            search_frame, width=15, font=("times new roman", 12, "bold")
        )
        search_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        search_btn = Button(
            search_frame,
            text="Search",
            width=15,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        search_btn.grid(row=0, column=2, padx=20)

        showAll_btn = Button(
            search_frame,
            text="Show All",
            width=15,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        showAll_btn.grid(row=1, column=2)

        # ==================Table Frame=============================
        table_frame = LabelFrame(
            right_frame,
            bd=4,
            relief=RIDGE,
            font=("times new roman", 15, "bold"),
        )
        table_frame.place(x=10, y=130, width=610, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=(
                "Dep",
                "Course",
                "Year",
                "Sem",
                "ID",
                "Name",
                "RollNo",
                "Gender",
                "DOB",
                "Email",
                "PhoneNo",
                "Address",
                "Teacher",
                "Photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("ID", text="Student Id")
        self.student_table.heading("Name", text="Student Name")
        self.student_table.heading("RollNo", text="Roll No")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("PhoneNo", text="Phone No")
        self.student_table.heading("Teacher", text="Teacher Name")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("Dep", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("RollNo", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("PhoneNo", width=100)
        self.student_table.column("Photo", width=120)
        self.student_table.column("Teacher", width=120)
        self.student_table.column("Address", width=120)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # =====================Functions Declaration=====================

    def addData(self):
        if (
            self.var_Dep.get() == "Select Department"
            or self.var_Std_name.get() == ""
            or self.var_Std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="anshu2004",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_Dep.get(),
                        self.var_Course.get(),
                        self.var_Year.get(),
                        self.var_Sem.get(),
                        self.var_Std_id.get(),
                        self.var_Std_name.get(),
                        self.var_RollNo.get(),
                        self.var_Gender.get(),
                        self.var_DOB.get(),
                        self.var_email.get(),
                        self.var_Phone.get(),
                        self.var_Address.get(),
                        self.var_Teacher_names.get(),
                        self.var_radio1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success",
                    "Student details has been added Successfully",
                    parent=self.root,
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # ============================fetch data==============
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="anshu2004",
            database="face_recognizer",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # =================================get cursor==================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        # Check if data has enough elements
        if len(data) >= 14:
            self.var_Dep.set(data[0])
            self.var_Course.set(data[1])
            self.var_Year.set(data[2])
            self.var_Sem.set(data[3])
            self.var_Std_id.set(data[4])
            self.var_Std_name.set(data[5])
            self.var_RollNo.set(data[6])
            self.var_Gender.set(data[7])
            self.var_DOB.set(data[8])
            self.var_email.set(data[9])
            self.var_Phone.set(data[10])
            self.var_Address.set(data[11])
            self.var_Teacher_names.set(data[12])
            self.var_radio1.set(data[13])
        else:
            pass

    # ================update function===============
    def updateData(self):
        if (
            self.var_Dep.get() == "Select Department"
            or self.var_Std_name.get() == ""
            or self.var_Std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update",
                    "Do you want to update this student's data",
                    parent=self.root,
                )
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="anshu2004",
                        database="face_recognizer",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Student_name=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,Teacher=%s,PhotoSampleStatus=%s where Student_Id=%s",
                        (
                            self.var_Dep.get(),
                            self.var_Course.get(),
                            self.var_Year.get(),
                            self.var_Sem.get(),
                            self.var_Std_name.get(),
                            self.var_RollNo.get(),
                            self.var_Gender.get(),
                            self.var_DOB.get(),
                            self.var_email.get(),
                            self.var_Phone.get(),
                            self.var_Address.get(),
                            self.var_Teacher_names.get(),
                            self.var_radio1.get(),
                            self.var_Std_id.get(),
                        ),
                    )
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success",
                    "Student details successfully Updated..",
                    parent=self.root,
                )
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ==========================delete function===========

    def deleteData(self):
        if self.var_Std_id.get() == "":
            messagebox.showerror(
                "Error", "Student ID must be required", parent=self.root
            )
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page",
                    "Do you want to Delete this Student",
                    parent=self.root,
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="anshu2004",
                        database="face_recognizer",
                    )
                    my_cursor = conn.cursor()
                    sql = "Delete from student where Student_Id=%s"
                    val = (self.var_Std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo(
                    "Delete", "Successfully deleted student details", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # =======================reset function=============

    def resetData(self):
        self.var_Dep.set("Select Department")
        self.var_Course.set("Select Course")
        self.var_Year.set("Select Year")
        self.var_Sem.set("Select Semester")
        self.var_Std_id.set("")
        self.var_Std_name.set("")
        self.var_RollNo.set("")
        self.var_Gender.set("Select Gender")
        self.var_DOB.set("")
        self.var_email.set("")
        self.var_Phone.set("")
        self.var_Address.set("")
        self.var_Teacher_names.set("")
        self.var_radio1.set("")

    # =================generate DataSet or Take Photo sample======
    def generateDs(self):
        if (
            self.var_Dep.get() == "Select Department"
            or self.var_Std_name.get() == ""
            or self.var_Std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="anshu2004",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id += 1
                my_cursor.execute(
                    "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Student_name=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,Teacher=%s,PhotoSampleStatus=%s where Student_Id=%s",
                    (
                        self.var_Dep.get(),
                        self.var_Course.get(),
                        self.var_Year.get(),
                        self.var_Sem.get(),
                        self.var_Std_name.get(),
                        self.var_RollNo.get(),
                        self.var_Gender.get(),
                        self.var_DOB.get(),
                        self.var_email.get(),
                        self.var_Phone.get(),
                        self.var_Address.get(),
                        self.var_Teacher_names.get(),
                        self.var_radio1.get(),
                        self.var_Std_id.get()+"1",
                    ),
                )
                conn.commit()
                self.fetch_data()
                self.resetData()
                conn.close()

                # =======================Load predefine data  from Open cv=============

                faceClassifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml"
                )

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = faceClassifier.detectMultiScale(gray, 1.3, 5)

                    for x, y, w, h in faces:
                        face_cropped = img[y : y + h, x : x + w]
                        return face_cropped

                def capture_images():
                    cap = cv2.VideoCapture(2)
                    img_id = 0

                    while True:
                        ret, img_frame = cap.read()

                        cropped_face = face_cropped(img_frame)

                        if cropped_face is not None:
                            img_id += 1
                            face_resized = cv2.resize(cropped_face, (450, 450))
                            face_grayscale = cv2.cvtColor(
                                face_resized, cv2.COLOR_BGR2GRAY
                            )
                            file_path = (
                                "data/user."+str(id)+"."+str(img_id)+".jpg"
                            )
                            cv2.imwrite(file_path, face_grayscale)
                            cv2.putText(
                                face_resized,
                                str(img_id),
                                (50, 50),
                                cv2.FONT_HERSHEY_COMPLEX,
                                2,
                                (0, 255, 0),
                                2,
                            )
                            cv2.imshow("Cropped Face", face_resized)

                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("RESULT", "Data Set Generated Successfully")

                capture_thread = threading.Thread(target=capture_images)
                capture_thread.start()

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
