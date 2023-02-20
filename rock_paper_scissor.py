import tkinter as tk
from tkinter import messagebox
import random

def play_game(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    user_choice = choice

    result = "You chose: " + user_choice + "\nComputer chose: " + computer_choice + "\n"

    if user_choice == computer_choice:
        result += "Tie!"
    elif user_choice == "Rock" and computer_choice == "Scissors":
        result += "You win!"
        user_score[0] += 1
    elif user_choice == "Paper" and computer_choice == "Rock":
        result += "You win!"
        user_score[0] += 1
    elif user_choice == "Scissors" and computer_choice == "Paper":
        result += "You win!"
        user_score[0] += 1
    else:
        result += "You lose."
        computer_score[0] += 1

    messagebox.showinfo("Result", result)
    score_label.config(text="User: " + str(user_score[0]) + " Computer: " + str(computer_score[0]))

def reset_scores():
    user_score[0] = 0
    computer_score[0] = 0
    score_label.config(text="User: " + str(user_score[0]) + " Computer: " + str(computer_score[0]))

app = tk.Tk()
app.title("Rock-Paper-Scissors")

user_score = [0]
computer_score = [0]

start_message = tk.Label(app, text="Select a button to play:")
start_message.pack()

rock_button = tk.Button(app, text="Rock", command=lambda: play_game("Rock"), bg="red", height=3, width=15, cursor="hand2")
paper_button = tk.Button(app, text="Paper", command=lambda: play_game("Paper"), bg="green", height=3, width=15, cursor="hand2")
scissors_button = tk.Button(app, text="Scissors", command=lambda: play_game("Scissors"), bg="blue", height=3, width=15, cursor="hand2")

rock_button.pack()
paper_button.pack()
scissors_button.pack()

reset_button = tk.Button(app, text="Reset Scores", command=reset_scores, bg="yellow", height=3, width=15, cursor="hand2")
reset_button.pack()

score_label = tk.Label(app, text="User: 0 Computer: 0")
score_label.pack()

app.mainloop()