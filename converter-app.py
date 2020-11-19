from tkinter import *
from tkinter import ttk
import requests

root = Tk()
root.title('Weather App: Siphenkosi')
root.geometry("400x300")


def convert():
    base = selection2.get()
    url = f'https://v6.exchangerate-api.com/v6/4c17ef91aa3a8af8fb32a96c/latest/{base}'
    response = requests.get(url)
    result = response.json()

    x = float(amount_entry.get())
    currency = selection1.get()
    y = result['conversion_rates'][currency]
    calc = x/y
    output.config(text=round(calc, 2))


header = Label(root, text="Converter App", font=("arial", 20, "bold")).place(x=105, y=10)

amount_lbl = Label(root, text="Amount: ", font=("arial", 12, "bold")).place(x=20, y=70)
amount_entry = Entry(root, width=30)
amount_entry.place(x=100, y=70)

select_cur_lbl = Label(root, text="Select currency:")
select_cur_lbl.place(x=20, y=100)
var = StringVar()
selection1 = ttk.Combobox(root, textvariable=var, width=18, value=["USD", "ZAR", "PRE"])
selection1.place(x=20, y=130)

select_cur_lbl2 = Label(root, text="Select currency:")
select_cur_lbl2.place(x=240, y=125)
var2 = StringVar()
selection2 = ttk.Combobox(root, textvariable=var2, width=18, value=["USD", "ZAR", "PRE"])
selection2.place(x=240, y=125)

convert = Button(root, text="Convert", command=convert).place(x=240, y=160)

output = Label(root, font=("arial", 15), fg="green")
output.place(x=180, y=200)

root.mainloop()
