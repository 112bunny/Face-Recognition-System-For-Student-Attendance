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
from help import Help  # Commented to avoid error

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        # First image
        img = Image.open(r"C:\face_recognition\pic\istockphoto-1169.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"C:\face_recognition\pic\sole.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"C:\face_recognition\pic\imagesss.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=950, y=0, width=550, height=130)

        # Background image
        img3 = Image.open(r"C:\face_recognition\pic\pexels-photo-417074.jpeg")
        img3 = img3.resize((1505, 691), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1505, height=691)

        # Title
        title_lbl = Label(
            bg_img,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1505, height=45)

        # ================================
        # Button Section
        # ================================

        # Student button
        img4 = Image.open(r"C:\face_recognition\pic\student-profile.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(
            bg_img,
            text="Student Details",
            command=self.student_details,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=200, y=300, width=220, height=40)

        # Face Detector button
        img5 = Image.open(r"C:\face_recognition\pic\airkd.png")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b2.place(x=500, y=100, width=220, height=220)

        b2_1 = Button(
            bg_img,
            text="Face Detector",
            cursor="hand2",
            command=self.face_data,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b2_1.place(x=500, y=300, width=220, height=40)

        # Help button
        img7 = Image.open(r"C:\face_recognition\pic\images.png")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b3 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.help_data)
        b3.place(x=800, y=100, width=220, height=220)

        b3_1 = Button(
            bg_img,
            text="Help Desk",
            cursor="hand2",
            command=self.help_data,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b3_1.place(x=800, y=300, width=220, height=40)

        # Train button
        img8 = Image.open(r"C:\face_recognition\pic\2985134-200.png")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b4 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b4.place(x=200, y=380, width=220, height=220)

        b4_1 = Button(
            bg_img,
            text="Train Data",
            cursor="hand2",
            command=self.train_data,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b4_1.place(x=200, y=580, width=220, height=40)

        # Developer button
        img10 = Image.open(r"C:\face_recognition\pic\depositphotos_305.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b5 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_data)
        b5.place(x=500, y=380, width=220, height=220)

        b5_1 = Button(
            bg_img,
            text="Developer",
            cursor="hand2",
            command=self.developer_data,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b5_1.place(x=500, y=580, width=220, height=40)

        # Exit button
        img11 = Image.open(r"C:\face_recognition\pic\exit1.png")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b6 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b6.place(x=800, y=380, width=220, height=220)

        b6_1 = Button(
            bg_img,
            text="Exit",
            cursor="hand2",
            command=self.iExit,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b6_1.place(x=800, y=580, width=220, height=40)

    # ================================
    # Functions
    # ================================
    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure to exit the window?", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

# ================================
# Main Program
# ================================
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
