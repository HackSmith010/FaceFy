from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
import cv2
import threading

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Attendance Details")
        
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
        
        inside_framel = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        inside_framel.place(x=20,y=15,width=623,height=600)
        
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
            font=("times new roman", 12, "bold"),
            width=16,
            state="readonly",
        )
        l7_combo["values"] = (
            "Status",
            "Present",
            "Absent"
        )
        l7_combo.current(0)
        l7_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        btn_frame = Frame(inside_framel, relief=RIDGE, bd=2, bg="White")
        btn_frame.place(x=0, y=250, width=620, height=40)

        Import = Button(
            btn_frame,
            text="Import csv",
            width=15,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        Import.grid(row=0, column=0)
        
        Export = Button(
            btn_frame,
            text="Export csv",
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
            width=15,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        reset_btn.grid(row=0, column=3, pady=2)
        
        #right label frame
        right_frame = LabelFrame(
            self.root,
            bd=7,
            relief=RIDGE,
            text="Attendance Details",
            font=("times new roman", 20, "bold"),
        )
        right_frame.place(x=685, y=65, width=663, height=660)

        inside_framer = Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        inside_framer.place(x=20,y=15,width=623,height=600)













if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()