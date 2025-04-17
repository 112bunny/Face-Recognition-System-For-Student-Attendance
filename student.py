from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import mysql.connector
from keras_facenet import FaceNet


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Student Details")

        # ================= Variables =================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.photo_sample = StringVar()

        # ================= Main Frame =================
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=10, width=1480, height=760)

        # ================= Title =================
        title_lbl = Label(main_frame, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1480, height=50)

        # ================= Left Frame =================
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("times new roman", 15, "bold"))
        left_frame.place(x=10, y=60, width=720, height=680)

        # ============ Department ============
        lbl_dep = Label(left_frame, text="Department", font=("times new roman", 12, "bold"))
        lbl_dep.grid(row=0, column=0, padx=10, sticky=W)
        combo_dep = ttk.Combobox(left_frame, textvariable=self.var_dep,
                                 font=("times new roman", 12, "bold"), state="readonly")
        combo_dep["values"] = ("Select Department", "CSE", "IT", "ECE", "Mechanical")
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # ============ Course ============
        lbl_course = Label(left_frame, text="Course", font=("times new roman", 12, "bold"))
        lbl_course.grid(row=0, column=2, padx=10, sticky=W)
        combo_course = ttk.Combobox(left_frame, textvariable=self.var_course,
                                    font=("times new roman", 12, "bold"), state="readonly")
        combo_course["values"] = ("Select Course", "BCA", "B.Tech", "MCA", "M.Tech")
        combo_course.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # ============ Year ============
        lbl_year = Label(left_frame, text="Year", font=("times new roman", 12, "bold"))
        lbl_year.grid(row=1, column=0, padx=10, sticky=W)
        combo_year = ttk.Combobox(left_frame, textvariable=self.var_year,
                                  font=("times new roman", 12, "bold"), state="readonly")
        combo_year["values"] = ("Select Year", "1st", "2nd", "3rd", "4th")
        combo_year.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # ============ Semester ============
        lbl_semester = Label(left_frame, text="Semester", font=("times new roman", 12, "bold"))
        lbl_semester.grid(row=1, column=2, padx=10, sticky=W)
        combo_semester = ttk.Combobox(left_frame, textvariable=self.var_semester,
                                      font=("times new roman", 12, "bold"), state="readonly")
        combo_semester["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4")
        combo_semester.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # ================= Class Student Information =================
        class_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Class Student Information",
                                  font=("times new roman", 15, "bold"))
        class_frame.place(x=5, y=100, width=700, height=450)

        # ============ Student ID ============
        lbl_std_id = Label(class_frame, text="Student ID:", font=("times new roman", 12, "bold"))
        lbl_std_id.grid(row=0, column=0, padx=10, sticky=W)
        self.entry_std_id = ttk.Entry(class_frame, textvariable=self.var_std_id,
                                      font=("times new roman", 12, "bold"), width=20)
        self.entry_std_id.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # ============ Student Name ============
        lbl_std_name = Label(class_frame, text="Student Name:", font=("times new roman", 12, "bold"))
        lbl_std_name.grid(row=0, column=2, padx=10, sticky=W)
        self.entry_std_name = ttk.Entry(class_frame, textvariable=self.var_std_name,
                                        font=("times new roman", 12, "bold"), width=20)
        self.entry_std_name.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # ============ Division ============
        lbl_div = Label(class_frame, text="Class Division", font=("times new roman", 12, "bold"))
        lbl_div.grid(row=1, column=0, padx=10, sticky=W)
        combo_div = ttk.Combobox(class_frame, textvariable=self.var_div,
                                  font=("times new roman", 12, "bold"), state="readonly")
        combo_div["values"] = ("A", "B", "C", "D")
        combo_div.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # ============ Roll No ============
        lbl_roll = Label(class_frame, text="Roll No:", font=("times new roman", 12, "bold"))
        lbl_roll.grid(row=1, column=2, padx=10, sticky=W)
        self.entry_roll = ttk.Entry(class_frame, textvariable=self.var_roll,
                                    font=("times new roman", 12, "bold"), width=20)
        self.entry_roll.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # ============ Gender ============
        lbl_gender = Label(class_frame, text="Gender:", font=("times new roman", 12, "bold"))
        lbl_gender.grid(row=2, column=0, padx=10, sticky=W)
        combo_gender = ttk.Combobox(class_frame, textvariable=self.var_gender,
                                    font=("times new roman", 12, "bold"), state="readonly")
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # ============ DOB ============
        lbl_dob = Label(class_frame, text="DOB:", font=("times new roman", 12, "bold"))
        lbl_dob.grid(row=2, column=2, padx=10, sticky=W)
        self.entry_dob = ttk.Entry(class_frame, textvariable=self.var_dob,
                                   font=("times new roman", 12, "bold"), width=20)
        self.entry_dob.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # ============ Email ============
        lbl_email = Label(class_frame, text="Email:", font=("times new roman", 12, "bold"))
        lbl_email.grid(row=3, column=0, padx=10, sticky=W)
        self.entry_email = ttk.Entry(class_frame, textvariable=self.var_email,
                                     font=("times new roman", 12, "bold"), width=20)
        self.entry_email.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # ============ Phone ============
        lbl_phone = Label(class_frame, text="Phone:", font=("times new roman", 12, "bold"))
        lbl_phone.grid(row=3, column=2, padx=10, sticky=W)
        self.entry_phone = ttk.Entry(class_frame, textvariable=self.var_phone,
                                     font=("times new roman", 12, "bold"), width=20)
        self.entry_phone.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # ============ Address ============
        lbl_address = Label(class_frame, text="Address:", font=("times new roman", 12, "bold"))
        lbl_address.grid(row=4, column=0, padx=10, sticky=W)
        self.entry_address = ttk.Entry(class_frame, textvariable=self.var_address,
                                       font=("times new roman", 12, "bold"), width=20)
        self.entry_address.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # ============ Teacher ============
        lbl_teacher = Label(class_frame, text="Teacher Name:", font=("times new roman", 12, "bold"))
        lbl_teacher.grid(row=4, column=2, padx=10, sticky=W)
        self.entry_teacher = ttk.Entry(class_frame, textvariable=self.var_teacher,
                                       font=("times new roman", 12, "bold"), width=20)
        self.entry_teacher.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # ============ Photo Sample Option ============
        lbl_photo = Label(class_frame, text="Photo Sample:", font=("times new roman", 12, "bold"))
        lbl_photo.grid(row=5, column=0, padx=10, sticky=W)

        self.photo_sample.set("No")
        take_photo = Radiobutton(class_frame, text="Take Photo Sample", variable=self.photo_sample, value="Yes")
        take_photo.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        no_photo = Radiobutton(class_frame, text="No Photo Sample", variable=self.photo_sample, value="No")
        no_photo.grid(row=5, column=2, padx=10, pady=5, sticky=W)

        # ================= Buttons =================
        btn_frame = Frame(class_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=380, width=700, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, font=("times new roman", 12, "bold"),
                          bg="blue", fg="white", width=15)
        save_btn.grid(row=0, column=0)

        capture_btn = Button(btn_frame, text="Capture", command=self.capture_face, font=("times new roman", 12, "bold"),
                             bg="green", fg="white", width=15)
        capture_btn.grid(row=0, column=1)

    # ================= Function to Save Student Data =================
    def add_data(self):
        if self.var_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Dipan#1234",
                                           database="face_recognizer", auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            query = """INSERT INTO student (Dep, course, year, semester, student_id, name, division, roll, gender, dob, email, phone, address, teacher, photoSample) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            data = (
                self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                self.var_std_id.get(), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(),
                self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(),
                self.var_address.get(), self.var_teacher.get(), self.photo_sample.get()
            )
            my_cursor.execute(query, data)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Student details added successfully!", parent=self.root)

    # ================= Function to Capture and Store Face =================
    def capture_face(self):
        if self.var_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("Error", "Please enter Student ID and Name", parent=self.root)
            return

        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        embedder = FaceNet()

        captured = False

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                face = frame[y:y + h, x:x + w]
                face_rgb = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                face_resized = cv2.resize(face_rgb, (160, 160))

                cv2.putText(frame, "Press 'C' to Capture or 'Q' to Quit", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            cv2.imshow("Face Capture", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('c'):
                img_path = f"C:/Major_project/data/{self.var_std_id.get()}.jpg"
                cv2.imwrite(img_path, face_resized)

                face_expanded = np.expand_dims(face_resized, axis=0)
                embeddings = embedder.embeddings(face_expanded)[0]
                np.save(f"C:/Major_project/data/{self.var_std_id.get()}.npy", embeddings)

                captured = True
                messagebox.showinfo("Success", f"Photo captured and saved for Student ID: {self.var_std_id.get()}")
                break

            elif key == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


# ============================
# Main Function
# ============================
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
