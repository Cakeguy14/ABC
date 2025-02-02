
import random

def spin_row():
    return [row for row in range(3)]

def print_row():
    pass

def payout_row():
    pass

def main():
    balance =100
    symbols = ['🍕','🥫','🥐','🍞']
    bet = (input("How much would you like to bet?: "))
    print("Welcome to the slot machine!")

    while balance > 0:
        print("Your balance is:"(balance))
        continue
    if bet > balance:
        print("You don't have enough money to make this bet!")
        continue
    elif bet <= 0:
        print("You must bet a positive amount!")
    elif bet < balance:
        print("you've bet $", bet, "on this round")

    bet = int(bet)
    balance -= bet
    row = spin_row()
    print_row(row)

    payout = payout_row(row)
    balance += payout
    print("Your balance is:", balance)

print("Thanks for playing!")

