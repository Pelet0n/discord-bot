from tkinter import *
from tkinter import messagebox
from math import sqrt
from tkinter.font import BOLD

#Konfiguracja okienka
root = Tk()
root.title("KalKInf")
root.configure(background='#7ccfc3')
font = ("Comic Sans MS",15, BOLD, )
efont = ("Comic Sans MS",30, BOLD, )
ffont = ('Comic Sans MS' ,15, BOLD,)
entry = Entry(root,   borderwidth=1, textvariable="0" , font=efont, bg="#7ccfc3", text="0")
entry.grid(row=0, column=0, columnspan=4, ipadx=25, ipady=60 )
root.resizable(width=False, height=False)


#funkcje obliczeń na liczbach
def button_click(number):
    curr = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(curr) + str(number))

def button_addn():
    first_number = entry.get()
    if first_number != '':
        global math
        global f_num
        math="addition"
        try:
            f_num = float(first_number) 
            entry.insert(0, f'{f_num}:')
        except ValueError:
            messagebox.showerror("Błąd w obliczeniach", "Błąd podczas obliczenia")
        
        entry.delete(0, END)
    else:
        entry.delete(0, END)


def button_sub():
    first_number = entry.get()
    if first_number != '':
        global math
        global f_num
        math="substract"
        try:
            f_num = float(first_number) 
            entry.insert(0, f'{f_num}:')
        except ValueError:
            messagebox.showerror("Błąd w obliczeniach", "Błąd podczas obliczenia")
        
        entry.delete(0, END)
    else:
        entry.delete(0, END)

def button_multi():
    first_number = entry.get()
    if first_number != '':
        global math
        global f_num
        math="multiply"
        try:
            f_num = float(first_number) 
            entry.insert(0, f'{f_num}:')
        except ValueError:
            messagebox.showerror("Błąd w obliczeniach", "Błąd podczas obliczenia")
        entry.delete(0, END)
    else:
        entry.delete(0, END)

def button_div():
    first_number = entry.get()
    if first_number != '':
        global math
        global f_num
        math="divide"
        try:
            f_num = float(first_number) 
            entry.insert(0, f'{f_num}:')
        except ValueError:
            messagebox.showerror("Błąd w obliczeniach", "Błąd podczas obliczenia")
        entry.delete(0, END)
    else:
        entry.delete(0, END)

def button_sqrtadd():
    first_number = entry.get()
    if first_number != '':
        try:
            f_num = float(first_number) 
            entry.insert(0, sqrt(f_num))
        except ValueError:
            messagebox.showerror("Błąd w obliczeniach", "Błąd podczas wykonywania obliczenia")
            entry.delete(0, END)
    else:
        entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)

    try:
        if math == "addition":
            sum = f_num + float(second_number)
            if sum - int(sum) == 0:
                sum = int(sum)
            entry.insert(0, sum)
        if math == "substract":
            sum = f_num - float(second_number)
            if sum - int(sum) == 0:
                sum = int(sum)
            entry.insert(0, sum)
        if math == "multiply":
            sum = f_num * float(second_number)
            if sum - int(sum) == 0:
                sum = int(sum)
            entry.insert(0, sum)
        if math == "divide":
            sum = f_num / float(second_number)
            if sum - int(sum) == 0:
                sum = int(sum)
            entry.insert(0, sum)

    except:
        messagebox.showwarning("Brak działania", "Żeby wykonało się równanie musi być działanie")


def button_cln():
    
    entry.delete(0, END)

#opisanie przycisków
button_0 = Button(root, text="0", padx=45, pady=20,borderwidth= 5, bg='#33adff' ,activebackground="#6666ff",  font=font    ,command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=45, pady=20,borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    ,command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=45, pady=20,borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    ,command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=45, pady=20,borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    ,command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=45, pady=20,borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    ,command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=45, pady=20,borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    ,command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=45, pady=20,borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    ,command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=45, pady=20,borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    ,command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=45, pady=20,borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    ,command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=45, pady=20,borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    ,command=lambda: button_click(9))
button_addon = Button(root, text="+", padx=45, pady=20,borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    ,command=  button_addn)
button_multiply = Button(root, text="*", padx=45, pady=20,borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    ,command=  button_multi)
button_minus = Button(root, text="-", padx=45, pady=20, borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    ,command= button_sub)
button_equals = Button(root, text="=", padx=117, pady=50,borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    , command= button_equal)
button_clear = Button(root, text="Clear", padx=100, borderwidth= 5, pady=50,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    , command= button_cln )
button_divide = Button(root, text="/", padx=45, borderwidth= 5, pady=20,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    , command= button_div)
button_dott = Button(root, text=".", padx=45, pady=20,borderwidth= 5,bg='#33adff' ,activebackground="#6666ff",fg="black", font=font    ,command=lambda: button_click ("."))
button_sqrt = Button(root, text="√", padx=45, pady=20, borderwidth=5, bg='#33adff', activebackground="#6666ff", fg="black", font=font, command=button_sqrtadd)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_dott.grid(row=3, column=3)
button_addon.grid(row=4, column=2)
button_clear.grid(row=6, column=0, columnspan=2, rowspan=2)
button_equals.grid(row=6, column=2, columnspan=2, rowspan=2)


button_minus.grid(row=4, column=1)
button_multiply.grid(row=1, column=3)
button_divide.grid(row=2, column=3)
button_sqrt.grid(row=4, column=3)


root.mainloop()