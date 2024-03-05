from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from time import strftime
from datetime import datetime

from traindata import Train
from student import Student
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Face Recognition System")

        t_lbl = Label(
            text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
            font=("times new roman", 35, "bold"),
            bg="cyan",
            fg="red",
        )
        t_lbl.place(x=0, y=0, width=1366, height=45)
        
        # bg_image
        img1 = Image.open("Images/bgImg1.jpeg")
        img1 = img1.resize((1366, 768))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_lbl = Label(self.root, image=self.photoimg1)
        bg_lbl.place(x=0, y=45, width=1366, height=723)

        # ========================time=======================
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000,time)
            
        lbl = Label(bg_lbl,font=("times new roman",14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        # student_button
        img2 = Image.open("Images/details.jpeg")
        img2 = img2.resize((220, 220))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(
            bg_lbl, image=self.photoimg2, command=self.student_System, cursor="hand2"
        )
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(
            bg_lbl,
            text="Student Details",
            command=self.student_System,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=200, y=300, width=220, height=40)

        # face_recog_button
        img3 = Image.open("Images/recog.jpeg")
        img3 = img3.resize((220, 220))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 = Button(bg_lbl, image=self.photoimg3,command=self.face_data, cursor="hand2")
        b2.place(x=600, y=100, width=220, height=220)

        b2_1 = Button(
            bg_lbl,
            text="Face Recognition",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            command=self.face_data,
            bg="darkblue",
            fg="white",
        )
        b2_1.place(x=600, y=300, width=220, height=40)

        # attendance_management_button
        img4 = Image.open("Images/attendance.jpeg")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b3 = Button(bg_lbl,command=self.attendance_data, image=self.photoimg4)
        b3.place(x=1000, y=100, width=220, height=220)

        b3_1 = Button(
            bg_lbl,
            text="Attendance",
            command=self.attendance_data,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b3_1.place(x=1000, y=300, width=220, height=40)

        # train_data_button
        img5 = Image.open("Images/train.jpeg")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b4 = Button(bg_lbl,command=self.train_data,image=self.photoimg5)
        b4.place(x=200, y=400,width=220, height=220)

        b4_1 = Button(
            bg_lbl,
            text="Train Data",
            command=self.train_data,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b4_1.place(x=200, y=600, width=220, height=40)

        # student_button
        img6 = Image.open("Images/details.jpeg")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b5 = Button(bg_lbl, command=self.open_img, image=self.photoimg6, cursor="hand2")
        b5.place(x=600, y=400, width=220, height=220)

        b5_1 = Button(
            bg_lbl,
            text="Photos",
            cursor="hand2",
            command=self.open_img,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b5_1.place(x=600, y=600, width=220, height=40)

        # exit_button
        img7 = Image.open("Images/details.jpeg")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b6 = Button(bg_lbl,command=self.Exit, image=self.photoimg7, cursor="hand2")
        b6.place(x=1000, y=400, width=220, height=220)

        b6_1 = Button(
            bg_lbl,
            text="Temp 2",
            command=self.Exit,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b6_1.place(x=1000, y=600, width=220, height=40)

    def open_img(self):
        os.startfile("data")
        
    def Exit(self):
        self.Exit = messagebox.askyesno("FaceFy","Do you want to exit the Project?")
        if self.Exit > 0:
            self.root.destroy()
        else:
            return

        # ================Functions==================

    def student_System(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
