from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk
from tkcalendar import *
from tkinter.ttk import *

import pymysql
import mysql.connector


def connect_database():
    print('hello')


window = Tk()
window.title("Lab")
window.resizable(False, False)  # no zoom in/out window

background_Image = ImageTk.PhotoImage(file="ll.jpg")
background_label = Label(window, image=background_Image)
background_label.pack()

style = Style()
style.configure('TButton', font=('courier', 10, 'bold'),
                foreground='blue', width=9, cursor="hand", background="blue", fg="white")


# username label and entry box
user_label = Label(text="User Name", font=("courier", 12, "bold"))
user_label.place(x=150, y=210)
user_entry = Entry(width=40)
user_entry.place(x=150, y=230)

# password label and entry box
pwd_label = Label(text="Password", font=("courier", 12, "bold"))
pwd_label.place(x=150, y=270)
pwd_entry = Entry(width=40, show='*')
pwd_entry.place(x=150, y=290)

# confirm password label and entry box
con_label = Label(text="Confirm Password", font=("courier", 12, "bold"))
con_label.place(x=150, y=330)
con_entry = Entry(width=40, show='*')
con_entry.place(x=150, y=350)


save_btn = Button(text="Save", width=11, cursor="hand", style='TButton', command=window.destroy)
save_btn.place(x=310, y=410)


window.mainloop()