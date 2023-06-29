from tkinter import *

window = Tk()
# window.minsize(width=400, height=200)
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    result_label.config(text=f"{km}")


miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

km_label = Label(text=" Km")
km_label.grid(row=1, column=2)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

button = Button(text="Calculator", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()