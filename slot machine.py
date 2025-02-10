
import random

def spin_row():
    symbols = ['🍕', '🥫', '🥐', '🍞']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def payout_row(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍕':
            return bet * 10
        elif row[0] == '🥫':
            return bet * 5
        elif row[0] == '🥐':
            return bet * 2
        elif row[0] == '🍞':
            return bet * 1
    return 0


def main():
    balance = 100
    print("Welcome to the slot machine!")

    while balance > 0:
        print("Your balance is ",(balance))
        bet = input("How much would you like to bet?: ")
        if not bet.isdigit():
            print("Please enter a valid amount!")
            continue
        bet = int(bet)
        if bet > balance:                                                            #todo without the bet = int(bet) you will get error at > because you cannot right if without defining the bet varibable as int or str
            print("You don't have enough money to make this bet!")
            continue
        elif bet <= 0:
            print("You must bet a positive amount!")
        else:
            print("you've bet $", bet, "on this round")
            break


    balance -= bet
    row = spin_row()
    # print(row)
    print_row(row)

    payout = payout_row(row, bet)
    if payout > 0:
        print("You won $", payout)
    else:
        print("You lost!")

    balance += payout
    print("Your balance is: ", balance)
    return main()
    # play_again = input("Would you like to play again? (y/n): ")
    # if play_again.lower() != 'y':
    #     print("Thanks for playing!")
    #     return
    # else:
    #     return main()
# print("Thanks for playing!")

if __name__  == "__main__":
    main()

