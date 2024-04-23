import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image


class NewsApp:

    def __init__(self):

        # fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&'
                                 'apiKey=e2ceab74395f4cc3ab1c115de6f521e7').json()

        # initial GUI load
        self.load_gui()

        # load the 1st news item
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry("350x600")
        self.root.resizable(0,0)
        self.root.title("News App")
        self.root.configure(background="black")

    def clear(self):
        # pack is a geometry manager which pick every item called slaves on root and destroy
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):
        # clear the screen for the new news item
        self.clear()

        # load image
        try:
            img_url = self.data['articles'][index]['urlToImage'] # fetch image from url
            raw_data = urlopen(img_url).read() # stores data in binary
            img = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(img) # display image
        except:
            img_url = 'https://thumbs.dreamstime.com/b/print-305144870.jpg' # image load error
            raw_data = urlopen(img_url).read() # stores data in binary
            img = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(img) # display image

        label = Label(self.root, image=photo)
        label.pack()

        # display heading
        heading = Label(self.root, text=self.data['articles'][index]['title'],
                        bg="black", fg="white", wraplength=350, justify="center")
        heading.pack(pady=(10,20))
        heading.config(font=("verdana", 15))

        # display details
        details = Label(self.root, text=self.data['articles'][index]['description'],
                        bg="black", fg="white", wraplength=350, justify="center")
        details.pack (pady=(2, 20))
        details.config (font=("verdana", 12))

        # creating buttons using frame
        frame = Frame(self.root, bg="black")
        frame.pack(expand=True, fill=BOTH)

        # show prev button for index>0
        if index != 0:
            prev = Button(frame, text="Prev", width=16, height=3,
                          command=lambda : self.load_news_item(index-1))
            prev.pack(side=LEFT)

        # Read more button - redirects to the original article
        read = Button (frame, text="Read More", width=16, height=3,
                       command=lambda : self.open_link(self.data['articles'][index]['url']))
        read.pack (side=LEFT)

        # show next button for index<len(data)
        if index != len(self.data['articles'])-1:
            next = Button (frame, text="Next", width=16, height=3,
                           command=lambda : self.load_news_item(index+1))
            next.pack (side=LEFT)

        self.root.mainloop ()

    def open_link(self, url):
        webbrowser.open(url)


onj = NewsApp()