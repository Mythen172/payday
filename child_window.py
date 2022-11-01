from tkinter import *
from PIL import Image as PilImage
from PIL import ImageTk

class Child_window:
    def __init__(self, parent, label, width=1080, height=546, resizable=(False, False), title = "Создать новое расписание", icon=r"resources/oblozhka.ico"):

        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+400+260")
        self.root.iconbitmap(icon)
        self.root.resizable(resizable[0], resizable[1])
        self.label = label
        img = PilImage.open(r"resources\plus.png")
        img = img.resize((40, 40), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)
        self.label = Label(bg="red",width=100,height=100).grid(column=0,row=0)