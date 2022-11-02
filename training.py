from tkinter import *
from PIL import Image as PilImage
from PIL import ImageTk
from child_window import Child_window
from Check_time import checktime

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

        self.But_mon=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=0, padx=5)
        self.But_tue=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=1)
        self.But_Wed=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=2)
        self.But_the=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=3)
        self.But_fri=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=4)
        self.But_sut=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=5)
        self.But_sun=Button(image=self.photo_image, bg="#B3B1B1", relief="flat", cursor="hand2", command=self.open_window).grid(column=1, row=6)

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

if __name__ == "__main__":
    app = app()
    checktime()
    app.mainloop()