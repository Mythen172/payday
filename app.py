from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image as PilImage
from PIL import ImageTk
from datetime import datetime
import re

class app(Tk):
    def __init__(self):

        super().__init__()
        self.title("Создать новое расписание")
        self.geometry("1080x546+400+260")
        self.iconbitmap(r"resources/oblozhka.ico")
        self['bg'] = '#B3B1B1'
        img = PilImage.open(r"resources\plus.png")
        img = img.resize((40, 40), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

    def button_on_window(self):

        self.But_mon=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=0, padx=5)
        self.But_tue=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=1)
        self.But_Wed=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=2)
        self.But_fri=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=4)
        self.But_the=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=3)
        self.But_sut=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=5)
        self.But_sun=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=6)

    def label_on_window(self):

        Label(text="Понедельник", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=0)
        Label(text="Вторник", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=1)
        Label(text="Среда", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=2)
        Label(text="Четверг", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=3)
        Label(text="Пятница", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=4)
        Label(text="Суббота", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=5)
        Label(text="Воскресенье", font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=6)
        Label(font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=22, width=11).grid(column=0, row=7)

    def open_window(self):

        child = Child_window(self)
        child.grab_set()
        child.execute_accept()

class Child_window(Toplevel):

    def execute_accept(self, newval):
        return re.match("\d{0,5}$", newval) is not None

    def __init__(self, parent):

        super().__init__(parent)
        self.title("Создать новое расписание")
        self.iconbitmap(r"resources/oblozhka.ico")
        self.geometry('400x200+250+250')
        self.resizable(False, False)
        img = PilImage.open(r"resources\galochka.png")
        img = img.resize((40, 40), PilImage.ANTIALIAS)
        self.photo_image_g = ImageTk.PhotoImage(img)

        self.check = (self.register(self.execute_accept), "%P")

        self.button_accept = Button(self, image=self.photo_image_g, width=50, height=50, relief='flat', command=self.destroy).place(x=174,y=110)
        self.label = Label(self, font=('candara Bold', 15), width=20, height=7, text='Введите время через ":"').place(x=90, y=-70)
        self.entry = Entry(self, width=4, font=('candara Bold', 20), validate='key', validatecommand=self.check)
        self.entry.insert(2, ':')
        self.entry.pack(anchor=CENTER, pady=62)

class checktime:
    def __init__(self):

        self.now = datetime.now()
        self.w = self.now.weekday()+1
        self.h = self.now.hour
        self.m = self.now.minute

        if self.w == 2 and self.h == 13 and self.m == 35:
            print('jopa')

if __name__ == "__main__":
    App = app()
    App.label_on_window()
    App.button_on_window()
    checktime()
    App.mainloop()