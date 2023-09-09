from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# create buttons
cancel_icon_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=cancel_icon_img, bd=0, highlightthickness=0)
wrong_btn.grid(row=1, column=0)

check_icon_img = PhotoImage(file="images/right.png")
right_btn = Button(image=check_icon_img, bd=0, highlightthickness=0)
right_btn.grid(row=1, column=1)


window.mainloop()
