from tkinter import *
from PIL import ImageTk, Image

# used to navigate through files and folders
import os

def rotate_img():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter += 1


# keep track of image
counter = 1

root = Tk()
root.title("Wallpaper Viewer")

root.geometry("250x400")
root.configure(background="black")

files = os.listdir("wallpapers")

img_array = []
for file in files:
    img = Image.open(os.path.join("wallpapers", file)) # complete path for each image
    img_resized = img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(img_resized)) # storing each image in array

img_label = Label(root, image=img_array[0]) # first image when gui loads
img_label.pack(pady=(15,10))

next_btn = Button(root, text="Next", fg="black", bg="white", width=28, height=2, command = rotate_img)
next_btn.pack()


root.mainloop()