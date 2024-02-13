# بسم الله الرحمن الرحيم

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
import pymysql
import mysql.connector


def imp_log():
    root.destroy()
    import login


def imp_medical():
    root.destroy()
    import medical


def clear():
    tst_entry.delete(0, END)
    dia_entry.delete(0, END)
    pre_entry.delete(0.0, END)
    cal_entry.delete(0, END)


# Database connection
def connect_database():
    if dia_entry.get() == '' or pre_entry.get(0.0, END) == '' or cal_entry.get() == '':
        messagebox.showerror('Warning ;)', 'Oh, You forgot to fill a field')
    else:
        try:
            # The Connection method of MySQL
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Q,u5.S@2',
                port='3306',
                database='doctor_table'
            )
            # A pointer
            my_cursor = mydb.cursor()
        except:
            messagebox.showerror('ERROR', 'Database Connectivity Issue, Please Try Again.')
            return
        query = 'INSERT INTO examination_data(id, patient_name, test_name, diagnose, prescription, diagnose_date)' \
                'VALUES(%s, %s, %s, %s, %s, %s)'
        my_cursor.execute(query, (id_entry.get(), pat_entry.get(), tst_entry.get(), dia_entry.get(),
                                  pre_entry.get(0.0, END), cal_entry.get()))
        mydb.commit()
        mydb.close()
        messagebox.showinfo('Success', 'Saving is done :)')


# GUI design.
root = Tk()
root.title("DOCTOR")
root.resizable(False, False)

# Inserting an image
bg_im = ImageTk.PhotoImage(file="doctor.png")
bg_la = Label(root, image=bg_im)
bg_la.pack()

# Patient Name.
pat_label = Label(text='Patient Name', font=('Georgia', 12), bg="white", fg="#4D3FF8")
pat_label.place(x=130, y=120)
pat_entry = Entry(root, relief="flat", width=40, bg="#c3d7df", fg="purple", highlightthickness=1,
                  highlightbackground="orange", highlightcolor="blue")
# pat_entry.insert(0, 'Ahmed')
# pat_entry.config(state='disabled')
pat_entry.place(x=130, y=150, height=22.5)

# Patient ID
id_label = Label(text='Patient ID', font=('Georgia', 12), bg="white", fg="#4D3FF8")
id_label.place(x=500, y=120)
id_entry = Entry(root, relief="flat", width=29, bg="#c3d7df", fg="purple", highlightthickness=1,
                 highlightbackground="orange", highlightcolor="blue")
# id_entry.insert(0, '1')
# id_entry.config(state='disabled')
id_entry.place(x=500, y=150, height=22.5)

# Test name
tst_label = Label(text='Test Name', font=('Georgia', 12), bg="white", fg="#4D3FF8")
tst_label.place(x=130, y=200)
tst_entry = Entry(root, relief="flat", width=40, bg="#c3d7df", fg="purple", highlightthickness=1,
                  highlightbackground="orange", highlightcolor="blue")
tst_entry.place(x=130, y=230, height=22.5)

# Diagnose name
dia_label = Label(text='Diagnose', font=('Georgia', 12), bg="white", fg="#4D3FF8")
dia_label.place(x=130, y=280)
dia_entry = Entry(root, relief="flat", width=40, bg="#c3d7df", fg="purple", highlightthickness=1,
                  highlightbackground="orange", highlightcolor="blue")
dia_entry.place(x=130, y=310, height=24)

# Prescription name
pre_label = Label(text='Prescription', font=('Georgia', 12), bg="white", fg="#4D3FF8")
pre_label.place(x=130, y=360)
pre_entry = Text(root, relief="flat", width=30, height=8, bg="#c3d7df", fg="purple", highlightthickness=1,
                 highlightbackground="orange", highlightcolor="blue")
pre_entry.place(x=130, y=390)

# The date
cal_label = Label(text='Date of Diagnose', font=('Georgia', 12), bg="white", fg="#4D3FF8")
cal_label.place(x=500, y=280)
cal_entry = DateEntry(root, width=30)
cal_entry.place(x=500, y=310)

# The medical history of the patient
his_btn = Button(text="Show Medical History", width=19, font=("Georgia", 10, 'bold'), borderwidth=1,
                 background="#6256F7", activebackground='orange', fg="white", cursor="hand2", command=imp_medical)
his_btn.place(x=500, y=200)

# the save button
save_btn = Button(text="Save", width=14, font=("Georgia", 10, 'bold'), borderwidth=1,
                  background="blue", activebackground='orange', fg="white", cursor="hand2", command=connect_database)
save_btn.place(x=130, y=570)

# The clear button
cle_btn = Button(text="Clear", width=14, font=("Georgia", 10, 'bold'), borderwidth=1,
                 background="#BDB77A", activebackground='orange', fg="white", cursor="hand2", command=clear)
cle_btn.place(x=130, y=650)

# The next button
nex_btn = Button(text="Next", width=14, font=("Georgia", 10, 'bold'), borderwidth=1,
                 background="#70E121", activebackground='orange', fg="white", cursor="hand2")
nex_btn.place(x=900, y=570)

# This button direct you into a page has all examination info
pri_btn = Button(text="Print a report", width=14, font=("Georgia", 10, 'bold'), borderwidth=1,
                 background="brown", activebackground='orange', fg="white", cursor="hand2")
pri_btn.place(x=900, y=650)

# The schedule of the button
sche_btn = Button(text="Schedule", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0)
sche_btn.place(x=3, y=208)

# The Log-out button
lout_btn = Button(text="Log out", width=9, font=("Arial", 9, 'bold'),
                  background="#fdd1a7", activebackground='#fdd1a7', fg="white", cursor="hand2", bd=0, command=imp_log)
lout_btn.place(x=3, y=635)

root.mainloop()
