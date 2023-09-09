from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FIXED_WIDTH = 800
FIXED_HEIGHT = 526
GOAL_COMPLETE_TEXT = "No new word to learn"

from_lang = "French"
to_lang = "English"


def load_data(file):
    return pandas.read_csv(file).to_dict(orient="records")


def have_words_to_learn(words_record):
    return len(words_record) > 0


def show_goal_completed():
    label = Label(text=GOAL_COMPLETE_TEXT, bg=BACKGROUND_COLOR, fg="white", font=("Arial", 40, "bold"))
    label.place(relx=0.5, rely=0.5, anchor=CENTER)


def know_word():
    # remove word from words_to_learn
    words_to_learn.remove(current_word)
    # save updated words_to_learn to a file
    pandas.DataFrame(data=words_to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_word, flip_timerId
    window.after_cancel(flip_timerId)
    if have_words_to_learn(words_to_learn):
        current_word = choice(words_to_learn)
        canvas.itemconfig(canvas_image, image=card_front_img)
        canvas.itemconfig(card_title, text=from_lang, fill="black")
        canvas.itemconfig(card_word, text=current_word[from_lang], fill="black")
        flip_timerId = window.after(3000, flip_card)
    else:
        canvas.grid_forget()
        right_btn.grid_forget()
        wrong_btn.grid_forget()
        show_goal_completed()


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text=to_lang, fill="white")
    canvas.itemconfig(card_word, text=current_word[to_lang], fill="white")
    window.after_cancel(flip_timerId)


try:
    words_to_learn = load_data("data/words_to_learn.csv")
except FileNotFoundError:
    words_to_learn = load_data("data/french_words.csv")

window = Tk()
window.title("Flash Card")
window.minsize(width=FIXED_WIDTH, height=FIXED_HEIGHT)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

if not have_words_to_learn(words_to_learn):
    show_goal_completed()
else:
    current_word = choice(words_to_learn)

    flip_timerId = window.after(3000, func=flip_card)

    # create canvas
    canvas = Canvas(width=FIXED_WIDTH, height=FIXED_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
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
    right_btn = Button(image=check_icon_img, bd=0, highlightthickness=0, command=know_word)
    right_btn.grid(row=1, column=1)


window.mainloop()
