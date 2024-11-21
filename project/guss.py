import random
import tkinter as tk
from tkinter import messagebox

class GuessTheNumberApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Guess the Number Game")

        # Randomly generate the number to guess
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        # Instructions label
        self.label = tk.Label(root, text="Guess a number between 1 and 100:", font=("Arial", 14))
        self.label.pack(pady=10)

        # Entry for user's guess
        self.guess_entry = tk.Entry(root, font=("Arial", 14), width=10)
        self.guess_entry.pack(pady=5)

        # Submit button
        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 12))
        self.submit_button.pack(pady=5)

        # Feedback label
        self.feedback_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.feedback_label.pack(pady=5)

    def check_guess(self):
        try:
            # Get user's guess
            guess = int(self.guess_entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.feedback_label.config(text="Too low! Try again.")
            elif guess > self.number_to_guess:
                self.feedback_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number {self.number_to_guess} in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def reset_game(self):
        # Reset the game state
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.guess_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

# Create the main application window
if _name_ == "_main_":
    root = tk.Tk()
    app = GuessTheNumberApp(root)
    root.mainloop()