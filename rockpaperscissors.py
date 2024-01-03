from random import randint

def playGame():
    # create hashmap that maps rock, paper and scisscors to value 0, 1, 2
    hashmap = {
    "rock":     0,
    "paper":    1,
    "scissors": 2
    }

    # inverse hashmap
    inv_hashmap = {v: k for k, v in hashmap.items()}

    # generate a random number between 0 and 2 which corresponds to rock, paper or scissors
    computerChoice = randint(0, 2)

    # get user input and corresponding value of the user input in the hashmap
    userInput = input("Enter your choice (rock/paper/scissors): ")
    userChoice = hashmap[userInput]

    # definition of winning conditions
    print("Computers Choice: " + inv_hashmap[computerChoice])
    if (computerChoice == userChoice):
        print("It's a tie!")
    elif computerChoice == (userChoice + 1) % 3:
        print("Computer wins!")
    else:
        print("You win!")
        
playGame()
                                                      
