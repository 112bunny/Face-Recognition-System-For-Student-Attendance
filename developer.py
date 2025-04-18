from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")  
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER ",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1505,height=45)

        img_top = Image.open(r"C:\face_recognition\pic\deep-leraning.jpg")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)


#*******frame*******
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=500)

        img_top1 = Image.open(r"C:\face_recognition\pic\vectee.jpg")
        img_top1 = img_top1.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)

#developer info
        


        dep_label=Label(main_frame,text="Team members:",font=("times new roman",31,"bold"),bg="white")
        dep_label.place(x=0,y=5)
        dep_label=Label(main_frame,text="Dipanwita Acharya",font=("times new roman",21,"bold"),bg="white")
        dep_label.place(x=0,y=70)
        dep_label=Label(main_frame,text="Anisha Roy",font=("times new roman",21,"bold"),bg="white")
        dep_label.place(x=0,y=130)
        dep_label=Label(main_frame,text="Srinjoy Dutta",font=("times new roman",21,"bold"),bg="white")
        dep_label.place(x=0,y=190)
        dep_label=Label(main_frame,text="Sagar Dey",font=("times new roman",21,"bold"),bg="white")
        dep_label.place(x=0,y=250)


        

        img_width = 120  # Each image width
        img_height = 165  # Each image height

        # Load and Resize Four Different Images
        img1 = Image.open(r"C:\face_recognition\pic\Passport Formal Dipanwita  (3).jpg")
        img1 = img1.resize((img_width, img_height), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        img2 = Image.open(r"C:\face_recognition\pic\srinjoy.jpg")
        img2 = img2.resize((img_width, img_height), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img3 = Image.open(r"C:\face_recognition\pic\anisha.png")
        img3 = img3.resize((img_width, img_height), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        img4 = Image.open(r"C:\face_recognition\pic\sagar.jpg")
        img4 = img4.resize((img_width, img_height), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        # Place Images in a Row
        x_padding = 0 # Padding between images
        y_position = 320  # Y-coordinate for all images

        f_lbl1 = Label(main_frame, image=self.photoimg1)
        f_lbl1.place(x=10, y=y_position, width=img_width, height=img_height)

        f_lbl2 = Label(main_frame, image=self.photoimg2)
        f_lbl2.place(x=10 + img_width + x_padding, y=y_position, width=img_width, height=img_height)

        f_lbl3 = Label(main_frame, image=self.photoimg3)
        f_lbl3.place(x=10 + 2*(img_width + x_padding), y=y_position, width=img_width, height=img_height)

        f_lbl4 = Label(main_frame, image=self.photoimg4)
        f_lbl4.place(x=10 + 3*(img_width + x_padding), y=y_position, width=img_width, height=img_height)






if __name__ == "__main__":
    
    root = Tk()
    obj = Developer(root)
    root.mainloop()       