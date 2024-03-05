import tkinter as tk
import customtkinter as CTk
import tkinter.messagebox as tkmb 
from PIL import Image,ImageTk  

CTk.set_appearance_mode("system")  
CTk.set_default_color_theme("green")  

class Register(tk.Frame):  

    def __init__(self, root):
        super().__init__(root)  

        self.root = root  
        self.root.geometry("1366x768+0+0")  
        self.root.title("Register...")  
        
        # ============================variables=======================
        var_fname = CTk.StringVar()
        var_lname = CTk.StringVar()
        var_contact = CTk.StringVar()
        var_email = CTk.StringVar()
        combo_var = CTk.StringVar()
        var_SecAns = CTk.StringVar()
        var_pass = CTk.StringVar()
        var_Cpass = CTk.StringVar()
        var_check = CTk.IntVar()
        
        bg_img=ImageTk.PhotoImage(Image.open("Images/bg1.jpg"))
        l1=CTk.CTkLabel(master=self.root,image=bg_img)
        l1.pack()
        
        frame =CTk.CTkFrame(master=l1,width=800,height=500,corner_radius=15)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        l2=CTk.CTkLabel(master=frame,text="REGISTER HERE",font=('Century Gothic',20,"bold"))
        l2.place(x=350,y=40)
        
        # ====================register function=======================
        def register():
                if var_fname.get()==""or var_email.get()=="" or var_Cpass.get()=="":
                        tkmb.showerror("Error","All Fields are Required..")
                elif var_pass.get()==var_Cpass.get():
                        tkmb.showerror("Error","Password and Confirm Password are having different credentials.")
                elif var_check.get()==0:
                        tkmb.showerror("Error","Please Agree our Terms and Conditions")
                else:
                        tkmb.showinfo("Successful")
                        
        

# =======================labels and entry===================

        fname = CTk.CTkLabel(master=frame,text="First Name",font=('Century Gothic',15))
        fname.place(x=100,y=100)

        fname_entry=CTk.CTkEntry(master=frame,textvariable=var_fname,width=220)
        fname_entry.place(x=100,y=130)
        
        lname = CTk.CTkLabel(master=frame,text="Last Name",font=('Century Gothic',15))
        lname.place(x=450,y=100)

        lname_entry=CTk.CTkEntry(master=frame,textvariable=var_lname,width=220)
        lname_entry.place(x=450,y=130)
        
        contact = CTk.CTkLabel(master=frame,text="Contact No.",font=('Century Gothic',15))
        contact.place(x=100,y=160)

        contact_entry=CTk.CTkEntry(master=frame,textvariable=var_contact,width=220)
        contact_entry.place(x=100,y=190)
        
        email = CTk.CTkLabel(master=frame,text="Email",font=('Century Gothic',15))
        email.place(x=450,y=160)

        email_entry=CTk.CTkEntry(master=frame,textvariable=var_email,width=220)
        email_entry.place(x=450,y=190)
        
        security = CTk.CTkLabel(master=frame,text="Security Question",font=('Century Gothic',15))
        security.place(x=100,y=220)
        
        combo_var = CTk.StringVar(value="")
        security_combo = CTk.CTkComboBox(master=frame,values=[
                                                                "Your Pet name",
                                                                "Your Favourite Game",
                                                                "Your Best Friend's Name"],
                                         variable=combo_var,
                                         width=220)
        combo_var.set("Select Security Question")
        security_combo.place(x=100,y=250)
        
        security_ans = CTk.CTkLabel(master=frame,text="Security Answer",font=('Century Gothic',15))
        security_ans.place(x=450,y=220)
        security_ans_entry=CTk.CTkEntry(master=frame,textvariable=var_SecAns,width=220)
        security_ans_entry.place(x=450,y=250)
        
        passw = CTk.CTkLabel(master=frame,text="Password",font=('Century Gothic',15))
        passw.place(x=100,y=280)
        passw_entry=CTk.CTkEntry(master=frame,textvariable=var_pass,width=220)
        passw_entry.place(x=100,y=310)
        
        rpassw = CTk.CTkLabel(master=frame,text="Confirm Password",font=('Century Gothic',15))
        rpassw.place(x=450,y=280)
        rpassw_entry=CTk.CTkEntry(master=frame,textvariable=var_Cpass,width=220)
        rpassw_entry.place(x=450,y=310)
        
# ========================check Button====================
        chckbtn = CTk.CTkCheckBox(master=frame,textvariable=var_check,text="I Agree the Terms & Conditions",font=('Century Gothic',12))
        chckbtn.place(x=100,y=380)
        
#  =======================buttons==================
        loginnow = CTk.CTkButton(master=frame,width=220,text="Login Now",corner_radius=6,fg_color="white",text_color="Black",hover_color="grey")
        loginnow.place(x=400,y=420)
        
        registernow = CTk.CTkButton(master=frame,command=register,width=220,text="Register Now",corner_radius=6,fg_color="white",text_color="Black",hover_color="grey")
        registernow.place(x=150,y=420)
        
        


  
        
if __name__ == "__main__":
    root = CTk.CTk()  
    obj = Register(root)
    root.mainloop()