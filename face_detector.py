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
        button_recognize = Button(f_lbl, text="Start Face Recognition", cursor="hand2", font=("times new roman", 20, "bold"), bg="black", fg="white",command=self.recognize_faces)
        button_recognize.place(x=600, y=650, width=300, height=40)


    #face recognition function
    def recognize_faces(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text,clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

            coords = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 3)
                id, predict = clf.predict(gray_img[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Jayesh@24", database="face_detection")
                my_cursor = conn.cursor()

                my_cursor.execute("select student_name from student_info where Student_id ="+ str(id))
                n= my_cursor.fetchone() 
                n = "+".join(n)

                my_cursor.execute("select roll_no from student_info where Student_id ="+ str(id))
                r= my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select department from student_info where Student_id ="+ str(id))
                d= my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 77:
                    cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll No: {r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coords.append([x, y, w, h])

            return coords

        def recognize(img, clf, faceCascade):
            coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img         
                    
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Well Come to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break  
        video_cap.release()
        cv2.destroyAllWindows()


            
                

            




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()