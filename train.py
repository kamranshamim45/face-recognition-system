from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="White", fg="Blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load and display the top image
        img_top = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\train1.webp")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoImg_top = ImageTk.PhotoImage(img_top)

        f_lbl_top = Label(self.root, image=self.photoImg_top)
        f_lbl_top.place(x=0, y=55, width=1530, height=325)

        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="DarkRed", fg="White")
        b1_1.place(x=0, y=380, width=1530, height=60)

        # Load and display the bottom image
        img_bottom = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\peoples.jpg")
        img_bottom = img_bottom.resize((1530, 285), Image.LANCZOS)
        self.photoImg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl_bottom = Label(self.root, image=self.photoImg_bottom)
        f_lbl_bottom.place(x=0, y=440, width=1530, height=285)

    def train_classifier(self):
        Data_dir = "Data"
        path = [os.path.join(Data_dir, file) for file in os.listdir(Data_dir)]
        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L')  # Convert to grayscale
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])
  # Assuming filename format is user.id.jpg

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)  # Allow the window to update
            except Exception as e:
                print(f"Error loading image {image}: {e}")

        ids = np.array(ids)

        # Train classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.save("classifier.xml")  # Use save instead of write
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()