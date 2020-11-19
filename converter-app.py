from tkinter import *
from tkinter import ttk
import requests

root = Tk()
root.title('Weather App: Siphenkosi')
root.geometry("400x300")

url = f'https://v6.exchangerate-api.com/v6/4c17ef91aa3a8af8fb32a96c/latest/USD'
response = requests.get(url)
result = response.json()

country_code = list(result['conversion_rates'].keys())


def convert():
    try:
        base = selection2.get()
        url = f'https://v6.exchangerate-api.com/v6/4c17ef91aa3a8af8fb32a96c/latest/{base}'
        response = requests.get(url)
        result = response.json()

        x = float(amount_entry.get())
        currency = selection1.get()
        y = result['conversion_rates'][currency]
        calc = x/y
        output.config(text=round(calc, 2))
        code_output.config(text=base)
    except ValueError:
        amount_entry.delete(0,END)
        output.config(text="please enter a valid amount")


header = Label(root, text="Converter App", font=("arial", 20, "bold"))
header.place(x=105, y=10)

amount_lbl = Label(root, text="Amount: ", font=("arial", 12, "bold"))
amount_lbl.place(x=20, y=70)
amount_entry = Entry(root, width=30)
amount_entry.place(x=100, y=70)

select_cur_lbl = Label(root, text="From:")
select_cur_lbl.place(x=20, y=100)
var = StringVar()
selection1 = ttk.Combobox(root, textvariable=var, width=18, value=country_code)
selection1.set(country_code[0])
selection1.place(x=20, y=130)

select_cur_lbl2 = Label(root, text="To:")
select_cur_lbl2.place(x=240, y=100)
var2 = StringVar()
selection2 = ttk.Combobox(root, textvariable=var2, width=18, value=country_code)
selection2.set(country_code[0])
selection2.place(x=240, y=130)

convert = Button(root, text="Convert", command=convert)
convert.place(x=240, y=160)

output = Label(root, font=("arial", 15), fg="green")
output.place(x=180, y=200)

code_output = Label(root, font=("arial", 15), fg="red")
code_output.place(x=270, y=200)

root.mainloop()
