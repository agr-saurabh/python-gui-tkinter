# Tkinter is built in library of python
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()
    if email == "saurabh@gmail.com" and password == "1234":
        messagebox.showinfo("Congrats!!!", "Login Successful")
    else:
        messagebox.showerror("Error!!!", "Login Attempt Failed")

# creating object root of TK class
root = Tk()

root.title("Login Form")
root.iconbitmap("./img/gui_icon.ico")

# root.minsize(100, 100)

# set specific size of gui window
root.geometry("350x500")

root.configure(background = "#0096DC")


img = Image.open("./img/flipkart-logo.png")
img_resized = img.resize((70,70))
img = ImageTk.PhotoImage(img_resized)

img_label = Label(root, image = img)
img_label.pack(pady=(10,10)) # geometry manager, put on screen

text_label = Label(root, text = "Flipkart", fg="white", bg="#0096DC")
text_label.pack()
text_label.config(font=("verdana", 24))

email_label = Label(root, text = "Enter Email", fg="white", bg="#0096DC")
email_label.pack(pady=(20,5))
email_label.config(font=("verdana", 12))

email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1,15))

password_label = Label(root, text = "Enter Password", fg="white", bg="#0096DC")
password_label.pack(pady=(20,5))
password_label.config(font=("verdana", 12))

password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1,15))

login_btn = Button(root, text = "Login Here", fg="black", bg="white",
                   width=20, height=2, command=handle_login) # command defines btn function
login_btn.pack(pady=(10,20))
login_btn.config(font=("verdana",10))



# mainloop will keep gui consistently on screen
root.mainloop()