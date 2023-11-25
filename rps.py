import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

# Function to determine the winner
def play(user_choice):
    global user_score, computer_score, round_number
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    update_score_label()
    round_number += 1

    if round_number == 6:
        end_game()
        return

    create_shapes(user_choice, computer_choice, result)

# Function to update the score label
def update_score_label():
    score_label.config(text=f"You: {user_score}  Computer: {computer_score}")

# Function to end the game and display the winner
def end_game():
    if user_score > computer_score:
        winner_message = "You win the game!"
    elif user_score < computer_score:
        winner_message = "Computer wins the game!"
    else:
        winner_message = "It's a tie game!"

    messagebox.showinfo("Game Over", f"Game Over! {winner_message}")

# Create a list to store PhotoImage objects
image_list = []

# Function to create shapes for user and computer choices
def create_shapes(user_choice, computer_choice, result):
    user_choice_image = Image.open(f"{user_choice.lower()}.png")
    user_choice_image = user_choice_image.resize((100, 100))
    user_choice_image = ImageTk.PhotoImage(user_choice_image)
    image_list.append(user_choice_image)  # Store the reference in the list

    computer_choice_image = Image.open(f"{computer_choice.lower()}.png")
    computer_choice_image = computer_choice_image.resize((100, 100))
    computer_choice_image = ImageTk.PhotoImage(computer_choice_image)
    image_list.append(computer_choice_image)  # Store the reference in the list

    user_choice_label.config(image=image_list[-2])
    computer_choice_label.config(image=image_list[-1])
    result_label.config(text=result)
    update_score_label()


# Initialize scores and round number
user_score = 0
computer_score = 0
round_number = 0

# Create a Tkinter window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")
window.geometry("600x500")

# Create a heading label
heading = tk.Label(window, text="Rock, Paper, Scissors Game", font=("Times New Roman", 26), fg="maroon")
heading.pack()

# Create labels and buttons
label = tk.Label(window, text="Select your choice:", font=("Times New Roman", 20),fg="navy")
label.pack()

rock_button = tk.Button(window, text="Rock", command=lambda: play("Rock"), font=("Times New Roman", 16), fg="teal")
rock_button.pack()

paper_button = tk.Button(window, text="Paper", command=lambda: play("Paper"), font=("Times New Roman", 16), fg="teal")
paper_button.pack()

scissors_button = tk.Button(window, text="Scissors", command=lambda: play("Scissors"), font=("Times New Roman", 16), fg="teal")
scissors_button.pack()

# Create labels to display user and computer choices
user_choice_label = tk.Label(window)
user_choice_label.pack()

computer_choice_label = tk.Label(window)
computer_choice_label.pack()

# Create a label to display the result
result_label = tk.Label(window, text="", font=("Times New Roman", 20), fg="magenta")
result_label.pack()

# Create a label to display the score
score_label = tk.Label(window, text=f"You: {user_score}  Computer: {computer_score}", font=("Times New Roman", 20), fg="purple")
score_label.pack()

# Start the Tkinter main loop
window.mainloop()
