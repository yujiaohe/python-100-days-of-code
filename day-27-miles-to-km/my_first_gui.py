from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label["text"] = "New Text"
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


window.mainloop()


