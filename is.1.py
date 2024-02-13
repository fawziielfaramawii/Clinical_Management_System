from tkinter import *
import  mysql.connector
import pymysql
import tkinter as tk
from tkinter import ttk
from  tkinter import messagebox
from tkinter.ttk import Combobox
import pyttsx3
from tkcalendar import Calendar,DateEntry
from PIL import ImageTk




# connect to data base
def connect_database():
    if name.get() == '' or phone.get() == '' or adress.get() == '' or gender_combobox.get() == '' or birth.get() == '':
        messagebox.showerror('ERROR :(', 'All Fields are Required.')
    else:
        try:
            mydb=mysql.connector.Connect(host="localhost", user="root", password="fawzy@@",database="patients")
            my_cursor= mydb.cursor()
        except:
            messagebox.showerror("Error","Database Connectivity Issue,Please Try Again")
            return
        query = 'insert into data_patients (Patient_Name,Patient_Phone,Patient_Adress ,Gander,Birth_Date)values(%s,%s,%s,%s,%s)'
        my_cursor.execute(query,(name.get(), phone.get(), adress.get(), gender_combobox.get(), birth.get()))
        mydb.commit()
        mydb.close()
        messagebox.showinfo('Success','The Process Is Completely Successfully')
        clear()


def clear():
    name.delete(0,END)
    phone.delete(0,END)
    adress.delete(0,END)
    gender_combobox.delete(0,END)
    birth.delete(0,END)




# init ************GUI****************************
window = Tk()
window.title("Patient")
window.resizable(False, False)

# photo *********************************************
img = ImageTk.PhotoImage(file="ma.png")
label = Label(window, image=img)
label.pack()



# name*************************************.
name = Entry(window, bg="#c78767", fg="black", relief="flat", font=("family", 10), highlightthickness=1,
            highlightbackground="#f5b03b", highlightcolor="#c78767"
            , selectbackground="#fdd1a7", selectforeground="#f5b03b")
name.place(x=120, y=110, width=200, height=25)

l2 = Label(text=" Patient Name", highlightcolor="#f5b03b",bg="white",foreground="black",highlightbackground="#fdd1a7",font=("gray",10))
l2.place(x=100 ,y=90,width= 120 ,height=20)




# phone *****************************************
phone = Entry(window, bg="#c78767", fg="black", relief="flat", font=("family", 10), highlightthickness=1,
            highlightbackground="#f5b03b", highlightcolor="#c78767"
            , selectbackground="#fdd1a7", selectforeground="#f5b03b")
phone.place(x=120, y=200, width=200, height=25)

l2 = Label(text=" Patient Phone", highlightcolor="#f5b03b",bg="white",foreground="black", highlightbackground="black", font=("black",10))
l2.place(x=100 ,y=180,width= 120 ,height=20)




# gander *************************************************************************************

gender_combobox = Combobox(window, values=['Male', 'Female'], font="brown 10", state='r',
background="green",foreground="black")
gender_combobox.place(x=120, y=405, width=200, height=25)

l2 = Label(text=" Patient Gender", highlightcolor="#f5b03b",bg="white",foreground="black",highlightbackground="black",font=("black",10))
l2.place(x=100 ,y=385,width= 120 ,height=20)




#** Appointments************************************************************
appointment_combobox = Combobox(window, values=['4 : 00', '4 : 20'], font="brown 10", state='r',
background="green",foreground="black")
appointment_combobox.place(x=430, y=405, width=200, height=25)

l5 = Label(text="Appointment", highlightcolor="#f5b03b",bg="white",foreground="black",highlightbackground="black",font=("black",10))
l5.place(x=410 ,y=385,width= 120 ,height=20)




# adress ****************************************************************
adress = Entry(window, bg="#c78767", fg="black", relief="flat", font=("family", 10), highlightthickness=1,
            highlightbackground="#f5b03b", highlightcolor="#c78767"
            , selectbackground="#fdd1a7", selectforeground="#f5b03b")
adress.place(x=120, y=290, width=200, height=50)

l2 = Label(text=" Patient Adress", highlightcolor="#f5b03b",bg="white",foreground="black",highlightbackground="black",font=("black",10))
l2.place(x=100 ,y=270,width= 120 ,height=20)






# DATE

l2 = Label(text="Date of Birth", highlightcolor="#f5b03b",bg="white",foreground="black",highlightbackground="black",font=("black",10) )
l2.place(x=100 ,y=480,width= 120 ,height=20)


birth = DateEntry(window,selectmode='day', highlightcolor="#f5b03b",bg="white",foreground="black",highlightbackground="black",font=("black",10),height=15)
birth.place(x=120,y=500,width= 200,height=25)
#def my_upd():
   # l1.config(text=cal.get_date())
#b1 = tk.Button(window, text="The Date Is", command=lambda: my_upd(),bg="#c78767", fg="black", )
#b1.place(x=470,y=145,height=15)
#l1=tk.Label(window, bg="#f5b03b",fg="black")
#l1.place(x=470, y=165)





#* edit ***************
f1=Button(window,text="Edit",highlightcolor="#f5b03b",bg="yellow",foreground="black",highlightbackground="black",font=("black",12),height=8)
f1.place(x=430,y =210,width=150,height=25)



#* save ***************
f1=Button(window,text="Save",highlightcolor="#f5b03b",bg="brown",foreground="yellow",highlightbackground="black",font=("black",12),height=8,command=connect_database)
f1.place(x=430,y =250,width=150,height=25)


#* clear ***************
f1=Button(window,text="Clear",highlightcolor="#f5b03b",bg="gray",foreground="black",highlightbackground="black",font=("black",12),height=8,command=clear)
f1.place(x=430,y =290,width=150,height=25)








































window.mainloop()


