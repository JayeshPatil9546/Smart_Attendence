from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1532x840+0+0")  # Updated size to fit all images properly
        self.root.title("Help Desk")

        # First image
        img = Image.open("C:/attendence/college_image/b.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl1 = Label(self.root, image=self.photoimg)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open("C:/attendence/college_image/a3.png")
        img1 = img1.resize((1032, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl2 = Label(self.root, image=self.photoimg1)
        f_lbl2.place(x=500, y=0, width=1032, height=130)

        # Third image (background)
        img2 = Image.open("C:/attendence/college_image/bg.png")
        img2 = img2.resize((1532, 710), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=130, width=1532, height=710)

        # Title label
        title_lbl = Label(bg_img, text="HELP DESK", font=("times new roman", 35, "bold"), bg="black", fg="white") 
        title_lbl.place(x=0, y=0, width=1532, height=45)

        contact_lbl = Label(bg_img, text="For any technical issue please contact:-", font=("times new roman", 35, "bold"), bg="black", fg="white")
        contact_lbl.place(x=0, y=250, width=1532, height=45)

        email_lbl = Label(bg_img, text="Email:-imrd@gmail.com", font=("times new roman", 35, "bold"), bg="black", fg="white") 
        email_lbl.place(x=0, y=350, width=1532, height=45)

        phone_lbl = Label(bg_img, text="Contact No:-+91 987654XXXX", font=("times new roman", 35, "bold"), bg="black", fg="white")
        phone_lbl.place(x=0, y=400, width=1532, height=45)





if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()