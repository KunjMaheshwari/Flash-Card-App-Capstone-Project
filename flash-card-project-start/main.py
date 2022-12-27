from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card_front.itemconfig(card_text, text="French", fill="black")
    card_front.itemconfig(card_word, text=current_card["French"], fill="black")
    card_front.itemconfig(card_background, image=insert_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    card_front.itemconfig(card_text, text="English", fill="white")
    card_front.itemconfig(
        card_word, text=current_card["English"], fill="white")
    card_front.itemconfig(card_background, image=inser_backimage)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=800, height=600)

flip_timer = window.after(3000, func=flip_card)


card_front = Canvas(width=800, height=526,
                    bg=BACKGROUND_COLOR, highlightthickness=0)
insert_image = PhotoImage(file="images/card_front.png")
inser_backimage = PhotoImage(file="images/card_back.png")
card_background = card_image = card_front.create_image(
    400, 263, image=insert_image)
card_text = card_front.create_text(
    400, 150, text="text", font=("Arial", 40, "italic"))
card_word = card_front.create_text(
    400, 263, text="word", font=("Arial", 60, "bold"))
card_front.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
