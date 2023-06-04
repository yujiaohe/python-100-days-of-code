from tkinter import *
from tkmacosx import Button
from random_word import Wordnik
from tkinter import messagebox
import requests
import random

LIMIT = 50

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()


def start():
    timer_label.config(text="01:00")
    speed = speed_result_label.cget("text")
    print(f"current speed is {speed}")
    words_cycle = 1
    if speed != '?':
        words_cycle = speed // 40 + 1
    # Method1: generate random_words with Wordnik
    # random_words = []
    # wordnik = Wordnik()
    # for _ in range(words_cycle):
    #     # .get_random_words() return 50 words
    #     random_words.extend(wordnik.get_random_words())

    # Method2: generate random_words with a remote dictionary
    random_words = random.choices(WORDS, k=LIMIT*words_cycle)
    random_words = [item.decode("utf-8") for item in random_words]

    sample_text.config(state=NORMAL)
    sample_text.delete("1.0", END)
    sample_text.insert(END, ' '.join(random_words))
    sample_text.config(state=DISABLED)

    type_text.config(state=NORMAL)
    type_text.delete("1.0", END)
    type_text.focus()

    count_down(60, random_words)


def count_down(count, words):
    count_min = count // 60
    count_sec = count % 60
    timer_label.config(text=f"{count_min:02n}:{count_sec:02n}")
    if count > 0:
        window.after(1000, count_down, count - 1, words)
    else:  # time over and calculate typing speed
        # disable user input first
        type_text.config(state=DISABLED)
        type_words = type_text.get('1.0', END).split(" ")
        correct_sum = 0
        for i in range(min(len(words), len(type_words))):
            if words[i] == type_words[i]:
                correct_sum += 1
        user_speed = correct_sum
        print(f"{user_speed}")
        messagebox.showinfo("Speed WPM", message=f"Your typing speed WPM is:\n{user_speed}")
        speed_result_label.config(state=NORMAL)
        speed_result_label.config(text=user_speed)
        speed_result_label.config(state=DISABLED)


# --------------------UI setup------------------
window = Tk()
window.title("Typing Speeding Test")
window.config(padx=10, pady=10)

# Labels
speed_label = Label(text="Speed WPM:", width=10)
speed_label.grid(column=0, row=0)
time_label = Label(text="Time left:", width=10)
time_label.grid(column=2, row=0)
speed_result_label = Label(text="?", width=10, background="white", borderwidth=1)
speed_result_label.grid(column=1, row=0)
timer_label = Label(text="01:00", width=10, background="white", borderwidth=1)
timer_label.grid(column=3, row=0)
type_label = Label(text="Type word below:")
type_label.grid(column=0, row=2)

# Texts
sample_text = Text(bg="#FFF8DE", height=10, width=50, font=("Arial", 14))
sample_text.config(state=DISABLED)
sample_text.grid(column=0, row=1, columnspan=4)
type_text = Text(height=10, width=50, font=("Arial", 14))
type_text.grid(column=0, row=3, columnspan=4)

# Button
start_button = Button(window, text="Start", background="#D6E8DB", command=start)
start_button.grid(column=3, row=2)

window.mainloop()