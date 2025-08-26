from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        print("Save button clicked")
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # =======#variables=========
        self.var_Dep=StringVar()
        self.var_course=StringVar()
        self.var_Year=StringVar()
        self.var_Sem=StringVar()
        self.var_std_Id=StringVar()
        self.var_std_Name=StringVar()
        self.var_Div=StringVar()
        self.var_Roll=StringVar()
        self.var_Gender=StringVar()
        self.var_Dob=StringVar()
        self.var_Email=StringVar()
        self.var_Phone=StringVar()
        self.var_Address=StringVar()
        self.var_Teacher=StringVar()
        self.var_radio1 = StringVar()

        img=Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\student1.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoImg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoImg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img1 = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\student3.jpg")
        img1= img1.resize((500, 130), Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoImg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        img2 = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\student4.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoImg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        img3 = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\background.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoImg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoImg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="darkGreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)

        img_left = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\student2.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoImg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image=self.photoImg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        #Current Course

        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",
                                font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=115)
        #Department

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Dep,font=("times new roman", 12, "bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical","Management","B.tech")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course

        course_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=0, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly",width=20)
        course_combo["values"] = ("Select Course", "BCA", "MCA", "BBA", "MBA","B.COM","IT","BIOTECH")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #Year

        year_label = Label(current_course_frame, text='Year', font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Year, font=("times new roman", 12, "bold"), state="readonly",
                                    width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #Semester

        semester_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=0, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Sem, font=("times new roman", 12, "bold"), state="readonly",
                                  width=20)
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #Class Student Information
        class_Student_frame=LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                          font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=5, y=250, width=720, height=300)

        #student id

        studentId_label = Label(class_Student_frame, text="StudentID", font=("times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentId_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_Id,width=20,font=("times new roman", 12, "bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        # studentName

        studentName_label = Label(class_Student_frame, text="Student Name", font=("times new roman", 12, "bold"),
                                  bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_Name, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class division

        class_div_label = Label(class_Student_frame, text="Class Division", font=("times new roman", 12, "bold"),
                                bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        class_div_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_Div,font=("times new roman", 12, "bold"), state="readonly",
                                    width=18)
        class_div_combo["values"] = ("A", "B", "C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        #Roll No

        roll_no_label = Label(class_Student_frame, text="Roll No", font=("times new roman", 12, "bold"),
                              bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_Roll, width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #Gender

        gender_label = Label(class_Student_frame,text="Gender", font=("times new roman", 12, "bold"),
                                bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_Gender,
                                  font=("times new roman", 12, "bold"), state="readonly",
                                  width=18)
        gender_combo["values"] = ("Male", "Female", "Transgender")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #DOB

        dob_label = Label(class_Student_frame, text="D-O-B", font=("times new roman", 12, "bold"),
                                bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_Dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #Emai

        email_label = Label(class_Student_frame, text="Email", font=("times new roman", 12, "bold"),
                                bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_Email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        #phone no

        phone_label = Label(class_Student_frame, text="Phone No:", font=("times new roman", 12, "bold"),
                            bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        phone_entry = ttk.Entry(class_Student_frame,textvariable=self.var_Phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        #Address

        address_label = Label(class_Student_frame, text="Address", font=("times new roman", 12, "bold"),
                            bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_Address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)


        #Teacher name

        teacher_label = Label(class_Student_frame, text="Teacher Name", font=("times new roman", 12, "bold"),
                            bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_Teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="YES")
        radiobtn1.grid(row=6,column=0)


        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="No Photo Sample", value="NO")
        radiobtn2.grid(row=6, column=1)

        #button frame

        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0,column=0,)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="Pink", fg="white")
        update_btn.grid(row=0, column=1, )

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="Dark Red", fg="white")
        delete_btn.grid(row=0, column=2, )

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="Red", fg="white")
        reset_btn.grid(row=0, column=3, )

        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=230, width=715, height=35)

        take_photo_btn = Button(btn_frame1,command=self.generate_dataset, text="Take Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="Blue",
                           fg="white")
        take_photo_btn.grid(row=0, column=0, )

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35, font=("times new roman", 13, "bold"),
                                bg="Blue",
                                fg="white")
        update_photo_btn.grid(row=0, column=1, )


        # Right label frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        right_frame.place(x=780, y=10, width=760, height=580)

        img_right = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\student5.jpg")
        img_right = img_right.resize((720, 130), Image.LANCZOS)
        self.photoImg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoImg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        #Searching System

        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System ",
                                         font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=700, height=70)

        search_label=Label(search_frame,text="Search By:", font=("times new roman", 12, "bold"),
                            bg="Red",fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="readonly",
                                      width=15)
        search_combo["values"] = (
        "Select", "Roll-No", "Phone-No","D-O-B","Student Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=14, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=12, font=("times new roman", 12, "bold"), bg="Dark Red",
                            fg="white")
        search_btn.grid(row=0, column=3,padx=4 )

        showAll_btn = Button(search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="Red",
                           fg="white")
        showAll_btn.grid(row=0, column=4,padx=4 )

        # ========table frame==================

        table_frame=Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=700, height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Dep","course","Year","Sem","Id","Name","Div","Roll","Gender","Dob","Email","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Id", text="Student Id")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Roll", text="Roll")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Div", text="Division")
        self.student_table.heading("Dob", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("Photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("Id", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Roll", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Div", width=100)
        self.student_table.column("Dob", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Teacher", width=100)
        self.student_table.column("Photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        # =========function declaration===========

    def add_data(self):

        print("Add Data method called")
        if self.var_Dep.get() == "Select Department" or self.var_std_Name.get() == "" or self.var_std_Id.get() == "" or self.var_Year.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Kamran@123",
                                               database="face_recogination")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                        self.var_Dep.get(),
                        self.var_course.get(),
                        self.var_Year.get(),
                        self.var_Sem.get(),
                        self.var_std_Id.get(),
                        self.var_std_Name.get(),
                        self.var_Div.get(),
                        self.var_Roll.get(),
                        self.var_Gender.get(),
                        self.var_Dob.get(),
                        self.var_Email.get(),
                        self.var_Phone.get(),
                        self.var_Address.get(),
                        self.var_Teacher.get(),
                        self.var_radio1.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
                # ============fetch data=========

    def fetch_data(self):
                    try:
                        conn = mysql.connector.connect(host="localhost", user="root", password="Kamran@123",
                                                       database="face_recogination")
                        my_cursor=conn.cursor()
                        my_cursor.execute("SELECT * FROM student")
                        data = my_cursor.fetchall()

                        if len(data) != 0:
                            self.student_table.delete(*self.student_table.get_children())
                            for i in data:
                                self.student_table.insert("", END, values=i)
                        conn.close()  # Close the connection after fetching data
                    except Exception as es:
                        messagebox.showerror("Error", f"Could not fetch data: {str(es)}", parent=self.root)

                  #get cursor

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()

        # Check if an item is selected
        if cursor_focus:
            content = self.student_table.item(cursor_focus)
            data = content["values"]

            # Check if data has the expected number of elements
            if len(data) >= 15:  # Adjust this number based on your actual data structure
                self.var_Dep.set(data[0])
                self.var_course.set(data[1])
                self.var_Year.set(data[2])
                self.var_Sem.set(data[3])
                self.var_std_Id.set(data[4])
                self.var_std_Name.set(data[5])
                self.var_Div.set(data[6])
                self.var_Roll.set(data[7])
                self.var_Gender.set(data[8])
                self.var_Dob.set(data[9])
                self.var_Email.set(data[10])
                self.var_Phone.set(data[11])
                self.var_Address.set(data[12])
                self.var_Teacher.set(data[13])
                self.var_radio1.set(data[14])
            else:
                messagebox.showwarning("Warning", "Selected data is incomplete.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "No item selected.", parent=self.root)

        # update function

    def update_data(self):
        print("Update button clicked")
        if self.var_Dep.get() == "Select Department" or self.var_std_Name.get() == "" or self.var_std_Id.get() == "" or self.var_Year.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Kamran@123",
                                                   database="face_recogination")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student SET Dep=%s, course=%s, Year=%s, Semester=%s,Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
                        (
                            self.var_Dep.get(),
                            self.var_course.get(),
                            self.var_Year.get(),
                            self.var_Sem.get(),
                            self.var_std_Name.get(),
                            self.var_Div.get(),  # Corrected this line
                            self.var_Roll.get(),
                            self.var_Gender.get(),
                            self.var_Dob.get(),
                            self.var_Email.get(),
                            self.var_Phone.get(),
                            self.var_Address.get(),
                            self.var_Teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_Id.get(),

                        ))
                    conn.commit()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                    self.fetch_data()
                    conn.close()
                else:
                    if not update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
                # Delete Function
    def delete_data(self):
                    if self.var_std_Id.get() == "":
                        messagebox.showerror("Error", "Student ID must be required", parent=self.root)
                    else:
                        try:
                            delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?",
                                                         parent=self.root)
                            if delete:  # If the user clicks "Yes"
                                conn = mysql.connector.connect(host="localhost", user="root", password="Kamran@123",
                                                               database="face_recogination")
                                my_cursor = conn.cursor()
                                sql = "DELETE FROM student WHERE Student_id = %s"
                                val = (self.var_std_Id.get(),)
                                my_cursor.execute(sql, val)

                                conn.commit()  # Commit the changes
                                self.fetch_data()  # Refresh the data
                                conn.close()  # Close the connection
                                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
                            else:
                                return  # If the user clicks "No", simply return
                        except Exception as es:
                            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
                #Reset data
    def reset_data(self):
        self.var_Dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_Year.set("Select year")
        self.var_Sem.set("Select Semester")
        self.var_std_Id.set("")
        self.var_std_Name.set("")
        self.var_Div.set("")
        self.var_Roll.set("")
        self.var_Gender.set("")
        self.var_Dob.set("")
        self.var_Email.set("")
        self.var_Phone.set("")
        self.var_Address.set("")
        self.var_Teacher.set("")
        self.var_radio1.set("")


        # Generate data set Take photo sample

    def generate_dataset(self):
        if self.var_Dep.get() == "Select Department" or self.var_std_Name.get() == "" or self.var_std_Id.get() == "" or self.var_Year.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Connect to the database
                conn = mysql.connector.connect(host="localhost", user="root", password="Kamran@123",
                                               database="face_recogination")
                my_cursor = conn.cursor()

                # Fetch all student records
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                id = 0

                # Get the current highest ID
                for x in myresult:
                    id += 1

                # Update the student record
                my_cursor.execute(
                    "UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
                    (
                        self.var_Dep.get(),
                        self.var_course.get(),
                        self.var_Year.get(),
                        self.var_Sem.get(),
                        self.var_Div.get(),
                        self.var_Roll.get(),
                        self.var_Gender.get(),
                        self.var_Dob.get(),
                        self.var_Email.get(),
                        self.var_Phone.get(),
                        self.var_Address.get(),
                        self.var_Teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_Id.get()  # Corrected this line
                    )
                )
                conn.commit()  # Commit the changes
                self.fetch_data()  # Refresh the data
                self.reset_data()  # Reset the input fields
                conn.close()  # Close the connection

                # Load predefined data face frontals from OpenCV
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        return img[y:y + h, x:x + w]  # Return the cropped face

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"Data/user.{id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or img_id == 50:  # Break on Enter key or after 100 images
                        break

                cap.release()  # Release the video capture
                cv2.destroyAllWindows()  # Close all OpenCV windows
                messagebox.showinfo("Result", "Generating data sets completed!!!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)






if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()