from tkinter import *

root = Tk()
root.title("Savings Calculator")

# create function that will:
# - retrieve the initial deposit amount
# - retrieve the interest rate and convert to decimal
# - retrieve the number of years
# - using those values, calculate and display 
#			the balance at the end of each year
# 		up to the number of years entered by the user
# - EXTRA CREDIT:  Make the list box only as big 
#			as needed.  For example, if user enters 5 years,
#			the list box should be only 5 lines tall
def calc():
  deposit_amount = float(ent_deposit.get())
  interest_rate = float(ent_interest.get()) /100
  years = int(float(ent_years.get()))
  calc_total = deposit_amount
  list.delete(0, END)
  for yr in range(1, years + 1):
    calc_total += calc_total * interest_rate
    list.insert(END, f"Year {yr} ending balance: ${calc_total:.2f}")
  
# create widgets - first label and entry box are done for you
lab_deposit = Label(root, text="Deposit Amt:")
ent_deposit = Entry(root)

lab_interest = Label(root, text="Interest Rate:")
ent_interest = Entry(root)

lab_years = Label(root, text="Years:")
ent_years = Entry(root)

btnCalc = Button(root, text="Calculate", command=calc)

list = Listbox(root, width=30, height=0)


# add the widgets to the form - first label and entry box are done for you
lab_deposit.grid(row=0, column=0, sticky=W, padx=5)
ent_deposit.grid(row=0, column=1, padx=10, pady=5, sticky=W)

lab_interest.grid(row=1, column=0, sticky=W, padx=5)
ent_interest.grid(row=1, column=1, padx=10, pady=5, sticky=W)

lab_years.grid(row=2, column=0, sticky=W, padx=5)
ent_years.grid(row=2, column=1, padx=10, pady=5, sticky=W)

btnCalc.grid(row=5, column=0, padx=10, pady=5, columnspan=2, sticky=S)

list.grid(padx=15, pady=15, sticky="", columnspan=2)



# run the code for the main loop
root.mainloop()