from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import mysql.connector
import pandas as pd
from datetime import datetime
from keras_facenet import FaceNet
from scipy.spatial.distance import cosine


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        # ================= Title =================
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1505, height=45)

        # ================= Left Image =================
        img_left = Image.open(r"C:\face_recognition\pic\airkd.png")
        img_left = img_left.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # ================= Right Image =================
        img_right = Image.open(r"C:\face_recognition\pic\Facial-Recognition.jpg")
        img_right = img_right.resize((850, 700), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.root, image=self.photoimg_right)
        f_lbl.place(x=650, y=55, width=850, height=700)

        # ================= Recognize Button =================
        bt_1 = Button(self.root, text="FACE RECOGNITION", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 30, "bold"), bg="green", fg="white")
        bt_1.place(x=650, y=680, width=850, height=60)

        # Initialize FaceNet model
        self.embedder = FaceNet()

        # Load stored embeddings
        self.embeddings, self.student_ids = self.load_stored_embeddings()

    # ============================
    # Load Stored Embeddings and Student IDs
    # ============================
    def load_stored_embeddings(self):
        data_path = "C:/Major_project/data/"
        embeddings = []
        student_ids = []

        for file in os.listdir(data_path):
            if file.endswith(".npy"):
                file_path = os.path.join(data_path, file)
                embedding = np.load(file_path)

                # Extract the student ID from the file name
                student_id = file.split(".")[0]
                embeddings.append(embedding)
                student_ids.append(student_id)

        if len(embeddings) == 0:
            messagebox.showerror("Error", "No embeddings found in the data folder!")
        return np.array(embeddings), student_ids

    # ============================
    # Fetch Student Name from MySQL
    # ============================
    def fetch_student_name(self, student_id):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Dipan#1234",
                database="face_recognizer",
                auth_plugin="mysql_native_password"
            )
            cursor = conn.cursor()
            query = "SELECT name FROM student WHERE student_id = %s"
            cursor.execute(query, (student_id,))
            result = cursor.fetchone()

            conn.close()

            if result:
                return result[0]  # Return the student's name
            else:
                return "Unknown"  # Return "Unknown" if student not found

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"MySQL Error: {e}")
            return "Unknown"

    # ============================
    # Mark Attendance in Excel
    # ============================
    def mark_attendance(self, student_name):
        file_path = "attendance.xlsx"
        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y")
        time_str = now.strftime("%H:%M:%S")

        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
        else:
            df = pd.DataFrame(columns=["Date", "Time", "Name", "Status"])

        # Check if attendance is already marked
        if ((df["Date"] == date_str) & (df["Name"] == student_name)).any():
            return  # Skip if attendance already marked

        # Mark attendance
        new_row = pd.DataFrame({"Date": [date_str], "Time": [time_str], "Name": [student_name], "Status": ["Present"]})
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(file_path, index=False)

    # ============================
    # Face Recognition Logic
    # ============================
    def face_recog(self):
        # Open camera
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        # Initialize accuracy variables
        true_positives = 0
        false_negatives = 0
        total_faces_detected = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                face_crop = frame[y:y + h, x:x + w]
                rgb_face = cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)

                # Resize face to 160x160 (FaceNet requirement)
                face_resized = cv2.resize(rgb_face, (160, 160))
                face_resized = np.expand_dims(face_resized, axis=0)

                # Get embedding for captured face
                embedding = self.embedder.embeddings(face_resized)[0]
                min_dist = 100  # High initial distance
                best_match_id = None

                # Compare with stored embeddings
                for stored_embedding, student_id in zip(self.embeddings, self.student_ids):
                    dist = cosine(embedding, stored_embedding)

                    if dist < 0.4 and dist < min_dist:
                        min_dist = dist
                        best_match_id = student_id

                # ============================
                # Calculate True Positives (TP) and False Negatives (FN)
                # ============================
                if best_match_id is not None and min_dist < 0.4:
                    student_name = self.fetch_student_name(best_match_id)
                    self.mark_attendance(student_name)
                    color = (0, 255, 0)  # Green for recognized faces
                    true_positives += 1
                else:
                    student_name = "Unknown"
                    color = (0, 0, 255)  # Red for unrecognized faces
                    false_negatives += 1

                total_faces_detected += 1
                cv2.putText(frame, student_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 3)

            cv2.imshow("Face Recognition", frame)

            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()

        # ============================
        # Calculate and Display Accuracy
        # ============================
        if total_faces_detected > 0:
            accuracy = (true_positives / (true_positives + false_negatives)) * 100
            print(f"\n✅ Face Recognition Accuracy: {accuracy:.2f}%")
            messagebox.showinfo("Accuracy", f"Face Recognition Accuracy: {accuracy:.2f}%")
        else:
            print("No faces detected during the session!")
            messagebox.showinfo("Accuracy", "No faces detected during the session!")


# ============================
# Main Function
# ============================
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)  # Create an object of the Face_Recognition class
    root.mainloop()
