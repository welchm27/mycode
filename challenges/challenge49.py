#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

def main():
    import random

    num= random.randint(1,100)

    rounds= 0

    guess= ""
    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit():
            guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            rounds + 1

        elif guess < num:
            print("Too low!")
            rounds + 1

        else:
            print("Correct!")
    
if __name__ == "__main__":
    main()
