import random

options = ["rock", "paper", "scissor"]
running = True

print("Welcome to the Rock Paper Scissor Game!")
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
         player = input("Please enter a valid option: ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
            print("It's a tie!")
    elif player == "Rock" and computer == "Paper":
            print("You lose!")
    elif player == "Paper" and computer == "Scissor":
            print("You lose!")
    elif player == "Scissor" and computer == "Rock":
            print("You lose!")
    else:
            print("You win!")
    if not input("Do you want to play again? (y/n) ").lower().startswith("y"):
            running = False
print("Thanks for playing!")








