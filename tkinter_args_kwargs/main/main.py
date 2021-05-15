import tkinter


def button_clicked():
    print("I got clicked")
    # new_text = entry.get()
    label.config(text=f"{entry.get()}")


# Window
window = tkinter.Tk()
window.title("First Python GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
label["text"] = "New Text"
label.config(text="Label", padx=20, pady=20)

# label.pack()  # pack is not very precise
# label.place(x=0, y=0)  # place is too precise
label.grid(column=0, row=0)
# label.pack(side="left")
# label.pack(side="bottom")
# label.pack(expand=True)


# Button


button = tkinter.Button(text="Button", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
# Entry (Input)

button2 = tkinter.Button(text="Button 2")
button2.grid(column=2, row=0)

entry = tkinter.Entry(width=10)
# entry.pack()
entry.grid(column=3, row=2)

window.mainloop()
