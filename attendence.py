from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1532x840+0+0")  # Updated size to fit all images properly
        self.root.title("Attendance Management System")

        #variables
        self.var_atten_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendence=StringVar()

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
        title_lbl = Label(bg_img, text="Attendence", font=("times new roman", 35, "bold"), bg="black", fg="white") 
        title_lbl.place(x=0, y=0, width=1532, height=45)

        #frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=45, width=1532, height=665)

       # Left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", text="Attendence Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=750, height=610)

        # Load and resize image
        img_left = Image.open("C:/attendence/college_image/student_detail.jpg")
        img_left = img_left.resize((721, 130), Image.Resampling.LANCZOS)  # ✔️ resize and assign
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl2 = Label(left_frame, image=self.photoimg_left, bg="white")  # ✔️ use correct variable and parent
        f_lbl2.place(x=10, y=0, width=721, height=130)

        left_inside_frame = Frame(left_frame,relief=RAISED, bd=2, bg="white")
        left_inside_frame.place(x=5, y=135, width=730, height=400)


        #
        #Attendance  id
        attendence_id_label = Label(left_inside_frame, text="Attendance ID", font=("times new roman", 12, "bold"), bg="white")
        attendence_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        attendence_id_entry = ttk.Entry(left_inside_frame, font=("times new roman", 12, "bold"), textvariable=self.var_atten_id)
        attendence_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #roll 
        
        roll_no_label = Label(left_inside_frame, text="Roll no", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        roll_no_entry = ttk.Entry(left_inside_frame, font=("times new roman", 12, "bold"), textvariable=self.var_roll)
        roll_no_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #roll no
        name_label = Label(left_inside_frame, text="Name", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        name_entry = ttk.Entry(left_inside_frame, font=("times new roman", 12, "bold"), textvariable=self.var_name)
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        

        #department
        department_label = Label(left_inside_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        department_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        department_entry = ttk.Entry(left_inside_frame, font=("times new roman", 12, "bold"), textvariable=self.var_department)
        department_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #time
        time_label = Label(left_inside_frame, text="Time", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        time_entry = ttk.Entry(left_inside_frame, font=("times new roman", 12, "bold"), textvariable=self.var_time)
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #date
        date_label = Label(left_inside_frame, text="Date", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        date_entry = ttk.Entry(left_inside_frame, font=("times new roman", 12, "bold"), textvariable=self.var_date)
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #attendance status
        attendance_status_label = Label(left_inside_frame, text="Attendance Status", font=("times new roman", 12, "bold"), bg="white")
        attendance_status_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        attendance_status_combo = ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"), state="readonly", width=17, textvariable=self.var_attendence)
        attendance_status_combo["values"] = ("Status", "Present", "Absent")
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # buttons frame
        button_frame = Frame(left_inside_frame , bd=2, relief="raised", bg="white")
        button_frame.place(x=4, y=300, width=730, height= 30)

        # Save button
        save_button = Button(button_frame, text="Import csv",width=17, font=("times new roman", 11, "bold"), bg="gray", fg="white",command=self.import_csv)
        save_button.grid(row=0, column=0, padx=5, sticky=W)
        # Update button
        update_button = Button(button_frame, text="Export csv", width=17 ,font=("times new roman", 11, "bold"), bg="gray", fg="white",command=self.export_csv)
        update_button.grid(row=0, column=1, padx=5,  sticky=W)
        # Delete button
        delete_button = Button(button_frame, text="Update ", width=17 ,font=("times new roman", 11, "bold"), bg="gray", fg="white")
        delete_button.grid(row=0, column=2, padx=5,  sticky=W)
        # Reset button
        reset_button = Button(button_frame, text="Reset", width=17 ,font=("times new roman", 11, "bold"), bg="gray", fg="white",command=self.reset_data)
        reset_button.grid(row=0, column=3, padx=5, sticky=W)


        #right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=775, y=10, width=740, height=610)

        tabel_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        tabel_frame.place(x=5, y=5, width=720, height=550)

        #scroll bar
        scroll_x = ttk.Scrollbar(tabel_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tabel_frame, orient=VERTICAL)
        self.AttendenceReport = ttk.Treeview(tabel_frame, column=("id", "roll", "name", "department", "time", "date", "attendence"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendenceReport.xview)
        scroll_y.config(command=self.AttendenceReport.yview)
        
        self.AttendenceReport.heading("id", text="Attendance ID")
        self.AttendenceReport.heading("roll", text="Roll No")
        self.AttendenceReport.heading("name", text="Name")
        self.AttendenceReport.heading("department", text="Department")
        self.AttendenceReport.heading("time", text="Time")
        self.AttendenceReport.heading("date", text="Date")
        self.AttendenceReport.heading("attendence", text="Attendance Status")
        self.AttendenceReport["show"] = "headings"

        self.AttendenceReport.column("id", width=100)
        self.AttendenceReport.column("roll", width=150)
        self.AttendenceReport.column("name", width=100)
        self.AttendenceReport.column("department", width=120)
        self.AttendenceReport.column("time", width=100)
        self.AttendenceReport.column("date", width=100)
        self.AttendenceReport.column("attendence", width=150)

        self.AttendenceReport.pack(fill=BOTH, expand=1) 

        

        self.AttendenceReport.bind("<ButtonRelease>", self.get_cursor)
    

    #fetch data
    def fetch_data(self,rows):
        self.AttendenceReport.delete(*self.AttendenceReport.get_children())
        for i in rows:
            self.AttendenceReport.insert("", END, values=i)

    #import csv
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    #Export csv
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported", "Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)      


    #get cursor
    def get_cursor(self, event=""):
        cursor_row = self.AttendenceReport.focus()
        rows = self.AttendenceReport.item(cursor_row, 'values')
    
        if rows and len(rows) > 0:  # ✅ check before using rows
            self.var_atten_id.set(rows[0])
            self.var_atten_name.set(rows[1])
            self.var_atten_roll.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendence.set(rows[6])
        else:
            print("[DEBUG] No rows selected or empty data returned.")
          

    #reset data
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendence.set("")    
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()        