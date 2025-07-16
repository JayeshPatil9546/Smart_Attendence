from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1532x840+0+0")  # Updated size to fit all images properly
        self.root.title("Student Management System")


        #Variable declaration
        self.var_department = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_student_id = StringVar()
        self.var_student_name = StringVar()
        self.var_class_division = StringVar()
        self.var_roll_no = StringVar()
        self.var_phone_no = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_teacher_name = StringVar()
        self.var_birth_date = StringVar()
        self.var_gender = StringVar()
        self.var_photo_sample = StringVar()
       

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
        title_lbl = Label(bg_img, text="Student Management System", font=("times new roman", 35, "bold"), bg="black", fg="white") 
        title_lbl.place(x=0, y=0, width=1532, height=45)


        #frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=45, width=1532, height=665)

       # Left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=750, height=610)

        # Load and resize image
        img_left = Image.open("C:/attendence/college_image/student_detail.jpg")
        img_left = img_left.resize((721, 130), Image.Resampling.LANCZOS)  # ✔️ resize and assign
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl2 = Label(left_frame, image=self.photoimg_left, bg="white")  # ✔️ use correct variable and parent
        f_lbl2.place(x=10, y=0, width=721, height=130)

        #current cource
        current_cource_frame = LabelFrame(left_frame, bd=2, bg="white", text="Current cource", font=("times new roman", 12, "bold"))
        current_cource_frame.place(x=5, y=135, width=740, height=115)

        #department
        dep_label = Label(current_cource_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(current_cource_frame,textvariable=self.var_department, font=("times new roman", 12, "bold"), state='readonly')
        dep_combo['values'] = ("Select Department", "Computer ", "Information Technology", "Data Science", "AI")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #course
        course_label = Label(current_cource_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        course_combo = ttk.Combobox(current_cource_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), state='readonly')
        course_combo['values'] = ("Select Course", "BCA", "IMCA", "MCA", "BBA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #year
        year_label = Label(current_cource_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        year_combo = ttk.Combobox(current_cource_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), state='readonly')
        year_combo['values'] = ("Select Year", "2021", "2022", "2023", "2024")
        year_combo.current(0)
        year_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #semester        
        semester_label = Label(current_cource_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        semester_combo = ttk.Combobox(current_cource_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), state='readonly')
        semester_combo['values'] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semester 4")
        semester_combo.current(0)
        semester_combo.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        #class student information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", text="Class Student Information ", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=740, height=335)

        #student id
        student_id_label = Label(class_student_frame, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        student_id_entry = ttk.Entry(class_student_frame,textvariable=self.var_student_id, font=("times new roman", 12, "bold"))
        student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #student name
        student_name_label = Label(class_student_frame, text="Student Name", font=("times new roman", 12, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_student_name, font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #class division
        class_division_label = Label(class_student_frame, text="Class Division", font=("times new roman", 12, "bold"), bg="white")
        class_division_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        #class_division_entry = ttk.Entry(class_student_frame,textvariable=self.var_class_division, font=("times new roman", 12, "bold"))
        #class_division_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        class_division_combo = ttk.Combobox(class_student_frame,textvariable=self.var_class_division, font=("times new roman", 12, "bold"), state='readonly',width=18)
        class_division_combo['values'] = ("Select Division", "A", "B", "C", "D")
        class_division_combo.current(0)
        class_division_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        #Roll no
        student_roll_label = Label(class_student_frame, text="Roll No", font=("times new roman", 12, "bold"), bg="white")
        student_roll_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        student_roll_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll_no, font=("times new roman", 12, "bold"))
        student_roll_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #gender
        student_gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 12, "bold"), bg="white")
        student_gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        #student_gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_gender,font=("times new roman", 12, "bold"))
        #student_gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        student_gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender, font=("times new roman", 12, "bold"), state='readonly',width=18)
        student_gender_combo['values'] = ("Select Gender", "Male", "Female", "Other")
        student_gender_combo.current(0)
        student_gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #email
        student_email_label = Label(class_student_frame, text="Email", font=("times new roman", 12, "bold"), bg="white")
        student_email_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        student_email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, font=("times new roman", 12, "bold"))
        student_email_entry.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        #phone no
        student_phone_label = Label(class_student_frame, text="Phone No", font=("times new roman", 12, "bold"), bg="white")
        student_phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        student_phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone_no, font=("times new roman", 12, "bold"))
        student_phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        #address
        student_address_label = Label(class_student_frame, text="Address", font=("times new roman", 12, "bold"), bg="white")
        student_address_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        student_address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address, font=("times new roman", 12, "bold"))
        student_address_entry.grid(row=3, column=3, padx=2, pady=10, sticky=W)

        #teacher name
        teacher_name_label = Label(class_student_frame, text="Teacher Name", font=("times new roman", 12, "bold"), bg="white")
        teacher_name_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        teacher_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher_name,font=("times new roman", 12, "bold"))
        teacher_name_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        #Date of Birth
        dob_label = Label(class_student_frame, text="Date of Birth", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_birth_date, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=4, column=3, padx=2, pady=10, sticky=W)

        # redio buttons
        self.var_radio = StringVar()

        radiobutton = ttk.Radiobutton(class_student_frame, text="Take Photo Sample", variable=self.var_radio, value="Yes")
        radiobutton.grid(row=6, column=0, padx=5, pady=2, sticky=W)

        radiobutton1 = ttk.Radiobutton(class_student_frame, text="No Photo Sample", variable=self.var_radio, value="No")
        radiobutton1.grid(row=6, column=1, padx=5, pady=2, sticky=W)


        # buttons frame
        button_frame = Frame(class_student_frame, bd=2, relief="raised", bg="white")
        button_frame.place(x=4, y=250, width=730, height= 30)

        # Save button
        save_button = Button(button_frame, text="Save",width=17, font=("times new roman", 11, "bold"), bg="gray", fg="white",command=self.add_data)
        save_button.grid(row=0, column=0, padx=5, sticky=W)
        # Update button
        update_button = Button(button_frame, text="Update", width=17 ,font=("times new roman", 11, "bold"), bg="gray", fg="white",command=self.update_data)
        update_button.grid(row=0, column=1, padx=5,  sticky=W)
        # Delete button
        delete_button = Button(button_frame, text="Delete", width=17 ,font=("times new roman", 11, "bold"), bg="gray", fg="white")
        delete_button.grid(row=0, column=2, padx=5,  sticky=W)
        # Reset button
        reset_button = Button(button_frame, text="Reset", width=17 ,font=("times new roman", 11, "bold"), bg="gray", fg="white")
        reset_button.grid(row=0, column=3, padx=5, sticky=W)

        # buttons frame
        button_frame1 = Frame(class_student_frame, bd=2, relief="raised", bg="white")
        button_frame1.place(x=4, y=280, width=730, height= 30)

        # Take Photo button
        take_photo_button = Button(button_frame1, text="Take Photo Sample", width=36, font=("times new roman", 11, "bold"), bg="gray", fg="white")
        take_photo_button.grid(row=0, column=0, padx=5, sticky=W)
        # Update Photo button
        update_photo_button = Button(button_frame1, text="Update Photo Sample", width=36, font=("times new roman", 11, "bold"), bg="gray", fg="white")
        update_photo_button.grid(row=0, column=1, padx=5, sticky=W)


        #right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=775, y=10, width=740, height=610)

         # Load and resize image
        img_right = Image.open("C:/attendence/college_image/data.jpg")
        img_right = img_right.resize((721, 130), Image.Resampling.LANCZOS)  # ✔️ resize and assign
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl2 = Label(right_frame, image=self.photoimg_right, bg="white")  # ✔️ use correct variable and parent
        f_lbl2.place(x=10, y=0, width=721, height=130)

        # Search frame
        search_frame = LabelFrame(right_frame, bd=2, bg="white",relief="ridge", text="Search Student", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=730, height=70)

        search_label = Label(search_frame, text="Search By", font=("times new roman", 12, "bold"), bg="red")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state='readonly')
        search_combo['values'] = ("Select", "Roll No", "Phone No", "Email")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_button = Button(search_frame, text="Search", width=10, font=("times new roman", 11, "bold"), bg="gray", fg="white")
        search_button.grid(row=0, column=3, padx=5, sticky=W)

        show_all_button = Button(search_frame, text="Show All", width=10, font=("times new roman", 11, "bold"), bg="gray", fg="white")
        show_all_button.grid(row=0, column=4, padx=5, sticky=W)

        # Table frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief="ridge")
        table_frame.place(x=5, y=210, width=730, height=375)

        # Scroll bars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
       
        self.student_table = ttk.Treeview(table_frame, columns=("department", "course", "year", "semester", "student_id", "student_name", "class_division", "roll_no", "phone_no", "email", "address", "teacher_name", "birth_date","gender","photo_sample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("student_id", text="Student ID")
        self.student_table.heading("student_name", text="Student Name")
        self.student_table.heading("class_division", text="Class Division")
        self.student_table.heading("roll_no", text="Roll No")
        self.student_table.heading("phone_no", text="Phone No")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher_name", text="Teacher Name")
        self.student_table.heading("birth_date", text="Birth Date")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("photo_sample", text="Photo Sample")
        self.student_table['show'] = 'headings'

        self.student_table.column("department", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("student_id", width=100)
        self.student_table.column("student_name", width=100)
        self.student_table.column("class_division", width=100)
        self.student_table.column("roll_no", width=100)
        self.student_table.column("phone_no", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher_name", width=100)
        self.student_table.column("birth_date", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("photo_sample", width=100)


        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fatch_data()

    #function declaration
    def add_data(self):
        if self.var_department.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
            # Connect to the database
                conn = mysql.connector.connect(host="localhost", user="root", password="Jayesh@24", database="face_detection")
                cursor = conn.cursor()  
                cursor.execute("""
                    INSERT INTO student_info (
                        department, course, year, semester, student_id,
                        student_name, class_division, roll_no, phone_no,
                        email, address, teacher_name, birth_date, gender, photo_sample           
                    )                                                      
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_student_id.get(),
                    self.var_student_name.get(),
                    self.var_class_division.get(),
                    self.var_roll_no.get(),
                    self.var_phone_no.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_teacher_name.get(),
                    self.var_birth_date.get(),
                    self.var_gender.get(),
                    self.var_radio.get()
                ))
                conn.commit()
                self.fatch_data()  # Refresh the table after adding data
                conn.close()
                messagebox.showinfo("Success", "Student details added successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)    

    # fetch data from database and show in table
    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Jayesh@24", database="face_detection")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student_info")
        data = cursor.fetchall()

        if len(data) != 0:  # ✅ now it means "if data is present"
            self.student_table.delete(*self.student_table.get_children())  # clear old data
            for row in data:
                self.student_table.insert('', END, values=row)
        
        conn.close()

    #get cursor 
    def get_cursor(self, event=""):    
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']

        self.var_department.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_student_id.set(data[4])
        self.var_student_name.set(data[5])
        self.var_class_division.set(data[6])
        self.var_roll_no.set(data[7])
        self.var_phone_no.set(data[8])
        self.var_email.set(data[9])
        self.var_address.set(data[10])
        self.var_teacher_name.set(data[11])
        self.var_birth_date.set(data[12])
        self.var_gender.set(data[13])
        self.var_radio.set(data[14])



    # update data function
    def update_data(self):
        if self.var_department.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                update=messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Jayesh@24", database="face_detection")
                    cursor = conn.cursor()
                    cursor.execute("""
                    UPDATE student_info SET
                        department=%s, course=%s, year=%s, semester=%s,
                        student_name=%s, class_division=%s, roll_no=%s,
                        phone_no=%s, email=%s, address=%s,
                        teacher_name=%s, birth_date=%s , gender=%s, photo_sample=%s where student_id=%s """, ( 
                        self.var_department.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_student_name.get(),
                        self.var_class_division.get(),
                        self.var_roll_no.get(),
                        self.var_phone_no.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_teacher_name.get(),
                        self.var_birth_date.get(),
                        self.var_gender.get(),
                        self.var_radio.get(),
                        self.var_student_id.get()
                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                conn.commit()
                self.fatch_data()  # Refresh the table after updating data
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)
            





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()