import tkinter as tk
import random

# choices
choices = ["Rock", "Paper", "Scissors"]

# function to determine winner
def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(
        text=f"Your choice: {user_choice}\nComputer choice: {computer_choice}\nResult: {result}"
    )

# create window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("350x300")

title = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 16))
title.pack(pady=10)

# buttons
rock_btn = tk.Button(window, text="Rock", width=15, command=lambda: play("Rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(window, text="Paper", width=15, command=lambda: play("Paper"))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(window, text="Scissors", width=15, command=lambda: play("Scissors"))
scissors_btn.pack(pady=5)

# result display
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

# run GUI loop
window.mainloop()