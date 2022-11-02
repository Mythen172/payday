from tkinter import *
from PIL import Image as PilImage
from PIL import ImageTk

class Child_window(Toplevel):
    def __init__(self, parent):

        super().__init__(parent)
        self.title("Создать новое расписание")
        self.iconbitmap(r"resources/oblozhka.ico")
        self.geometry('500x300')
        self.resizable(False, False)
        img = PilImage.open(r"resources\galochka.png")
        img = img.resize((40, 40), PilImage.ANTIALIAS)
        self.photo_image_g = ImageTk.PhotoImage(img)

        self.button_accept = Button(self, image=self.photo_image_g, width=60, height=60).place(x=224,y=205)
