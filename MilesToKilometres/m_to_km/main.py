import tkinter
import time

window = tkinter.Tk()
window.title("Miles to Kilometres")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

label1 = tkinter.Label(text="is equal to:")
label1.grid(column=0, row=1)

entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0)

miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

number = tkinter.Label(text="0")
number.grid(column=1, row=1)

km = tkinter.Label(text="km")
km.grid(column=2, row=1)


def calculate():
    number.config(text=f"{round(float(entry.get()) * 1.60934, 2)}")


calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
