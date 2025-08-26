from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x790+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="White", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load and display the top image
        self.load_top_image()

        # Load and display the bottom image
        self.load_bottom_image()

        # Button for Face Recognition
        b1_1 = Button(self.root, text="Face Recognition", cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="darkGreen", fg="white", command=self.face_recog)
        b1_1.place(x=650, y=600, width=250, height=40)

    def load_top_image(self):
        try:
            img_top = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\face_recognition2.jpg")
            img_top = img_top.resize((650, 700), Image.LANCZOS)
            self.photoImg_top = ImageTk.PhotoImage(img_top)

            f_lbl_top = Label(self.root, image=self.photoImg_top)
            f_lbl_top.place(x=0, y=55, width=650, height=700)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load top image: {e}")

    def load_bottom_image(self):
        try:
            img_bottom = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\face_recognition1.jpg")
            img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
            self.photoImg_bottom = ImageTk.PhotoImage(img_bottom)

            f_lbl_bottom = Label(self.root, image=self.photoImg_bottom)
            f_lbl_bottom.place(x=650, y=55, width=950, height=700)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load bottom image: {e}")
    # ===================Attandance System============================
    def mark_attendance(self,i,r,n,d):
        with open("kamran.csv","r+",newline="\n") as f:
            myDtataList=f.readlines()
            name_list=[]
            for line in myDtataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if(i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    def face_recog(self):
        print("Starting face recognition...")
        print("Loading classifier...")

        face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        if not video_cap.isOpened():
            print("Error: Could not open video capture.")
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to capture image")
                break
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
            features = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=10)

            if len(features) == 0:
                print("No faces detected")
                cv2.putText(img, "No Face Detected", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            else:
                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Draw green rectangle for detected face
                    id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                    confidence = int((100 * (1 - predict / 300)))

                    print(f"ID: {id}, Predict: {predict}, Confidence: {confidence}")  # Debugging output

                    # Check confidence level
                    if confidence > 70:  # Adjust this threshold as needed
                        try:
                            # Establish the database connection
                            conn = mysql.connector.connect(host="localhost", user="root", password="Kamran@123",
                                                           database="face_recogination")
                            my_cursor = conn.cursor()

                            # Fetch Name, Roll, and Department
                            my_cursor.execute("SELECT Name, Roll, Dep FROM student WHERE Student_id=%s", (id,))
                            result = my_cursor.fetchone()

                            my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=%s", (id,))
                            i = my_cursor.fetchone()
                            i = "+".join(i) if i else "Unknown ID"

                            if result:
                                n, r, d = result
                            else:
                                n, r, d = "Unknown Face", "Unknown Face", "Unknown Face"

                            # Close the cursor and connection
                            my_cursor.close()
                            conn.close()

                            # Display recognized information
                            cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),
                                        3)
                            cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),
                                        3)
                            cv2.putText(img, f"Dep: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            self.mark_attendance(i, r, n, d)
                        except mysql.connector.Error as err:
                            print(f"Database error: {err}")
                            cv2.putText(img, "DB Error", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)
                    else:
                        # Draw red rectangle for unknown face
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)  # Draw red rectangle
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()