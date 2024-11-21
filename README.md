import tkinter as tk
from tkinter import messagebox
import random

player_score = 0
computer_score = 0
rounds = 0

def play_game(player_choice):
    global player_score, computer_score, rounds

    computer_choice = random.randint(1, 6)
    total = player_choice + computer_choice

    if total % 2 == 0:
        winner = "Computer"
        computer_score += 1
    else:
        winner = "You"
        player_score += 1

    rounds += 1
    
    result_label.config(text=f"You chose: {player_choice}, Computer chose: {computer_choice}")
    score_label.config(text=f"Rounds: {rounds} | Your Score: {player_score} | Computer Score: {computer_score}")
    winner_label.config(text=f"Winner of this round: {winner}")

    if rounds >= 10:
        if player_score > computer_score:
            messagebox.showinfo("Game Over", f"You won the game! Final Score: {player_score} - {computer_score}")
        elif player_score < computer_score:
            messagebox.showinfo("Game Over", f"Computer won the game! Final Score: {player_score} - {computer_score}")
        else:
            messagebox.showinfo("Game Over", f"It's a tie! Final Score: {player_score} - {computer_score}")
        reset_game()

def reset_game():
    global player_score, computer_score, rounds
    player_score = 0
    computer_score = 0
    rounds = 0
    score_label.config(text="Rounds: 0 | Your Score: 0 | Computer Score: 0")
    result_label.config(text="")
    winner_label.config(text="")

root = tk.Tk()
root.title("Odd-Even Cricket Game")
root.geometry("400x400")
root.resizable(False, False)

title_label = tk.Label(root, text="Odd-Even Cricket Game", font=("Helvetica", 16, "bold"), pady=10)
title_label.pack()

score_label = tk.Label(root, text="Rounds: 0 | Your Score: 0 | Computer Score: 0", font=("Helvetica", 12))
score_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 12), pady=10)
result_label.pack()

winner_label = tk.Label(root, text="", font=("Helvetica", 12, "italic"), pady=10)
winner_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

for i in range(1, 7):
    button = tk.Button(
        button_frame, 
        text=str(i), 
        font=("Helvetica", 12), 
        width=5, 
        command=lambda num=i: play_game(num)
    )
    button.grid(row=0, column=i-1, padx=5)

reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 12), bg="#e74c3c", fg="white", command=reset_game)
reset_button.pack(pady=20)

root.mainloop()

