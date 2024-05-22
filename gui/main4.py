from tkinter import *

def selectedValue():
  selection = "You selected the option" + str(var.get())
  label.config(text = selection)

root = Tk()
root.title("Radio Buttons")

var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=selectedValue)
R1.grid(pady=3)

R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=selectedValue)
R2.grid(pady=3)

R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=selectedValue)
R3.grid(pady=3)

label = Label(root)
label.grid(sticky=S)






root.mainloop()





