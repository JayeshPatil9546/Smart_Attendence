from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1532x840+0+0")
        self.root.title("Train Data")

        # Title label
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1532, height=45)

        # Train button
        train_btn = Button(self.root, text="Train Data", command=self.train_classifier, font=("times new roman", 20, "bold"), bg="blue", fg="white")
        train_btn.place(x=650, y=200, width=200, height=50)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image_path in path:
            img = Image.open(image_path).convert('L')  # Convert to grayscale
            image_np = np.array(img, 'uint8')

            # Assuming filename format: user.id.xxx.jpg  => split by "." and get id
            
            id = int(os.path.split(image_path)[1].split('.')[1])
            

            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training", image_np)
            cv2.waitKey(1)==13

        ids = np.array(ids)

        # Train the model
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed successfully")


# ✅ Main loop
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
