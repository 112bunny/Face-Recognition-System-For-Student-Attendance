from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
from keras_facenet import FaceNet


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        # ================= Title =================
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1505, height=45)

        # ================= Top Image =================
        img_top = Image.open(r"C:\face_recognition\pic\1_SrBuponCt2tn5s1yQxee7g.jpg")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        # ================= Train Button =================
        bt_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
                      font=("times new roman", 30, "bold"), bg="red", fg="white")
        bt_1.place(x=0, y=380, width=1530, height=60)

        # ================= Bottom Image =================
        img_bottom = Image.open(r"C:\face_recognition\pic\istockphoto-115903.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

        # Initialize FaceNet model
        self.embedder = FaceNet()

    # ============================
    # Training Function
    # ============================
    def train_classifier(self):
        data_dir = r"C:/Major_project/data"  # Directory where captured face data is stored

        # Check if data directory exists
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found!")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".jpg")]
        face_embeddings = []  # Store embeddings for all faces
        ids = []  # Store student IDs

        # Loop through all images and process
        for image in path:
            # Load and convert image to RGB (FaceNet requires RGB input)
            img = cv2.imread(image)
            if img is None:
                continue  # Skip invalid images

            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get face embedding using FaceNet
            faces = self.embedder.extract(rgb_img, threshold=0.95)

            if len(faces) == 0:
                continue  # Skip if no face is found

            for face in faces:
                x, y, w, h = face['box']
                face_crop = rgb_img[y:y + h, x:x + w]

                # Resize face to 160x160 (FaceNet input size)
                face_crop_resized = cv2.resize(face_crop, (160, 160))
                face_crop_resized = np.expand_dims(face_crop_resized, axis=0)  # Add batch dimension

                # Generate embedding for the cropped face
                embedding = self.embedder.embeddings(face_crop_resized)[0]

                # Extract student ID from image filename
                try:
                    student_id = int(os.path.split(image)[1].split('.')[0])  # Extract ID from filename
                except ValueError:
                    continue  # Skip if file name is not in the expected format

                # Store embedding and ID
                face_embeddings.append(embedding)
                ids.append(student_id)

                # Show the training face for visualization
                cv2.imshow("Training", cv2.cvtColor(face_crop, cv2.COLOR_RGB2BGR))
                cv2.waitKey(1)

        # Ensure embeddings and IDs are available
        if len(face_embeddings) == 0:
            messagebox.showerror("Error", "No valid face data found for training!")
            cv2.destroyAllWindows()
            return

        # Convert embeddings and IDs to numpy arrays
        face_embeddings = np.array(face_embeddings)
        ids = np.array(ids)

        # Save embeddings and IDs in .npz file
        np.savez("face_embeddings.npz", embeddings=face_embeddings, ids=ids)

        # Close all OpenCV windows
        cv2.destroyAllWindows()

        # Show success message
        messagebox.showinfo("Result", "Training completed and embeddings saved successfully!")


# ============================
# Main Function
# ============================
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)  # Create an object of the Train class
    root.mainloop()
