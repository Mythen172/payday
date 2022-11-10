from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image as PilImage
from PIL import ImageTk
from datetime import datetime
import re

days_ru = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
days_en = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

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

        for i in range(len(days_en)):
            self.day = days_en[i]
            self.day=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=lambda jopa=days_en[i]: self.add_newcell(jopa)).grid(column=1, row=i, padx=5)
            i=+i

    def label_on_window(self):

        for i in range(len(days_ru)): 
            Label(text=days_ru[i], font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=3, width=11).grid(column=0, row=i)
            i=+i

        Label(font=("candara Bold", 15), bg="#48B3C9", relief="flat", borderwidth=2, height=22, width=11).grid(column=0, row=7)

    def add_newcell(self, jopa):
            print(jopa)

            def open_window(self):
                child = Child_window(self)
                child.grab_set()
                child.execute_accept()

class Child_window(Toplevel):

    def execute_accept(self, newval):
        return re.match("\d{0,2}$", newval) is not None

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
        self.entry = Entry(self, width=2, font=('candara Bold', 20), validate='key', validatecommand=self.check).pack(anchor=W, padx=150, pady=62)
        self.entry1 = Entry(self, width=2, font=('candara Bold', 20), validate='key', validatecommand=self.check).pack(anchor=E,padx=50, pady=62)

class checktime:
    def __init__(self):

        self.now = datetime.now()
        self.w = self.now.weekday()+1
        self.h = self.now.hour
        self.m = self.now.minute

        if self.w == 4 and self.h == 22 and self.m == 37:
            print('jopa')

if __name__ == "__main__":
    App = app()
    App.label_on_window()
    App.button_on_window()
    checktime()
    App.mainloop()