from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="░D░E░V░E░L░O░P░E░R░", font=("times new roman", 35, "bold"), bg="White",
                          fg="Blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load and display the top image
        img_top = Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\dev.webp")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoImg_top = ImageTk.PhotoImage(img_top)

        f_lbl_top = Label(self.root, image=self.photoImg_top)
        f_lbl_top.place(x=0, y=55, width=1530, height=720)

        # Create a frame to hold the button
        self.button_frame = Frame(self.root, bg="white")
        self.button_frame.place(x=0, y=355, width=1530, height=45)  # Center the frame

        # Create a button to open the developer portfolio
        self.portfolio_button = Button(self.button_frame, text="𝔒𝔭𝔢𝔫_𝔇𝔢𝔳𝔢𝔩𝔬𝔭𝔢𝔯_𝔓𝔬𝔯𝔱𝔣𝔬𝔩𝔦𝔬", command=self.open_portfolio, font=("times new roman", 20, "bold"), bg="blue", fg="white")
        self.portfolio_button.pack(expand=True)# Use pack to center the button in the frame
        self.portfolio_button.place(x=0, y=0, width=1530, height=45)

    def open_portfolio(self):
        # Use the correct path to your HTML portfolio
        webbrowser.open(r"C:\Users\kamra\OneDrive\Desktop\Project work2\portfolio_kamran\portfolio.html")

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()