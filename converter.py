import tkinter
from tkinter import *

window = Tk()
window.title("Miles to Km")
window.minsize(width=244, height=120)
window.config(padx=12, pady=12, bg="#FAF0E6")

entry1 = tkinter.Entry(width=10, highlightcolor="deep sky blue", bd=3)
entry1.grid(row=0, column=1, padx=10, pady=10)

# label
label_conv = tkinter.Label(text="0", bg="#FAF0E6", font=("Arial", 10, "bold"))
label_conv.grid(row=1, column=1)

label1 = tkinter.Label(text="Miles", bg="#FAF0E6", font=("Arial", 10))
label1.grid(row=0, column=2)

label2 = tkinter.Label(text="Kilometers", bg="#FAF0E6", font=("Arial", 10))
label2.grid(row=1, column=2)

label3 = tkinter.Label(text="is equal to", bg="#FAF0E6", font=("Arial", 10))
label3.grid(row=1, column=0)

def calculate_conversion():
    user_guess = entry1.get()
    miles = float(user_guess)
    km = miles * 1.60934
    label_conv.config(text=f"{km:.2f}")

button = tkinter.Button(text="Calculate", command=calculate_conversion)
button.grid(row=2, column=1, pady=6)


window.mainloop()