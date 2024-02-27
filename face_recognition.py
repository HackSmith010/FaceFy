from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        t_lbl = Label(
            self.root,
            text=" Face Recognization",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="green",
        )
        t_lbl.place(x=0, y=0, width=1366, height=45)

        # button
        b1 = Button(
            self.root,
            text="Face Recognition",
            command=self.face_recog,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1.place(x=600, y=300, width=220, height=40)
        # =====================attendance==========================
    def mark_Attendance(self, r, n, d, c, i):
        try:
            with open("attendance.csv", "r+", newline="\n") as f:
                myDataList = f.readlines()
                existing_student_ids= [line.split(",")[0] for line in myDataList]
        except (FileExistsError, FileNotFoundError):
            with open("attendance.csv", "w", newline="\n") as f:
                existing_student_ids= []
                
        if i not in existing_student_ids:
            with open("attendance.csv", "a", newline="\n") as f:
                now = datetime.now()
                dtStr = now.strftime("%H:%M:%S")
                d1 = now.strftime("%d/%m/%Y")
                f.write(f"{i},{r},{n},{d},{c},{dtStr},{d1},Present\n")
                
                print("Attendance marked successfully for student ID:", i)
        else:
            print("Attendance already recorded for student ID:", i)
            
            
# ===================================face Recognition=====================
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            featuers = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors
            )

            coord = []

            for x, y, w, h in featuers:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y : y + h, x : x + w])
                # print(id)

                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    username="root",
                    password="anshu2004",
                    host="localhost",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select Student_name from student where Student_Id=" + str(id)
                )
                n = my_cursor.fetchone()
                # print(n)
                # n = list(n)
                # n = "+".join(n)

                my_cursor.execute(
                    "select RollNo from student where Student_Id=" + str(id)
                )
                r = my_cursor.fetchone()
                # r = list(r)
                # r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_Id=" + str(id))
                d = my_cursor.fetchone()
                # d = list(d)
                # d = "+".join(d)

                my_cursor.execute(
                    "select Course from student where Student_Id=" + str(id)
                )
                c = my_cursor.fetchone()

                my_cursor.execute(
                    "select Student_Id from student where Student_Id=" + str(id)
                )
                i = my_cursor.fetchone()
                # c = list(c)
                # c = "+".join(c)
                # print(f"Data: {r}, {n[0]}, {d[0]}, {c[0]}")
                if confidence > 77:
                    cv2.putText(
                        img,
                        f"Roll_No:{r[0]}",
                        (x, y - 80),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.5,
                        (64, 15, 223),
                        2,
                    )
                    cv2.putText(
                        img,
                        f"Student Name:{n[0]}",
                        (x, y - 60),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.5,
                        (64, 15, 223),
                        2,
                    )
                    cv2.putText(
                        img,
                        f"Dep:{d[0]}",
                        (x, y - 40),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.5,
                        (64, 15, 223),
                        2,
                    )
                    cv2.putText(
                        img,
                        f"Course:{c[0]}",
                        (x, y - 20),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.5,
                        (64, 15, 223),
                        2,
                    )
                    self.mark_Attendance(r,n,d,c,i)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(
                        img,
                        "Unknown Face",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 0),
                        3,
                    )

                coord = [x, y, w, y]

            return coord

        # ==========face Recognier=================
        def recognize(img, clf, faceCascade):
            coord = draw_boundray(
                img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf
            )
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap = cv2.VideoCapture(1)

        while True:
            ret, img = videoCap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
