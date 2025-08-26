
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from Attendance import Attendance
from developer import Developer
from help import HelpDesk


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Header images
        img = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\img1.png")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        img1 = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\img2.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        img2 = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\img3.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        img3 = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\background.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # =================Time==============

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font=("times new roman", 14, "bold"), bg="white", fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        # --- Buttons and Labels Section ---

        # Student button
        self.create_button(bg_img, "student details.jpg", "Student Details", 200, 100, self.student_details)

        # Face Detector
        self.create_button(bg_img, "face detector.jpg", "Face Detector", 500, 100,command=self.face_data)

        # Attendance
        self.create_button(bg_img, "Attandance.webp", "Attendance", 800, 100,command=self.Attendance_data)

        # Help Desk
        self.create_button(bg_img, "help desk.webp", "Help Desk", 1100, 100,command=self.help_data)

        # Train Data
        self.create_button(bg_img, "Train data.png", "Train Data", 200, 380,command=self.train_data)

        # Photos
        self.create_button(bg_img, "Photos.jpg", "Photos", 500, 380,command=self.open_img)

        # Developer
        self.create_button(bg_img, "Developer.jpeg", "Developer", 800, 380,command=self.developer_data)

        # Exit
        self.create_button(bg_img, "Exit.jpg", "Exit", 1100, 380,command=self.iExit)

    def create_button(self, parent, img_name, text, x, y, command=None):
        path = fr"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\{img_name}"
        image = Image.open(path)
        image = image.resize((220, 220), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        btn = Button(parent, image=photo, cursor="hand2", command=command)
        btn.image = photo  # Prevent garbage collection
        btn.place(x=x, y=y, width=220, height=220)
        btn_lbl = Button(parent, text=text, font=("times new roman", 15, "bold"), bg="darkblue", fg="white",
                         cursor="hand2", command=command)
        btn_lbl.place(x=x, y=y + 200, width=220, height=40)


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

        # ==================Function Button======================


    def open_img(self):
        os.startfile("Data")

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def Attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app=HelpDesk(self.new_window)
        
    
        
    # main.py




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
