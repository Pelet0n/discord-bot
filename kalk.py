from tkinter import *
from tkinter import messagebox


root = Tk()

entry = Entry(root, width=35, borderwidth=5, text="0")
entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

tekst = StringVar()
label = Label(root, width=35, textvariable=tekst)
label.grid(row=0, column=0, columnspan=3)

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
        f_num = float(first_number) 
        tekst.set(f'{f_num} +')
        entry.delete(0, END)
    else:
        entry.delete(0, END)


def button_sub():
    first_number = entry.get()
    if first_number != '':
        global math
        global f_num
        math="addition"
        f_num = float(first_number) 
        tekst.set(f'{f_num} -')
        entry.delete(0, END)
    else:
        entry.delete(0, END)

def button_multi():
    first_number = entry.get()
    if first_number != '':
        global math
        global f_num
        math="addition"
        f_num = float(first_number) 
        tekst.set(f'{f_num} *')
        entry.delete(0, END)
    else:
        entry.delete(0, END)

def button_div():
    first_number = entry.get()
    if first_number != '':
        global math
        global f_num
        math="addition"
        f_num = float(first_number) 
        tekst.set(f'{f_num} :')
        entry.delete(0, END)
    else:
        entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)

    try:
        if math == "addition":
            sum = f_num + float(second_number)
            tekst.set(f'{f_num} + {float(second_number)} = {sum}')
        if math == "substract":
            sum = f_num - float(second_number)
            tekst.set(f'{f_num} - {int(second_number)} = {sum}')
        if math == "multiply":
            sum = f_num * float(second_number)
            tekst.set(f'{f_num} * {int(second_number)} = {sum}')
        if math == "divide":
            sum = f_num / float(second_number)
            tekst.set(f'{f_num} : {int(second_number)} = {sum}')

    except:
        messagebox.showwarning("Daj jakąś liczbe", "Nie ma liczby")

def button_cln():
    entry.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady=20,command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_dot = Button(root, text='.', padx=40, pady=20, command=lambda: button_click('.'))
button_add = Button(root, text="+", padx=39, pady=20, command=button_addn)
button_equali = Button(root, text="=", padx=39, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=39, pady=20, command=button_cln)

button_substract = Button(root, text="-", padx=41, pady=20, command=button_sub)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multi)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_div)

button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)

button_0.grid(row=5, column=0)
button_dot.grid(row=8, column=0)
button_add.grid(row=6, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_equali.grid(row=6, column=1, columnspan=2)

button_substract.grid(row=7, column=0)
button_multiply.grid(row=7, column=1)
button_divide.grid(row=7, column=2)



root.mainloop()