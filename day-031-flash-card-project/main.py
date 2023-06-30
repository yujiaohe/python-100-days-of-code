from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    word_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_df = pd.read_csv("data/french_words.csv")

to_learn = word_df.to_dict(orient="records")
current_card = {}


def is_known():
    next_card()
    to_learn.remove(current_card)
    print(len(to_learn))
    learn_data = pd.DataFrame(to_learn)
    learn_data.to_csv("data/words_to_learn.csv", index=False)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card_canvas.itemconfig(card_title, text="French", fill="black")
    card_canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    card_canvas.itemconfig(canvas_image, image=card_front_img)
    window.after(3000, flip_card)


def flip_card():
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    card_canvas.itemconfig(canvas_image, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = card_canvas.create_image(400, 263, image=card_front_img)
card_title = card_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = card_canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()
