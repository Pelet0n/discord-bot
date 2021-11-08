from tkinter import *
 
root = Tk()

#myLabel = Label(root, text='Siema')
#myLabel2 = Label(root, text='Siema Jestem wojtek')
#myLabel3 = Label(root, text='')
#myLabel4 = Label(root, text='')
#myLabel5 = Label(root, text='')
def myClick():
    myLabel = Label(root, text='Hey you got this', fg='green', bg="#000000")
    myLabel.pack()
    




myButton = Button(root, text="1", command=myClick, fg="red", bg="#000000")
myButton.pack() 















#myLabel.grid(row=0, column=0)
#myLabel2.grid(row=1, column=5)
#myLabel3.grid(row=2, column=1)
#myLabel4.grid(row=3, column=1)
#myLabel5.grid(row=4, column=1)
root.mainloop()