from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1532x840+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1532, height=45)

        img1= Image.open("college_image/face_recognition.jpg")
        img1 = img1.resize((1532, 795   ), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=45, width=1532, height=795)

        # Button to start face recognition
        button_recognize = Button(f_lbl, text="Start Face Recognition", cursor="hand2", font=("times new roman", 20, "bold"), bg="black", fg="white")
        button_recognize.place(x=600, y=650, width=300, height=40)




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()