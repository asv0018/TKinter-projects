from tkinter import *
import tkinter.font as font
import random

colors = ["Red", "Orange", "White", "Black", "Green", "Blue", "Brown", "Purple", "Cyan", "Yellow", "Pink", "Magenta"]

timer = 60
score = 0
displayed_word_color = ""


def startGame():
    global displayed_word_color
    if timer == 60:
        startCountDown()
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text=random.choice(colors), fg=displayed_word_color)
        color_entry.bind('<Return>', displayNextWord)


def resetGame():
    global timer, score, displayed_word_color
    timer = 60
    score = 0
    displayed_word_color = ''
    game_score.config(text="Your score : " + str(score))
    display_words.config(text="")
    time_left.config(text="Game ends in : -")
    color_entry.delete(0, END)


def startCountDown():
    global timer
    if timer >= 0:
        time_left.config(text="Game ends in : " + str(timer) + "s")
        timer -= 1
        time_left.after(10, startCountDown)
        if timer == -1:
            time_left.config(text="Game over!!!")


def displayNextWord(event):
    global displayed_word_color
    global score
    if timer > 0:
        if displayed_word_color == color_entry.get().lower():
            score += 1
            game_score.config(text="Your score : " + str(score))
        color_entry.delete(0, END)
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text=random.choice(colors), fg=displayed_word_color)


win = Tk()
win.title("Color game")
#win.geometry("500x200")
app_font = font.Font(family="Helvetica", size=12)

game_desc = "Game description : Enter the color of the words displayed below. \n And keep in mind not to enter the word text itself."
myFont = font.Font(family="Helvetica")

game_description = Label(win, text=game_desc, font=app_font, fg="grey")
game_description.pack()

game_score = Label(win, text="Your score : " + str(score), font=(font.Font(size=16)), fg="green")
game_score.pack()

display_words = Label(win, font=(font.Font(size=28)), pady=10)
display_words.pack()

time_left = Label(win, text="Game ends in : -", font=(font.Font(size=14)), fg="orange")
time_left.pack()

color_entry = Entry(win, width=30)
color_entry.pack(pady=10)

btn_frame = Frame(win, width=80, height=40)
btn_frame.pack(side=BOTTOM)

start_button = Button(btn_frame, text="Start", width=20, fg="black", bg="pink", bd=0, padx=20, pady=10,
                      command=startGame)
start_button.grid(row=0, column=0)

reset_button = Button(btn_frame, text="Reset", width=20, fg="black", bg="light blue", bd=0, padx=20, pady=10,
                      command=resetGame)
reset_button.grid(row=0, column=1)

win.geometry('600x300')
win.mainloop()
