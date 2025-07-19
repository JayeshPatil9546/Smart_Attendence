from tkinter import *
from PIL import Image, ImageTk
from student import Student
import os

class Face_Recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1532x840+0+0")  # Updated size to fit all images properly
        self.root.title("Face Recognition System")

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
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="black", fg="white") 
        title_lbl.place(x=0, y=0, width=1532, height=45)

        #student Butten
        img3 = Image.open("C:/attendence/college_image/student.png")
        img3 = img3.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img, image=self.photoimg3,command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=200, y=320, width=220, height=40)

        # Face Detector Button
        img4 = Image.open("C:/attendence/college_image/face_detection.jpeg") 
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b2 = Button(bg_img, image=self.photoimg4, cursor="hand2") 
        b2.place(x=500, y=100, width=220, height=220)

        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b2_1.place(x=500, y=320, width=220, height=40)

        # Attendance Button
        img5 = Image.open("C:/attendence/college_image/attendence.png")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b3 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold") , bg="black", fg="white")
        b3_1.place(x=800, y=320, width=220, height=40)

        #help Butten
        img6 = Image.open("C:/attendence/college_image/help.jpeg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b4 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)

        b4_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b4_1.place(x=1100, y=320, width=220, height=40)

        #Train Butten
        img7 = Image.open("C:/attendence/college_image/train.png")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b5 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b5.place(x=200, y=400, width=220, height=220)

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b5_1.place(x=200, y=620, width=220, height=40)

        # Photos Button
        img8 = Image.open("C:/attendence/college_image/photos.png")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b6 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.open_img)
        b6.place(x=500, y=400, width=220, height=220)

        b6_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b6_1.place(x=500, y=620, width=220, height=40)

        # Developer Button
        img9 = Image.open("C:/attendence/college_image/developer.png")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b7 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b7.place(x=800, y=400, width=220, height=220)

        b7_1 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b7_1.place(x=800, y=620, width=220, height=40)

        # Exit Button
        img10 = Image.open("college_image/exit.jpeg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b8 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=root.destroy)
        b8.place(x=1100, y=400, width=220, height=220)

        b8_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white", command=root.destroy)
        b8_1.place(x=1100, y=620, width=220, height=40)


    # function to open image window
    def open_img(self):
        os.startfile("data")


        # functionality for buttons
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
            


    


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()
