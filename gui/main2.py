from tkinter import *

root = Tk()
root.title("Pay Calculator")

lbl1 = Label(root, text="Hours:")
lbl2 = Label(root, text="Rate:")
entHours = Entry(root)
entRate = Entry(root)

lbl1.grid(row=0, sticky=W, padx=5)
lbl2.grid(row=1, sticky=W, padx=5)

entHours.grid(row=0, column=1,padx=10, pady=5)
entRate.grid(row=1, column=1, padx=10, pady=5)

btnCalc = Button(root, text="Calculate Pay")
btnCalc.grid(row=2, columnspan=2, padx=10, pady=5)

lblGross = Label(root)
lblGross.grid(columnspan=2, padx=10, pady=5)

def calc_pay(self):
  hours = float(entHours.get())
  rate = float(entRate.get())
  gross = hours * rate
  message = f"Pay is ${gross:.2f}"
  lblGross.config(text=message)

btnCalc.bind("<Button-1>", calc_pay)


root.mainloop()




