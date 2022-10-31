import winsound
import os
from tkinter import *
from PIL import Image as PilImage
from PIL import ImageTk

class Window:
    def __init__(self, width=1080, height=546, title = "Звонки по расписанию", icon=r"resources/oblozhka.ico"):

        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+400+260")
        self.root.iconbitmap(icon)
        img = PilImage.open(r"resources\plus.png")
        img = img.resize((40, 40), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

    def Label_bg_days_buttons(self):

        Label(font=("candara Bold", 15), bg="#B3B1B1", relief="flat", borderwidth=3, height=44, width=337).place(x=127)
        Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2").grid(column=1, row=0, padx=5)
        Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2").grid(column=1, row=1)
        Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2").grid(column=1, row=2)
        Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2").grid(column=1, row=3)
        Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2").grid(column=1, row=4)
        Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2").grid(column=1, row=5)
        Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2").grid(column=1, row=6)

    def Label_days(self):

        Label(text="Понедельник", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=0)
        Label(text="Вторник", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=1)
        Label(text="Среда", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=2)
        Label(text="Четверг", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=3)
        Label(text="Пятница", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=4)
        Label(text="Суббота", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=5)
        Label(text="Воскресенье", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=6)
        Label(font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=22, width=11).grid(column=0, row=7)

    def run(self):
        self.Label_days()
        self.Label_bg_days_buttons()
        self.root.mainloop()

if __name__ == "__main__":
    window = Window()
    window.run()