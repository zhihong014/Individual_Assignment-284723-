import pandas as pd
import function as fn

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

Comfirm = Tk()
Comfirm.title('REGISTRATION COMFIRMATION')
Comfirm.geometry('500x200')
comfirm_a = IntVar()
comfirm_b = IntVar()

fn.open_new()

def submit():
    if comfirm_a.get() == 1:
        Comfirm.destroy()
        if fn.login():
            q = input('Do you want to CALCULATE or READ your tax data? (calc/read?)')
            if q == 'calc':
                fn.salary_calculation()
                fn.read()
            if q == 'read':
                fn.read()

    elif comfirm_b.get() == 1:
        print('Please register a account to save your information')
        Comfirm.destroy()
        if fn.registration():
            if fn.login():
                fn.salary_calculation()
                fn.read()

    elif comfirm_a.get() and comfirm_b.get() == 0:
        print('Do you want to REGISTER or LOGIN your account for MALAYSIA TAX INPUT PROGRAM?')
        Comfirm.destroy()

Comfirm_label = Label(Comfirm, text='Do you have been registered a account?',padx=10,pady=10, font=('Helvetica 12')).grid(row=1,column=1)
YES_checkbox = Checkbutton(Comfirm, text='LOGIN', variable=comfirm_a).grid(row=1,column=2)
NO_checkbox = Checkbutton(Comfirm, text='REGISTER', variable=comfirm_b).grid(row=1,column=3)
button = Button(Comfirm, text='OK', padx=20,pady=10, command=submit).grid(row=3,column=2)

Comfirm.mainloop()


