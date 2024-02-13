from tkinter import *

# from tkinter.ttk import Combobox
from PIL import ImageTk
from tkcalendar import *
from tkinter.ttk import *

# import pymysql
# import mysql.connector


# def connect_database():

window = Tk()
window.title("Lab")
window.resizable(False, False)  # no zoom in/out window


background_Image = ImageTk.PhotoImage(file="lab.png")
background_label = Label(window, image=background_Image)
background_label.pack()


style = Style()
style.configure('TButton', font=('calibri', 10, 'bold'),
                foreground='red', width=9, cursor="hand", background="red", fg="white")


Patient_name = Label(text='Patient Name ', font=('Georgia', 12), background='white',
                     style=style.configure('TEntry', bd='0', exportselection=0,
                                           selectbackground='red', selectborderwidth='red'))
Patient_name.place(x=130, y=120)
Patient_name_input = Entry(width=25)
# Patient_name_input.insert(0, 'Ayman')
# Patient_name_input.config(state='disabled')
Patient_name_input.place(x=130, y=140)

Patient_phone = Label(text='Patient Phone ', font=('Georgia', 12), background='white')
Patient_phone.place(x=130, y=190)
Patient_phone_input = Entry(width=25)
# Patient_phone_input.insert(0, '01060188385')
# Patient_phone_input.config(state='disabled')
Patient_phone_input.place(x=130, y=210)

Age = Label(text='Age ', font=('Georgia', 12), background='white')
Age.place(x=130, y=250)
Age_input = Entry(width=25)
# Age_input.insert(0, '19')
# Age_input.config(state='disabled')
Age_input.place(x=130, y=270)

Gender = Label(text='Gender ', font=('Georgia', 12), background='white')
Gender.place(x=130, y=310)
Gender_input = Combobox(width=25, values=['Male', 'Female'])
# Gender_input.insert(0, 'Male')
# Gender_input.config(state='disabled')
Gender_input.place(x=130, y=330)

Date_label = Label(text='Date of Analysis ', font=('Georgia', 12))
Date_label.place(x=500, y=120)
# Date_input = Entry(width=30)
Date_input = DateEntry(window, width=30)
Date_input.place(x=500, y=140)

No_label = Label(text='Name of Analysis ', font=('Georgia', 12))
No_label.place(x=500, y=180)
No_input = Entry(width=30)
No_input.place(x=500, y=200)

Name_label = Label(text='Result of Analysis ', font=('Georgia', 12), )
Name_label.place(x=500, y=240)
Name_entry = Text(width=39,  height=1)
Name_entry.place(x=500, y=260)

Cost = Label(text='Cost ', font=('Georgia', 12), background='white')
Cost.place(x=500, y=310)
Cost_input = Entry(width=25)
#Cost_input.insert(0, 'Cash')
Cost_input.place(x=500, y=330)

save_btn = Button(text="Save", width=11, cursor="hand2", style='TButton', command=window.destroy)
save_btn.place(x=500, y=440)

cancel_btn = Button(text="Clear", width=11, cursor="hand2", style='TButton', command=window.destroy)
cancel_btn.place(x=500, y=470)


window.mainloop()
