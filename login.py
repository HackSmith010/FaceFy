import tkinter as tk
import tkinter.messagebox as tkmb  
import customtkinter as CTk
from PIL import Image,ImageTk  

CTk.set_appearance_mode("System")  
CTk.set_default_color_theme("blue")  

class LoginPage(tk.Frame):  

    def __init__(self, root):
        super().__init__(root)  

        self.root = root  
        self.root.geometry("1366x768+0+0")  
        self.root.title("Login Page...")  
        
        bg_img=ImageTk.PhotoImage(Image.open("Images/loginbg.jpg"))
        l1=CTk.CTkLabel(master=self.root,image=bg_img)
        l1.pack()
        
        frame =CTk.CTkFrame(master=l1,width=320,height=360,corner_radius=15,fg_color="black")
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        l2=CTk.CTkLabel(master=frame,text="Log into your Account",font=('Century Gothic',20,"bold"))
        l2.place(x=50,y=45)

        entry1 = CTk.CTkEntry(master=frame,width=220,placeholder_text="Username")
        entry1.place(x=50,y=110)
        
        entry2 = CTk.CTkEntry(master=frame,width=220,placeholder_text="Password")
        entry2.place(x=50,y=165)
        
        # ====================login function=================
        def login():
            if entry1.get()=="" or entry2.get()=="":
                tkmb.showerror("Error","All Fields are required..")
            elif  entry1.get() == "HackSmith010" and entry2.get() == "Anshu2004":  
                tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
            else: 
                tkmb.showerror(title="Login Failed", 
                message="Invalid Username and password")
        
        # ===================Login Button====================
        button1=CTk.CTkButton(master=frame,width=220,text="Login",corner_radius=6,command=login)
        button1.place(x=50,y=270)
         # ===================Forgot Button====================
        button2=CTk.CTkButton(master=frame,width=160,text="Forget password",corner_radius=6,border_width=0,fg_color="black",hover_color="black")
        button2.place(x=150,y=200)
        
         # ===================New Register Button====================
        button3=CTk.CTkButton(master=frame,width=160,text="New User Register",corner_radius=6,border_width=0,fg_color="black",hover_color="black")
        button3.place(x=150,y=230)
        
        
            


  
        
if __name__ == "__main__":
    root = CTk.CTk()  
    obj = LoginPage(root)
    root.mainloop()  
