
# print("\u25CF \u250c \u2500 \u2510 \u2502 \u2514 \u2518")

#● ┌ ─ ┐ │ └ ┘

import random

dice_art = {1 : ("┌───────────┐",
                 "│           │",
                 "│     ●     │",
                 "│           │",
                 "└───────────┘"),
            2 : ("┌───────────┐",
                 "│   ●       │",
                 "│           │",
                 "│        ●  │",
                 "└───────────┘"),
            3 : ("┌───────────┐",
                 "│     ●     │",
                 "│           │",
                 "│  ●     ●  │",
                 "└───────────┘"),
            4 : ("┌───────────┐",
                 "│  ●     ●  │",
                 "│           │",
                 "│  ●     ●  │",
                 "└───────────┘"),
            5 : ("┌───────────┐",
                 "│  ●     ●  │",
                 "│     ●     │",
                 "│  ●     ●  │",
                 "└───────────┘"),
            6 : ("┌───────────┐",
                 "│  ●  ●  ●  │",
                 "│           │",
                 "│  ●  ●  ●  │",
                 "└───────────┘")}

total = 0
dice = []
roll_num = input("Enter the number of dice you want to roll: ")

for die in range(int(roll_num)):
    dice.append(random.randint(1, 6))
print(dice)

# for die in range(int(roll_num)):
#     for line in dice_art.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()


# print(line)

for die in dice:
    total += die
print(f"The total is {total}")




