from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

words_data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

from_lang = "French"
to_lang = "English"
current_word = choice(words_data)


def next_card():
    global current_word, flip_timerId
    window.after_cancel(flip_timerId)
    current_word = choice(words_data)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text=from_lang, fill="black")
    canvas.itemconfig(card_word, text=current_word[from_lang], fill="black")
    flip_timerId = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text=to_lang, fill="white")
    canvas.itemconfig(card_word, text=current_word[to_lang], fill="white")
    window.after_cancel(flip_timerId)


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timerId = window.after(3000, func=flip_card)

# create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text=from_lang, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=current_word[from_lang], font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# create buttons
cancel_icon_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=cancel_icon_img, bd=0, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

check_icon_img = PhotoImage(file="images/right.png")
right_btn = Button(image=check_icon_img, bd=0, highlightthickness=0, command=next_card)
right_btn.grid(row=1, column=1)


window.mainloop()
