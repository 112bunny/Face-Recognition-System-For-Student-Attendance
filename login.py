from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
from student import Student
import os
import tkinter
from train import Train
from face_recognition import Face_Recognition

from developer import Developer
from help import Help
from main import Face_Recognition_System


# ============================
# Main Function
# ============================
def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


# ============================
# Login Window Class
# ============================
class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1600x900+0+0")

        # Load background image
        lbl_bg = Image.open(r"C:\face_recognition\pic\pngtree-abstract-technology-background-technical-electric-image_443494.jpg")
        lbl_bg = lbl_bg.resize((1540, 900), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(lbl_bg)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1550, height=900)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"C:\face_recognition\pic\login_face.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimage1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimage1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Username label and entry
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Password label and entry
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        # Login button
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register button
        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # Forgot password button
        forgotbtn = Button(frame, text="Forget Password", command=self.forgot_password_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgotbtn.place(x=10, y=370, width=160)

    # ============================
    # Login Function
    # ============================
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Dipan#1234",
                database="face_recognizer",
                auth_plugin="mysql_native_password"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (self.txtuser.get(), self.txtpass.get()))
            row = my_cursor.fetchone()
            
            if row == None:
                messagebox.showerror("Error", "Invalid Username or Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access granted. Do you want to proceed?")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)  # Open Main System Window
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ============================
    # Open Main Window After Login
    # ============================
    def open_main_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition_System(self.new_window)

    # ============================
    # Open Register Window
    # ============================
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    # ============================
    # Forgot Password Window
    # ============================
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter your email to reset password")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Dipan#1234",
                database="face_recognizer",
                auth_plugin="mysql_native_password"
            )
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s"
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            
            if row == None:
                messagebox.showerror("Error", "Email not found!")
            else:
                conn.close()
                self.reset_password_window()

    # ============================
    # Reset Password Window
    # ============================
    def reset_password_window(self):
        self.root2 = Toplevel()
        self.root2.title("Reset Password")
        self.root2.geometry("400x400+450+150")

        lbl = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"))
        lbl.place(x=50, y=30)

        self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Teacher's Name", "Your Pet's Name")
        self.combo_security_Q.place(x=50, y=70, width=250)
        self.combo_security_Q.current(0)

        lbl_ans = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"))
        lbl_ans.place(x=50, y=110)

        self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
        self.txt_security.place(x=50, y=140, width=250)

        lbl_new_pass = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"))
        lbl_new_pass.place(x=50, y=180)

        self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
        self.txt_newpass.place(x=50, y=210, width=250)

        btn_reset = Button(self.root2, text="Reset", command=self.reset_password, font=("times new roman", 15, "bold"), fg="white", bg="green")
        btn_reset.place(x=150, y=270)

    # ============================
    # Reset Password Function
    # ============================
    def reset_password(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select Security Question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Dipan#1234",
                database="face_recognizer",
                auth_plugin="mysql_native_password"
            )
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            
            if row == None:
                messagebox.showerror("Error", "Please enter the correct answer", parent=self.root2)
            else:
                query = "UPDATE register SET password=%s WHERE email=%s"
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Your password has been reset successfully!", parent=self.root2)
                self.root2.destroy()


# ============================
# Registration Class
# ============================
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Background
        bg_img = Image.open(r"C:\face_recognition\pic\beautiful-scenery-desktop-wallpaper-62em4rvehqrfvdji.jpg")
        bg_img = bg_img.resize((1550, 900), Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)

        bg_lbl = Label(self.root, image=self.photoimg_bg)
        bg_lbl.place(x=0, y=0, width=1550, height=900)

        frame = Frame(self.root, bg="white")
        frame.place(x=350, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # Label and Entry for First Name
        fname_lbl = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname_lbl.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        self.fname_entry.place(x=50, y=130, width=250)

        # Last Name
        lname_lbl = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname_lbl.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # Contact
        contact_lbl = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact_lbl.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        # Email
        email_lbl = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email_lbl.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # Security Question
        secQ_lbl = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        secQ_lbl.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Teacher's Name", "Your Pet's Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        # Security Answer
        secA_lbl = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        secA_lbl.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # Password
        pswd_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd_lbl.place(x=50, y=310)

        self.txt_pass = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        self.txt_pass.place(x=50, y=340, width=250)

        # Confirm Password
        cpswd_lbl = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        cpswd_lbl.place(x=370, y=310)

        self.txt_cpass = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*")
        self.txt_cpass.place(x=370, y=340, width=250)

        # Register Button
        register_btn = Button(frame, text="Register", command=self.register_data, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="green", activeforeground="white", activebackground="green")
        register_btn.place(x=300, y=450, width=150)

    # ============================
    # Registration Data Function
    # ============================
    def register_data(self):
        if (
            self.var_fname.get() == ""
            or self.var_contact.get() == ""
            or self.var_email.get() == ""
            or self.var_securityQ.get() == "Select"
        ):
            messagebox.showerror("Error", "All fields are required!")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm Password must be the same!")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Dipan#1234",
                database="face_recognizer",
                auth_plugin="mysql_native_password"
            )
            my_cursor = conn.cursor()
            query = "INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            value = (
                self.var_fname.get(),
                self.var_lname.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_securityQ.get(),
                self.var_securityA.get(),
                self.var_pass.get(),
            )
            my_cursor.execute(query, value)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration Successful!")


# ============================
# Main System Page After Login
# ============================
"""class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1350x700+0+0")

        lbl_title = Label(self.root, text="Welcome to Face Recognition System", font=("times new roman", 35, "bold"), fg="green")
        lbl_title.pack(side=TOP, fill=X)"""


# ============================
# Main Execution
# ============================
if __name__ == "__main__":
    main()
