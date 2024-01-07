from tkinter import *
from tkinter import ttk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FRONT_TEXT_COLOR = "black"
BACK_TEXT_COLOR = "white"
current_card = {}
word_dict = {}
language = "gaeilge"
# ------ Read Data -----#
try:
    df = pd.read_csv(f"data/{language}_words_to_learn.csv")
except FileNotFoundError:
    original_df = pd.read_csv(f"data/{language}.csv")
    word_dict = original_df.to_dict(orient="records")
    language = original_df.keys()[0]
else:
    word_dict = df.to_dict(orient="records")
    language = df.keys()[0]





# ----- Display Words ---- #
def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    card = current_card[language]

    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(language_text, text=language, fill=FRONT_TEXT_COLOR)
    canvas.itemconfig(card_text, fill=FRONT_TEXT_COLOR)
    canvas.itemconfig(card_text, text=card)

    flip_timer = window.after(3000, flip_card)


def correct():
    word_dict.remove(current_card)
    data = pd.DataFrame(word_dict)
    data.to_csv(f"data/{language}_words_to_learn.csv", index=False)
    new_card()


def wrong():

    new_card()


# ---- timer ----- #
def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(language_text, text="English", fill=BACK_TEXT_COLOR)
    canvas.itemconfig(card_text, text=current_card["English"], fill=BACK_TEXT_COLOR)


# ------ Ui ------- #

window = Tk()
window.title("Vocab Tester")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)
canvas = Canvas(width=600, height=395)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(300, 200, image=front_img)
language_text = canvas.create_text(300, 130, text=language, fill=FRONT_TEXT_COLOR, font=("Ariel", 25, "italic"))
card_text = canvas.create_text(300, 197, text="", fill=FRONT_TEXT_COLOR, font=("Ariel", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=correct)
right_button.grid(row=1, column=1)

new_card()
window.mainloop()
