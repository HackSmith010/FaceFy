from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
from cv2 import *
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Face Recognition System")
        
        t_lbl = Label(
            self.root,
            text="Train DataSet",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="green",
        )
        t_lbl.place(x=0, y=0, width=1366, height=45)
        
        # bg_img
        img1 = Image.open("Images/trainingDataBG.jpeg")
        img1 = img1.resize((1366, 768))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_lbl = Label(self.root, image=self.photoimg1)
        bg_lbl.place(x=0, y=45, width=1366, height=723)
        
        #train dataset button
        img2 = Image.open("Images/snip2.png")
        img2 = img2.resize((337, 225))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(
            bg_lbl, image=self.photoimg2,command=self.train_Classifier, cursor="hand2",   
        )
        b1.place(x=547, y=107, width=337, height=225)
        
        
    def train_Classifier(self):
            data_dir=("data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            
            faces=[]
            ids=[]
            
            for image in path:
                img=Image.open(image).convert('L')  
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])
                
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)
            
    #  ======================Train Classifier=================
     
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training Dataset Completed!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()