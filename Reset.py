from tkinter import *
import mysql.connector
import pymysql
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk

 #init ************GUI****************************
window = Tk()
window.title("Reset Password")
window.resizable(False, False)

# photo
img = ImageTk.PhotoImage(file="ll.jpg")
label = Label(window, image=img)
label.pack()

# username label and entry box
user_label = Label(text="User Name", font=("courier", 12, "bold"), bg="white", fg="brown")
user_label.place(x=150, y=185)
user_entry = Entry(width=40, bg="#fdd1a7", fg="blue")
user_entry.place(x=150, y=210)

# email label and entry box
email_label = Label(text="Email", font=("courier", 12, "bold"), bg="white", fg="brown")
email_label.place(x=150, y=255)
email_entry = Entry(width=40, bg="#fdd1a7", fg="blue")
email_entry.place(x=150, y=280)

# password label and entry box
pwd_label = Label(text="Password", font=("courier", 12, "bold"), bg="white", fg="brown")
pwd_label.place(x=150, y=325)
pwd_entry = Entry(width=40, bg="#fdd1a7", fg="blue", show='*')
pwd_entry.place(x=150, y=350)

# confirm password label and entry box
con_label = Label(text="Confirm Password", font=("courier", 12, "bold"), bg="white", fg="brown")
con_label.place(x=150, y=395)
con_entry = Entry(width=40, bg="#fdd1a7", fg="blue", show='*')
con_entry.place(x=150, y=420)
''''
# Condition check
check = IntVar()  # This variable will store either (1)if you press or (0)if not.
terms_check = Checkbutton(root, text="I agree to the Terms & Conditions", font=("Arial", 10, "bold"),
                          bg="white", fg="brown", cursor="hand2", variable=check)
terms_check.place(x=150, y=465)
'''
#save
save_btn = Button(text="Save", width=11, font=("Arial", 9, "bold "), bg="brown",
                      fg="orange", bd=0,highlightbackground="white")
save_btn.place(x=230, y=480)
