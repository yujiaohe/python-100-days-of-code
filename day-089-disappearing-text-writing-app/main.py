from tkinter import *
from tkinter import messagebox

# https://www.squibler.io/dangerous-writing-prompt-app/write?limit=5&type=minutes
# A timer will count down and when the website detects the user
# has not written anything in the last 5/10 seconds,
# it will delete all the text they've written so far.

TIMER = 10
FONT = ('Arial', 14)
COLORS = [
    '#ff4200',
    '#f64a2e',
    '#eb514a',
    '#df5864',
    '#d25e7d',
    '#c16396',
    '#ad69b0',
    '#936eca',
    '#6d73e4',
    '#0078ff'
]

# -------------------UI Design-------------------
window = Tk()
window.title("The Most Dangerous Writing")
window.config(pady=10, padx=10)

# Labels
words_labels = Label(text="0 words", font=FONT)
words_labels.grid(column=1, row=2)
timer_labels = Label(font=FONT, fg="white", width=10)
timer_labels.grid(column=1, row=0)

# Text
typing_text = Text(window, font=FONT, fg="#6c757d")
typing_text.insert(index='1.0', chars="Start typing")
typing_text.grid(column=0, row=1, columnspan=3)


def start_typing(event):
    print("Start Typing")
    typing_text.delete(index1='1.0', index2=END)
    words = typing_text.get('1.0', END).split()
    pre_cnt = len(words)
    count_down(TIMER, pre_cnt)


def count_down(count, pre_cnt):
    words = typing_text.get('1.0', END).split()
    cnt = len(words)
    words_labels.config(text=f"{cnt} words")
    print(f"count_down, current_cnt={cnt}, pre_cnt={pre_cnt}")
    if pre_cnt == cnt and count > 0:
        timer_labels.config(text=count, background=COLORS[count - 1])
        window.after(1000, count_down, count - 1, pre_cnt)
    elif pre_cnt != cnt:  # restart timer and update pre_cnt
        count_down(TIMER, cnt)
    else:  # time over
        messagebox.showerror(title="Time Over!", message="Please start over.")
        typing_text.delete(index1='1.0', index2=END)
        words_labels.config(text="0 words")
        timer_labels.config(text="", background="white")
        print("Time out, all things will be deleted!")


typing_text.bind("<FocusIn>", start_typing)

window.mainloop()
