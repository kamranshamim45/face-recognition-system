from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

class HelpDesk:
    def __init__(self, root):
        print("Help Desk initialized")
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="ℍ𝔼𝕃ℙ 𝔻𝔼𝕊𝕂", font=("times new roman", 35, "bold"), bg="White", fg="Blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load and display the top image
        img_top = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\HELP_BG.jpeg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoImg_top = ImageTk.PhotoImage(img_top)

        f_lbl_top = Label(self.root, image=self.photoImg_top)
        f_lbl_top.place(x=0, y=55, width=1530, height=720)

        # Email link
        self.email_label = Label(f_lbl_top, text="Email: ", font=("times new roman", 20, "bold"), bg="white")
        self.email_label.place(x=450, y=220)

        self.email_link = Label(f_lbl_top, text="kamranshamim45@gmail.com", font=("times new roman", 20, "bold", "underline"), bg="white", fg="blue")
        self.email_link.place(x=550, y=220)
        self.email_link.bind("<Button-1>", self.open_email_client)

        # Buttons for additional features
        self.tutorial_button = Button(f_lbl_top, text="Open Tutorials", command=self.open_tutorials, font=("times new roman", 15, "bold"), bg="lightblue", fg="black")
        self.tutorial_button.place(x=450, y=300, width=200, height=50)

        self.feedback_button = Button(f_lbl_top, text="Feedback", command=self.open_feedback_form, font=("times new roman", 15, "bold"), bg="lightgreen", fg="black")
        self.feedback_button.place(x=700, y=300, width=200, height=50)

        self.chat_button = Button(f_lbl_top, text="Live Chat Support", command=self.open_chat, font=("times new roman", 15, "bold"), bg="lightcoral", fg="black")
        self.chat_button.place(x=950, y=300, width=200, height=50)

        self.knowledge_base_button = Button(f_lbl_top, text="Knowledge Base", command=self.open_knowledge_base, font=("times new roman", 15, "bold"), bg="lightyellow", fg="black")
        self.knowledge_base_button.place(x=450, y=370, width=700, height=50)

    def open_email_client(self, event):
        webbrowser.open("mailto:kamranshamim45@gmail.com")

    def open_tutorials(self):
        messagebox.showinfo("Tutorials", "Opening tutorials... (This would link to your tutorial section)")

    def open_feedback_form(self):
        messagebox.showinfo("Feedback", "Opening feedback form... (This would link to your feedback form)")

    def open_chat(self):
        messagebox.showinfo("Live Chat", "Opening live chat support... (This would link to your chat support)")

    def open_knowledge_base(self):
        messagebox.showinfo("Knowledge Base", "Opening knowledge base... (This would link to your knowledge base)")

if __name__ == "__main__":
    root = Tk()
    obj = HelpDesk(root)
    root.mainloop()