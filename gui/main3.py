from tkinter import *

root = Tk()
root.title("Colors")

def change_color(event):
  lst_colors["bg"] = lst_colors.get(lst_colors.curselection())

def print_selection():
  if lst_colors.curselection() == ():
    selected = "None Selected"
  else:
    selected = lst_colors.get(lst_colors.curselection())
  lbl1.configure(text=selected)
  

my_list = ["red", "yellow", "green", "blue"]
contents = StringVar()
contents.set(tuple(my_list))

lst_colors = Listbox(root, width=20, height=4, listvariable=contents)
lst_colors.grid(padx=10, pady=15)
lst_colors.bind("<<ListboxSelect>>", change_color)

b1 = Button(root, text="Display selection", command=print_selection)
b1.grid(row=1)

lbl1 = Label(root)
lbl1.grid()


root.mainloop()

























