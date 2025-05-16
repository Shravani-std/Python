import tkinter as tk
from tkinter import messagebox
import random

def play(user_choice):
    global score_user, computer_score

    cmp_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(cmp_choices)

    result_text.set(f"You chose: {user_choice}\nComputer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_text.set(result_text.get() + "\nIt's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        score_user += 1
        result_text.set(result_text.get() + f"\nYou won this round!")
    else:
        computer_score += 1
        result_text.set(result_text.get() + f"\nComputer won this round!")

    score_label.config(text=f"Score: You {score_user} - Computer {computer_score}")

    if score_user == 3:
        messagebox.showinfo("Game Over", "You are the Champion!")
        reset_game()
    elif computer_score == 3:
        messagebox.showinfo("Game Over", "Computer is the Champion!")
        reset_game()

def reset_game():
    global score_user, computer_score
    score_user = 0
    computer_score = 0
    score_label.config(text=f"Score: You 0 - Computer 0")
    result_text.set("Make your move!")

# Setup GUI
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

score_user = 0
computer_score = 0

title = tk.Label(root, text="Rock - Paper - Scissors", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

rules = tk.Label(root, text="First to 3 wins is the champion!", font=("Helvetica", 10))
rules.pack(pady=5)

result_text = tk.StringVar()
result_text.set("Make your move!")

result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 12), fg="blue")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score: You 0 - Computer 0", font=("Helvetica", 12))
score_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=12, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=12, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=12, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
