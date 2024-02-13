# بسم الله الرحمن الرحيم

from tkinter import *

# from tkinter.ttk import Combobox
from PIL import ImageTk
from tkcalendar import *
from tkinter.ttk import *

# import pymysql
# import mysql.connector


# def connect_database():


def calender():
    window.destroy()
    import Nurse


def lab():
    print('helo')





def login_page():
    window.destroy()
    import login


window = Tk()
window.title("NURSE")
window.resizable(False, False)  # no zoom in/out window

# Inserting an image
background_Image = ImageTk.PhotoImage(file="nurse.png")
background_label = Label(window, image=background_Image)
background_label.pack()

style = Style()
style.configure('TButton', font=('calibri', 10, 'bold'),
                foreground='red', width=9, cursor="hand", background="red", fg="white")

# ---------------------- Main buttons ----------------------

Appointments_btn = Button(text="Calender", style='TButton', width=7, command=calender)
Appointments_btn.place(x=-10, y=183)

lap_btn = Button(text="lab", width=5, style='TButton', command=lab)
lap_btn.place(x=2, y=408)

logout_btn = Button(text="logout", width=5, style='TButton', command=login_page)
logout_btn.place(x=2, y=638)

# ---------------------- Main patient info ----------------------


Patient_name = Label(text='Patient Name ', font=('Georgia', 12), background='white',
                     style=style.configure('TEntry', bd='0', exportselection=0,
                                           selectbackground='red', selectborderwidth='red'))
Patient_name.place(x=130, y=120)
Patient_name_input = Entry(width=25)
Patient_name_input.insert(0, 'Ayman')
Patient_name_input.config(state='disabled')
Patient_name_input.place(x=130, y=150)

Patient_phone = Label(text='Patient Phone ', font=('Georgia', 12), background='white')
Patient_phone.place(x=130, y=190)
Patient_phone_input = Entry(width=25)
Patient_phone_input.insert(0, '01060188385')
Patient_phone_input.config(state='disabled')
Patient_phone_input.place(x=130, y=210)

Age = Label(text='Age ', font=('Georgia', 12), background='white')
Age.place(x=130, y=250)
Age_input = Entry(width=25)
Age_input.insert(0, '19')
Age_input.config(state='disabled')
Age_input.place(x=130, y=280)

Gender = Label(text='Gender ', font=('Georgia', 12), background='white')
Gender.place(x=130, y=320)
Gender_input = Combobox(width=25, values=['Male', 'Female'])
Gender_input.insert(0, 'Male')
Gender_input.config(state='disabled')
Gender_input.place(x=130, y=350)

Payment = Label(text='Payment ', font=('Georgia', 12), background='white')
Payment.place(x=130, y=390)
Payment_input = Entry(width=25)
Payment_input.insert(0, 'Cash')

Payment_input.config(state='disabled')
Payment_input.place(x=130, y=420)

Total_Bill = Label(text='Total Bill ', font=('Georgia', 12), background='white')
Total_Bill.place(x=130, y=460)
Total_Bill_input = Entry(width=25)
Total_Bill_input.place(x=130, y=490)

Remainder = Label(text='Remainder ', font=('Georgia', 12), background='white')
Remainder.place(x=130, y=530)
Remainder_input = Entry(width=25)
Remainder_input.place(x=130, y=560)

Date_label = Label(text='Date of Visit ', font=('Georgia', 12))
Date_label.place(x=500, y=120)
# Date_input = Entry(width=30)
Date_input = DateEntry(window, width=30)
Date_input.place(x=500, y=150)

Time_label = Label(text='Time of Visit ', font=('Georgia', 12))
Time_label.place(x=500, y=190)
# Time_input = Entry(width=30)
Time_input = Combobox(width=30, values=['4:00', '4:20', '4:40', '5:00', '5:20',
                                        '5:40', '6:00', '6:20', '6:40', '7:00', '7:20', '7:40',
                                        '8:00', '8:40', '9:00'])
Time_input.place(x=500, y=210)
#  Appoinment  (day _Time)
Notes_label = Label(text='Appointment ', font=('Georgia', 12), )
Notes_label.place(x=500, y=250)
# day
l2 = Label(text="Day", background="white", foreground='#FC6130', font=("gray", 10))
l2.place(x=500, y=280)
add_day = Entry(window, width=15, background="#D3F371", foreground="purple",)
add_day.place(x=500, y=300, height=22.5)
# Time
l4 = Label(text="Time", background="white", foreground='#FC6130', font=("gray", 10))
l4.place(x=610, y=280)
add_day = Entry(window, width=15, background="#D3F371", foreground="purple")
add_day.place(x=610, y=300, height=22.5)




Accept_btn = Button(text="Accept", width=11, cursor="hand2", style='TButton', command=window.destroy)
Accept_btn.place(x=500, y=440)

cancel_btn = Button(text="Cancel", width=11, cursor="hand2", style='TButton', command=window.destroy)
cancel_btn.place(x=500, y=470)

window.mainloop()
