from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from face_recognition import Face_Recognition


class Login_Window:
   def __init__(self,root):
      self.root = root
      self.root.title("Login")
      self.root.geometry("1550x800+0+0")

      # Background image
      self.bg=ImageTk.PhotoImage(file=r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\loginimg.jpg")
      lbl_bg=Label(self.root,image=self.bg)
      lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

      # Title label
      frame=Frame(self.root,bg="black")
      frame.place(x=610,y=170,width=340,height=450)
      
      img1=Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\loginicon.png")
      img1=img1.resize((100,100),Image.LANCZOS)
      self.photoimage=ImageTk.PhotoImage(img1)
      lblimg1=Label(image=self.photoimage,bg="black",borderwidth=0)
      lblimg1.place(x=730,y=175,width=100,height=100)
      

      get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
      get_str.place(x=95,y=100)
      
      # Label and entry for username
      username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
      username.place(x=70,y=155)
      self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
      self.txtuser.place(x=40,y=185,width=270)
      # Label and entry for password
      password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
      password.place(x=70,y=225)
      self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
      self.txtpass.place(x=40,y=255,width=270)
      
      #Icon image
      img2=Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\userimg.webp")
      img2=img2.resize((25,25),Image.LANCZOS)
      self.photoimagebtn=ImageTk.PhotoImage(img2)
      lblimg1=Label(image=self.photoimagebtn,bg="black",borderwidth=0)
      lblimg1.place(x=650,y=323,width=25,height=25)
      
      #Icon image
      img3=Image.open(r"C:\Users\kamra\OneDrive\Desktop\Face Reconition System\Images\passwordimg.jpg")
      img3=img3.resize((25,25),Image.LANCZOS)
      self.photoimage3=ImageTk.PhotoImage(img3)
      lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
      lblimg1.place(x=650,y=395,width=25,height=25)
      
      # Login button
      loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RAISED,fg="white",bg="green",activeforeground="white",activebackground="green")
      loginbtn.place(x=110,y=300,width=120,height=35)
      
      # Register button
      registerbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
      registerbtn.place(x=15,y=350,width=160)
     
      # forget password button
      
      # Login button
      forgetbtn=Button(frame,text="Forget",font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
      forgetbtn.place(x=10,y=370,width=160)
      
   def login(self):
      if self.txtuser.get()=="" or self.txtpass.get()=="":
         messagebox.showerror("Error","All fields are required")
      elif self.txtuser.get()=="admin" and self.txtpass.get()=="12345":
         messagebox.showinfo("Success","Welcome to our Face Recognition System")
         self.root.destroy()
         from main import Face_Recognition_System
         main_root = Tk()
         app = Face_Recognition_System(main_root)
         main_root.mainloop()
      else:
         messagebox.showerror("Invalid","Username or Password is incorrect")
         
      
  
if __name__=="__main__":
   root=Tk()
   app=Login_Window(root)
   root.mainloop()
  