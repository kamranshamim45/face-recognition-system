from tkinter import *
from tkinter import ttk, messagebox
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
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # Load and resize the background image
        try:
            img3 = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\bg_img.jpg")
            img3 = img3.resize((1530, 710), Image.LANCZOS)
            self.photoImg3 = ImageTk.PhotoImage(img3)
        except Exception as e:
            print(f"Error loading image: {e}")
            return  # Exit if the image cannot be loaded

        # Create a label for the background image
        bg_img = Label(self.root, image=self.photoImg3)
        bg_img.place(x=0, y=0, width=1530, height=710)

        # Create a title label
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkGreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, width=1500, height=600)

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=0, y=0, width=750, height=600)


        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0, y=0, width=820, height=700)

        # =============Labeled And Entry================
            #Attandance Label
        attendanceId_label=Label(left_inside_frame, text="AttendanceId", font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman", 12, "bold"))

        attendanceId_entry.grid(row=0, column=1, padx=10,pady=10, sticky=W)

          #Name_Label

        rollLabel = Label(left_inside_frame, text="Roll", font=("comicsansns", 11, "bold"),
                                   bg="white")
        rollLabel.grid(row=0, column=2, padx=10, sticky=W)

        atten_roll = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_roll,font=("comicsansns", 11, "bold"))

        atten_roll.grid(row=0, column=3, padx=10, pady=8, sticky=W)

        #Name_Label

        nameLabel = Label(left_inside_frame, text="Name", font=("comicsansns", 11, "bold"),
                                   bg="white")
        nameLabel.grid(row=1, column=0, padx=4,pady=8, sticky=W)

        atten_name = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name,font=("comicsansns", 11, "bold"))

        atten_name.grid(row=1, column=1, padx=10, pady=8, sticky=W)

        # Department

        depLabel = Label(left_inside_frame, text="Department", font=("comicsansns", 11, "bold"),
                          bg="white")
        depLabel.grid(row=1, column=2, padx=10, sticky=W)

        atten_dep = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_dep, font=("comicsansns", 11, "bold"))
        atten_dep.grid(row=1, column=3, padx=10, pady=8, sticky=W)

        # Time Label
        timeLabel = Label(left_inside_frame, text="Time", font=("comicsansns", 11, "bold"), bg="white")
        timeLabel.grid(row=2, column=0, padx=10, sticky=W)

        atten_time = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_time, font=("comicsansns", 11, "bold"))
        atten_time.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # Date Label
        dateLabel = Label(left_inside_frame, text="Date", font=("comicsansns", 11, "bold"), bg="white")
        dateLabel.grid(row=2, column=2, padx=10, sticky=W)

        atten_date = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date, font=("comicsansns", 11, "bold"))
        atten_date.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        # Attendance Status
        attendance_status_label = Label(left_inside_frame, text="Attendance Status",
                                        font=("times new roman", 12, "bold"), bg="white")
        attendance_status_label.grid(row=3, column=0, padx=10, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, width=20,textvariable=self.var_atten_attendance, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=520, width=750, height=40)

        save_btn = Button(btn_frame, text="Import CSV",command=self.importCsv, width=19, font=("times new roman", 13, "bold"), bg="blue",
                          fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export CSV",command=self.exportCsv,width=19, font=("times new roman", 13, "bold"), bg="Pink",
                            fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=19,command=self.update_data, font=("times new roman", 13, "bold"), bg="Dark Red",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=19,command=self.reset_data, font=("times new roman", 13, "bold"), bg="Red",
                           fg="white")
        reset_btn.grid(row=0, column=3)

        # Right Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=760, y=0, width=750, height=600)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=580)

        # =================Scroll Bar===============
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id", "roll","name", "department", "time", "date", "attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # Pack the Treeview
        self.AttendanceReportTable.pack(fill=BOTH, expand=True)

        # Configure the Treeview columns
        self.AttendanceReportTable.heading("id", text="ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable['show'] = 'headings'

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        # ======================Fetch dataa===================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

            #Import csv

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

            # Export csv

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
             export_write=csv.writer(myfile,delimiter=",")
             for i in mydata:
                export_write.writerow(i)
            messagebox.showinfo("Data Export","Your Data exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()  # Get the selected row
        content = self.AttendanceReportTable.item(cursor_row)  # Get the content of the selected row
        rows = content['values']  # Get the values from the row

        # Check if rows is not empty
        if rows:  # Proceed only if there are values
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6] if len(rows) > 6 else "")  # Check for attendance value
        else:
            # Optionally, clear the variables or set them to default values
            self.var_atten_id.set("")
            self.var_atten_roll.set("")
            self.var_atten_name.set("")
            self.var_atten_dep.set("")
            self.var_atten_time.set("")
            self.var_atten_date.set("")
            self.var_atten_attendance.set("")

            #Update Data

    # Add this method to your Attendance class
    def update_data(self):
        cursor_row = self.AttendanceReportTable.focus()  # Get the selected row
        if cursor_row:  # Check if a row is selected
            content = self.AttendanceReportTable.item(cursor_row)  # Get the content of the selected row
            rows = content['values']  # Get the values from the row

            # Update the selected row with the values from the entry fields
            updated_values = (
                self.var_atten_id.get(),
                self.var_atten_roll.get(),
                self.var_atten_name.get(),
                self.var_atten_dep.get(),
                self.var_atten_time.get(),
                self.var_atten_date.get(),
                self.var_atten_attendance.get()
            )

            # Update the Treeview
            self.AttendanceReportTable.item(cursor_row, values=updated_values)
            messagebox.showinfo("Success", "Data updated successfully", parent=self.root)
        else:
            messagebox.showwarning("Select Row", "Please select a row to update", parent=self.root)

    # In the __init__ method, update the button creation for the Update button



    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")












# Main execution
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()