import random

# print(help(random))

# low = 1
# high = 100
# options = ["Rock", "Paper", "Scissor"]
# cards = ["k","q","j","l","a","1","2","3","4","5","6","7","8"]
# num = random.randint(low, high)
# # num = random.random()
# # option = random.choice(options)     #todo this should give a float value between low and high or 1 to 100
# random.shuffle(cards)
# print(cards) 

#todo number guessing game

low = 1
high = 100
num = random.randint(low, high)
print("Welcome to the Number Guessing Game!")
running = True
guesses = 0

while True:
    answer = int(input("Enter the number: "))
    guesses += 1

    if answer < low or answer > high:
        print("Invalid input! Please enter a number between", low, "and", high)
        continue
    elif answer < num:
        print("Too low! Try again.")
    elif answer > num:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number in", guesses)
        running = False
        break
    










