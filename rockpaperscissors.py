from random import randint
from tkinter import *
from tkinter import messagebox

# create hashmap that maps rock, paper and scisscors to value 0, 1, 2
hashmap = {
    "rock":     0,
    "paper":    1,
    "scissors": 2
}

# inverse hashmap
inv_hashmap = {v: k for k, v in hashmap.items()}

# create main window
root = Tk()
root.geometry("300x200") # Set the window size to 300x200
root.title("Rock, Paper, Scissors")

# create a function to play the game
def playGame():

    # generate a random number between 0 and 2 which corresponds to rock, paper or scissors
    computerChoice = randint(0, 2)

    # get user input and corresponding value of the user input in the hashmap
    userInput = user_choice.get()
    if userInput not in hashmap:
        messagebox.showerror("Error", "Invalid input")
        return
    userChoice = hashmap[userInput]

    # definition of winning conditions
    result = "Computer's Choice: " + inv_hashmap[computerChoice] + "\n"
    if (computerChoice == userChoice):
        result += "It's a tie!"
    elif computerChoice == (userChoice + 1) % 3:
        result += "Computer wins!"
    else:
        result += "You win!"

    messagebox.showinfo("Result", result)

# create label and entry for user input
user_choice_label = Label(root, text="Enter your choice (rock/paper/scissors): ")
user_choice = StringVar()
user_choice_entry = Entry(root, textvariable=user_choice)

# create button to play the game
play_button = Button(root, text="Play", command=playGame)

# position the elements on the window
user_choice_label.pack()
user_choice_entry.pack()
play_button.pack()

# start the main event loop
root.mainloop()
        
playGame()
                                                      
