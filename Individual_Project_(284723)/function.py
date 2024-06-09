import pandas as pd
from tkinter import *
from tkinter import ttk

import csv

#Open a new csv file
def open_new():
    df = pd.DataFrame({'User_ID':[' '], 
                       'User_Password':[' '], 
                       'User_Full_IC':[' '], 
                       'Salary_per_year':[' '], 
                       'Total_tax_relief':[' '], 
                       'Salary_after_tax_reief':[' '], 
                       'Taxrate':[' '], 
                       'Taxpayable':[' ']})
    df.to_csv('MALAYSIA_TAX_INPUT_PROGRAM.csv', index = False)
    
#Verify login
def verify_user(user_id, password, csv_file='MALAYSIA_TAX_INPUT_PROGRAM.csv'):
    try:
        df = pd.read_csv(csv_file, dtype={'User_ID': str, 'User_Password': str})
    except FileNotFoundError:
        print(f"Error: The file {csv_file} was not found.")
        return False
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return False
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

    df['User_ID'] = df['User_ID'].astype(str).str.strip()
    df['User_Password'] = df['User_Password'].astype(str).str.strip()

    user_exists = ((df['User_ID'] == user_id) & (df['User_Password'] == password)).any()
    return user_exists

#Login
def login():
    print('Please enter your user ID and password to login your account')
    input_user_id = input("User ID: ").strip()
    input_password = input("Password: ").strip()
    if verify_user(input_user_id, input_password):
        print("Login successful!")
        return True
    else:
        print("Invalid user ID or password.")
        return False
    
#Registration 
def registration():
    user_id_r = (input('User ID:'))
    user_ic = str(input('IC number:'))
    if len(user_ic) == 12:
        print('Your IC number verify succussfully!')
        password = user_ic[-4:]
        df = pd.DataFrame({'User_ID':[user_id_r], 
                       'User_Password':[password], 
                       'User_Full_IC':[user_ic], 
                       'Salary_per_year':[' '], 
                       'Total_tax_relief':[' '], 
                       'Salary_after_tax_reief':[' '], 
                       'Taxrate':[' '], 
                       'Taxpayable':[' ']})
        df.to_csv('MALAYSIA_TAX_INPUT_PROGRAM.csv', index = False)
        print(df)
        return True
    else:
        print('Please enter your full IC number (12 digits)')
        return False

#Read data
def read():
    df = pd.read_csv('MALAYSIA_TAX_INPUT_PROGRAM.csv', dtype=str)
    print(df)

#collect salary, calculate tax relief, tax rate, and taxpayable
def salary_calculation():
    salary = int(input('Enter your salary per year'))
    if salary > 0:
        root = Tk()
        root.title('TAX RELIEF CALCULATION')
        root.geometry('1000x600')

        #Create A Main Frame
        main_frame = Frame(root)
        main_frame.pack(fill=BOTH, expand=1)

        #Create A Canvas
        my_canvas =  Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        #Add A Scrollbar to the Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        #Configure the Canvas
        my_canvas.configure(yscrollcommand = my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        #create another frame inside the canvas
        window = Frame(my_canvas)

        #add that new frame to a window in the canvas
        my_canvas.create_window((0,0), window=window, anchor="nw")

        #justify the format of data from window
        data1 = 9000
        data2 = IntVar() 
        data3 = IntVar()
        data4 = IntVar()
        data5 = IntVar()
        data6 = IntVar()
        data7 = IntVar()
        data8 = IntVar()
        data9 = IntVar()
        data10 = IntVar()
        data11 = IntVar()
        data12 = IntVar()
        data13 = IntVar()
        data14 = IntVar()
        data15 = IntVar()
        data16a = IntVar()
        data16bi = IntVar()
        data16bii = IntVar()
        data16ci = IntVar()
        data16cii = IntVar()
        data17 = IntVar()
        data18 = IntVar()
        data19 = IntVar()
        data20 = IntVar()
        data21 = IntVar()

        #submit button
        def submit():
            #collect data for calculate tax relief
            a = data1

            b = data2.get()
            if b > 8000:
                b = 8000

            c = data3.get()
            if c > 6000:
                c = 6000

            d = data4.get()
            if d == 1:
                d = 6000

            e = data5.get()
            if e > 7000:
                e = 7000

            f = data6.get()

            g = data7.get()
            if g > 1000:
                g = 1000

            h = data8.get()
            if h > 4000:
                h = 4000

            fgh = f + g + h
            if fgh > 10000:
                fgh = 10000

            i = data9.get()
            if i > 2500:
                i = 2500

            j = data10.get()
            if j > 500:
                j = 500

            k = data11.get()
            if k > 1000:
                k = 1000

            l = data12.get()
            if l > 3000:
                l = 3000

            m = data13.get()
            if m > 8000:
                m = 8000

            n = data14.get()
            if n > 4000:
                n = 4000

            o = data15.get()
            if o == 1:
                o = 5000

            p = data16a.get()
            p = 2000 * p

            qi = data16bi.get()
            qi = 2000 * qi

            qii = data16bii.get()
            qii = 8000 * qii

            ri = data16ci.get()
            if ri == 1:
                ri = 6000

            rii = data16cii.get()
            if rii == 1:
                rii = 8000

            s = data17.get()
            if s > 7000:
                s = 7000

            t = data18.get()
            if s > 3000:
                s = 3000

            u = data19.get()
            if u > 3000:
                u = 3000

            v = data20.get()
            if v >350:
                v = 350

            w = data21.get()
            if w > 2500:
                w = 2500

            Total_tax_relief = a+b+c+d+e+fgh+i+j+k+l+m+n+o+p+qi+qii+ri+rii+s+t+u+v+w
            income = salary - Total_tax_relief

            # tax calculation
            if income > 0 and income <= 5000:
                    taxrate = 0
                    tax = 0

            elif income > 5000 and income <= 20000:
                    taxrate = 1
                    tax = ((salary - 5000) * taxrate/100)

            elif income > 20000 and income <= 35000:
                    taxrate = 3
                    tax = 150 + ((salary - 20000) * taxrate/100)

            elif income > 35000 and income <= 50000:
                    taxrate = 6
                    tax = 600 + ((salary - 35000) * taxrate/100)

            elif income > 50000 and income <= 70000:
                    taxrate = 11
                    tax = 1500 + ((salary - 50000) * taxrate/100)

            elif income > 70000 and income <= 100000:
                    taxrate = 19
                    tax = 3700 + ((salary - 70000) * taxrate/100)

            elif income > 100000 and income <= 400000:
                    taxrate = 25
                    tax = 9400 + ((salary - 100000) * taxrate/100)

            elif income > 400000 and income <= 600000:
                    taxrate = 26
                    tax = 84400 + ((salary - 400000) * taxrate/100)

            elif income > 600000 and income <= 2000000:
                    taxrate = 28
                    tax = 136400 + ((salary - 600000) * taxrate/100)

            elif income > 2000000:
                    taxrate = 30
                    tax = 528400 + ((salary - 2000000) * taxrate/100)

            print('Your salary = RM', salary)
            print('Total Tax Relief = RM', Total_tax_relief), 
            print('Salary for calculate your tax = RM', income)
            print('Your tax rate = ', taxrate,'%')        
            print('Your taxpayable = ', tax)

            with open('MALAYSIA_TAX_INPUT_PROGRAM.csv', mode='a', newline='') as write:
                 writer = csv.writer(write, delimiter=',')
                 writer.writerow([' ', ' ', ' ', salary, Total_tax_relief, income, taxrate, tax])
            root.destroy()

        title_Label = Label(window, text = 'ENTER THE AMOUNT IF YOU HAS/ARE:', padx=2,pady=2,font=('Helvetica 15 underline')).grid(row=0,column=0, sticky='w')
        RM_label = Label(window, text = 'RM',padx=2,pady=5,font=('Helvetica 15 underline')).grid(row=0,column=1)

        A_label = Label(window, text='1. Individual and dependent relatives', padx=2,pady=2,justify=LEFT,font=('Helvetica 10')).grid(row=1,column=0, sticky='w')
        A = Label(window, text='9000', padx=2,pady=2,font=('Helvetica 10')).grid(row=1,column=1)

        B_label = Label(window, text='2. Medical treatment, special needs and carer expenses for parents [RM8,000 (Restricted)]\n   (Medical condition certidfied by medical practitioner)',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=2,column=0, sticky='w')
        B = Entry(window, textvariable=data2,font=('Helvetica 10')).grid(row=2,column=1)

        C_label = Label(window, text='3. Purchase of basic supporting equipment for disable self, spouse, child or parent [RM6,000 (Restricted)]',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=3,column=0, sticky='w')
        C = Entry(window, textvariable=data3,font=('Helvetica 10')).grid(row=3,column=1)

        D_label = Label(window, text='4. Disable individual [RM6,000]',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=4,column=0, sticky='w')
        D = Checkbutton(window, text='YES', variable=data4).grid(row=4,column=1)

        E_label = Label(window, text='5. Education fees (Self): [RM7,000 (Restricted)]\n     i. Other than a degree at masters or doctorate level - \n        Course of study in law, accounting, islamic financing, technical, vocational, industrial, scientific or technology\n     ii. Degree at masters or doctorate level - Any course of study\n     iii. Course of study undertaken for the purpose of upskilling or self-enhancement (Restricted to RM2000)',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=5,column=0, sticky='w')
        E = Entry(window, textvariable=data5,font=('Helvetica 10')).grid(row=5,column=1)

        F_label = Label(window, text='6. Medical expenses on: \n     i. Serious diseases for self, spouse or child\n     ii. Fertility treatment for sell or spouse\n     iii. Vaccination for self, spouse and child (Restricted to RM1000)',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=6,column=0, sticky='w')
        F = Entry(window, textvariable=data6,font=('Helvetica 10')).grid(row=6,column=1)

        G_label = Label(window, text='7. Expenses (Restricted to RM1000) on: \n     i. Complete medical examination for self, spouse or child\n     ii. COVID-19 detection test including purchase of self-detection test kid for self, spouse o4 child\n     iii. Mental health examination or consulation for self, spouse or child',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=7,column=0, sticky='w')
        G = Entry(window, textvariable=data7,font=('Helvetica 10')).grid(row=7,column=1)

        H_label = Label(window, text='8. Expenses (Restricted to RM4000) for child aged 18 and below: \n     i. Assessment of intellectual disability diagnosis\n     ii. Early intervetion programme / intellectual disability rehabilitation treatment',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=8,column=0, sticky='w')
        H = Entry(window, textvariable=data8,font=('Helvetica 10')).grid(row=8,column=1)

        I_label = Label(window, text='9. Lifestyle - Expenses for the use / benefit of self, spouse or child in respect of: [RM2,500 (Restricted)]\n     i. Purchase or subscription of books /journals / magazines / newspaper / other similar publications (No banned reading materials)\n     ii. Pruchase of personal computer, smartphone or tablet (Not for business use)\n     iii. Purchase of sports equipment for sports activity defined under the Sports DevelopmentAct 1997 and payment of gym membership\n     iv. Payment of monthly bill internet subscription (Under own name)',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=9,column=0, sticky='w')
        I = Entry(window, textvariable=data9,font=('Helvetica 10')).grid(row=9,column=1)

        J_label = Label(window, text='10. Lifestyle - Additional relief for the use / benefit of self, spouse or child in respect of: [RM500 (Restricted)]\n     i. Purchase of sports equipment for any sports activity as defined under the Sports Development Act 1997\n     ii. Payment of rental or entrance fee at any sports facility\n     Payment of registration fee for any licensed by the Commissioner of Sports under the Sports Development Act 1997',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=10,column=0, sticky='w')
        J = Entry(window, textvariable=data10,font=('Helvetica 10')).grid(row=10,column=1)

        K_label = Label(window, text='11. Purchase of breastfeeding equipment for own use for a child aged 2 years and below \n     (Deduction allowed once in every TWO (2) years of assessment) [RM1,000 (Restricted)]',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=11,column=0, sticky='w')
        K = Entry(window, textvariable=data11,font=('Helvetica 10')).grid(row=11,column=1)

        L_label = Label(window, text='12. Child care fees to a registered child care centre / kindergarten for a child aged 6 years and below [RM3,000 (Restricted)]',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=12,column=0, sticky='w')
        L = Entry(window, textvariable=data12,font=('Helvetica 10')).grid(row=12,column=1)

        M_label = Label(window, text='13. Net deposit in Skim Simpanan Pendidikan Nasional \n     (Net deposit is the total deposit in 2023 MINUS total withdrawal in 2023) [RM8,000 (Restricted)]',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=13,column=0, sticky='w')
        M = Entry(window, textvariable=data13,font=('Helvetica 10')).grid(row=13,column=1)

        N_label = Label(window, text='14. Husband / wife / payment of alimony to former wife [RM4,000 (Restricted)]',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=14,column=0, sticky='w')
        N = Entry(window, textvariable=data14,font=('Helvetica 10')).grid(row=14,column=1)

        O_label = Label(window, text='15. Disabled husband / wife [RM5,000]',
                    padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=15,column=0, sticky='w')
        O = Checkbutton(window, text='YES', variable=data15).grid(row=15,column=1)

        P_label = Label(window, text='16a. Each unmarried child and under the age of 18 years old [RM2,000 per person] (ENTER THE NUMBER OF CHILD)',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=16,column=0, sticky='w')
        P = Entry(window, textvariable=data16a,font=('Helvetica 10')).grid(row=16,column=1)

        Qi_label = Label(window, text='16b(i). Each unmarried child of 18 years and above who is receiving full-time education [RM8,000 per person] (ENTER THE NUMBER OF CHILD)\n          ("A-Level", certificate, matriculation or preparatory courses) [RM2,000]',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=17,column=0, sticky='w')
        Qi = Entry(window, textvariable=data16bi,font=('Helvetica 10')).grid(row=17,column=1)

        Qii_label = Label(window, text='16b(ii). Each unmarried child of 18 years and above that: [RM2,000]\n          i. receiving further education in Malaysia in respect of an award of diploma or higher \n             (excluding matriculation/ preparatory courses)\n          ii. receiving further education outside Malaysia in respect of an award of degree or its equivalent \n             (including Master or Doctorate)\n          iii. the instruction and educational establishment shall be approved by the relevant government authority',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=18,column=0, sticky='w')
        Qii = Entry(window, textvariable=data16bii,font=('Helvetica 10')).grid(row=18,column=1)

        Ri_label = Label(window, text='16c(i). Disabled child [RM6,000]',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=19,column=0, sticky='w')
        Ri = Checkbutton(window, text='YES', variable=data16ci).grid(row=19,column=1)

        Rii_label = Label(window, text='16c(ii). Additional exemption of RM8,000 disable child age 18 years old and above, not married and pursuing \n          diplomas or above qualification in Malaysia @ bachelor degree or above outside Malaysia in program and in \n          Higher Education Institute that is accredited by related Government authorities [RM8,000]',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=20,column=0, sticky='w')
        Rii = Checkbutton(window, text='YES', variable=data16cii).grid(row=20,column=1)

        S_label = Label(window, text='17. Life insurance and EPF [RM7,000 (Restricted)]\n     Civil servants’ pension schemes, non-civil servants pension schemes and self-employed category:\n      i. Mandatory contributions to approved schemes or voluntary contributions to EPF \n         (excluding private retirement schemes) or contributions under any written law (Restricted to RM4,000)\n      ii. Life insurance premium payments or family takaful contributions or additional voluntary contributions to EPF \n         (Restricted to RM3,000)',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=21,column=0, sticky='w')
        S = Entry(window, textvariable=data17,font=('Helvetica 10')).grid(row=21,column=1)

        T_label = Label(window, text='18. Deferred Annuity and Private Retirement Scheme (PRS) [RM4,000 (Restricted)]',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=22,column=0, sticky='w')
        T = Entry(window, textvariable=data18,font=('Helvetica 10')).grid(row=22,column=1)

        U_label = Label(window, text='19. Education and medical insurance [RM3,000 (Restricted)]',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=23,column=0, sticky='w')
        U = Entry(window, textvariable=data19,font=('Helvetica 10')).grid(row=23,column=1)

        V_label = Label(window, text='20. Contribution to the Social Security Organization (SOCSO) [RM350 (Restricted)]',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=24,column=0, sticky='w')
        V = Entry(window, textvariable=data20,font=('Helvetica 10')).grid(row=24,column=1)

        W_label = Label(window, text='21. Expenses on charging facilities for Electric Vehicle (Not for business use) [RM2,500 (Restricted)]',
                        padx=2,pady=5, justify=LEFT,font=('Helvetica 10')).grid(row=25,column=0, sticky='w')
        W = Entry(window, textvariable=data21,font=('Helvetica 10')).grid(row=25,column=1)

        submit = Button(window, text='Submit',command=submit, width=20,height=2).grid(row=26,columnspan=2)

        root.mainloop()

