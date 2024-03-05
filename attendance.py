from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import os
import csv
from tkinter import filedialog
import mysql.connector
import cv2
import threading

my_data = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Attendance Details")
        
# ============================Variables=================================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        t_lbl = Label(
            self.root,
            text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="Grey",
            fg="Yellow",
        )
        t_lbl.place(x=0, y=0, width=1366, height=45)

        # bg_image
        img1 = Image.open("Images/bg3.jpg")
        img1 = img1.resize((1366, 768))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_lbl = Label(self.root, image=self.photoimg1)
        bg_lbl.place(x=0, y=45, width=1366, height=768)

        # main_frame = Frame(bg_lbl, bd=2)
        # main_frame.place(x=18, y=17, width=1331, height=670)

        # left label frame
        left_frame = LabelFrame(
            self.root,
            bd=7,
            relief=RIDGE,
            text="Student Attendance Details",
            font=("times new roman", 20, "bold"),
            highlightbackground="cyan",
        )
        left_frame.place(x=10, y=65, width=663, height=660)

        inside_framel = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        inside_framel.place(x=20, y=15, width=623, height=600)

        # ===============labels and Entry===============
        lbl1 = Label(
            inside_framel,
            text="Attendance Id :",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        lbl1.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        lbl1_entry = ttk.Entry(
            inside_framel,
            textvariable=self.var_atten_id,
            width=18,
            font=("times new roman", 12, "bold"),
        )
        lbl1_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        lbl2 = Label(
            inside_framel,
            text="Roll No :",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        lbl2.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        lbl2_entry = ttk.Entry(
            inside_framel,
            textvariable=self.var_atten_roll,
            width=18,
            font=("times new roman", 12, "bold"),
        )
        lbl2_entry.grid(row=0, column=4, padx=10, pady=5, sticky=W)

        lbl3 = Label(
            inside_framel,
            text="Name:",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        lbl3.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        lbl3_entry = ttk.Entry(
            inside_framel,
            textvariable=self.var_atten_name,
            width=18,
            font=("times new roman", 12, "bold"),
        )
        lbl3_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        lbl4 = Label(
            inside_framel,
            text="Department:",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        lbl4.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        lbl4_entry = ttk.Entry(
            inside_framel,
            textvariable=self.var_atten_dep,
            width=18,
            font=("times new roman", 12, "bold"),
        )
        lbl4_entry.grid(row=1, column=4, padx=10, pady=5, sticky=W)

        lbl5 = Label(
            inside_framel,
            text="Time:",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        lbl5.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        lbl5_entry = ttk.Entry(
            inside_framel,
            textvariable=self.var_atten_time,
            width=18,
            font=("times new roman", 12, "bold"),
        )
        lbl5_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        lbl6 = Label(
            inside_framel,
            text="Date:",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        lbl6.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        lbl6_entry = ttk.Entry(
            inside_framel,
            textvariable=self.var_atten_date,
            width=18,
            font=("times new roman", 12, "bold"),
        )
        lbl6_entry.grid(row=2, column=4, padx=10, pady=5, sticky=W)

        lbl7 = Label(
            inside_framel,
            text="Attendance Status:",
            font=("times new roman", 12, "bold"),
            bg="mint cream",
        )
        lbl7.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        l7_combo = ttk.Combobox(
            inside_framel,
            textvariable=self.var_atten_attendance,
            font=("times new roman", 12, "bold"),
            width=16,
            state="readonly",
        )
        l7_combo["values"] = ("Status", "Present", "Absent")
        l7_combo.current(0)
        l7_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        btn_frame = Frame(inside_framel, relief=RIDGE, bd=2, bg="White")
        btn_frame.place(x=20, y=250, width=585, height=40)

        Import = Button(
            btn_frame,
            text="Import csv",
            command=self.import_csv,
            width=15,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        Import.grid(row=0, column=0)

        Export = Button(
            btn_frame,
            text="Export csv",
            command=self.export_csv,
            width=15,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        Export.grid(row=0, column=1)

        Update = Button(
            btn_frame,
            text="Update",
            width=15,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        Update.grid(row=0, column=2)

        reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            width=15,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        reset_btn.grid(row=0, column=3, pady=2)

        # right label frame
        right_frame = LabelFrame(
            self.root,
            bd=7,
            relief=RIDGE,
            text="Attendance Details",
            font=("times new roman", 20, "bold"),
        )
        right_frame.place(x=685, y=65, width=663, height=660)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=20, y=15, width=623, height=600)

        # ==================scrollbars=======================

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(
            table_frame,
            columns=(
                "Id",
                "RollNo",
                "Name",
                "Department",
                "Time",
                "Date",
                "Attendance",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Id", text="Attendance ID")
        self.AttendanceReportTable.heading("RollNo", text="Roll No")
        self.AttendanceReportTable.heading("Name", text="Student Name")
        self.AttendanceReportTable.heading("Department", text="Department")
        self.AttendanceReportTable.heading("Time", text="Time")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("Id", width=100)
        self.AttendanceReportTable.column("RollNo", width=100)
        self.AttendanceReportTable.column("Name", width=100)
        self.AttendanceReportTable.column("Department", width=100)
        self.AttendanceReportTable.column("Time", width=100)
        self.AttendanceReportTable.column("Date", width=100)
        self.AttendanceReportTable.column("Attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # =========================fetch data================
    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def import_csv(self):
        global my_data
        my_data.clear()
        file_name = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
            parent=self.root,
        )
        with open(file_name) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                my_data.append(i)
            self.fetch_data(my_data)
        # insert 

    def export_csv(self):
        try:
            if len(my_data) < 1:
                messagebox.showerror(
                    "No Data", "No Data Found To Export..", parent=self.root
                )
                return False
            file_name1 = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Open CSV",
                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                parent=self.root,
            )

            with open(file_name1, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for row in my_data:
                    exp_write.writerow(row)
                messagebox.showinfo(
                    "Data Export",
                    "Your Data Exported to"
                    + os.path.basename(file_name1)
                    + "Successfully",
                )

        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
    # def addData(self):
    #     if (
    #         self.var_atten_id.get() == ""
    #         or self.var_atten_roll.get() == ""
    #         or self.var_atten_name.get() == ""
    #         or self.var_atten_dep.get() == ""
    #         or self.var_atten_time.get() == ""
    #         or self.var_atten_date.get() == ""
    #         or self.var_atten_attendance.get() == "Status"
    #     ):
    #         messagebox.showerror("Error", "All Fields are required", parent=self.root)
    #     else:
    #         try:
    #             conn = mysql.connector.connect(
    #                 host="localhost",
    #                 username="root",
    #                 password="pass123",
    #                 database="face_recognizer",
    #             )
    #             my_cursor = conn.cursor()
    #             my_cursor.execute(
    #                 "INSERT INTO attendance (attendance_id, roll_no, name, department, time, date, attendance_status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    #                 (
    #                     self.var_atten_id.get(),
    #                     self.var_atten_roll.get(),
    #                     self.var_atten_name.get(),
    #                     self.var_atten_dep.get(),
    #                     self.var_atten_time.get(),
    #                     self.var_atten_date.get(),
    #                     self.var_atten_attendance.get(),
    #                 ),
    #             )
    #             conn.commit()
    #             self.fetch_data()  
    #             conn.close()
    #             messagebox.showinfo(
    #                 "Success",
    #                 "Attendance details have been added successfully",
    #                 parent=self.root,
    #             )
    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
