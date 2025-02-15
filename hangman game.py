import random

words = ["apple", "banana", "cherry", "date",
         "elderberry", "fig", "grape", "honeydew",
         "jackfruit", "kiwi", "lemon", "mango",
         "nectarine", "orange", "papaya", "pineapple",
         "plum", "quince", "strawberry", "watermelon"]

hangman_art = {0: ("     ",
                   "     ",
                   "     ",
                   "     "),
               1: ("     ",
                   "  O  ",
                   "     ",
                   "     "),
               2: ("     ",
                   "  O  ",
                   "  |  ",
                   "     "),
               3: ("  0  ",
                   " /|  ",
                   "     ",
                   "     "),
               4: ("  0 ",
                   " /|\\",
                   "     ",
                   "     "),
               5: ("  0  ",
                   " /|\\",
                   " /   ",
                   "     "),
               6: ("  0  ",
                   " /|\\",
                   " / \\",
                   "     ")}

def display_man(word_guessed):
    for line in hangman_art[word_guessed]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_ans():
    pass

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    word_guessed = 3
    guessed_ans = set()
    is_running = True

    while is_running:
        display_man(word_guessed)
        display_hint(hint)
        guessed_ans = input("Guess a letter: ").lower()

        # if guess in guessed_ans:
        #     print("You already guessed that letter!")
        #     continue
        # if guess in answer:
        #     word_guessed += 1
        #     for i in range(len(answer)):
        #         if answer[i] == guess:
        #             hint[i] = guess
        #         if "_" not in hint:
        #             print("You won!")
        #             is_running = False
        #             break


    # tries = 6
    # print(hangman_art[tries])
    # print(" ".join(hint))
    # while True:
    #     guess = input("Guess a letter: ").lower()
    #     if guess in guessed_ans:
    #         print("You already guessed that letter!")
    #         continue
    #     elif guess not in answer:

    if __name__ == "__main__":
        main()
