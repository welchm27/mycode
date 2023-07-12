#!/usr/bin/env python3

def main():
    # initialize the round and answer variables
    round =0
    answer = " "

    while round < 3 and answer.lower() != "brian":
        round +=1 # increase count by 1
        answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
        if answer.lower() == "brian":  # if the correct answer is given
            print("Correct")
        elif answer.lower() == "shrubbery":
            print("You gave the super secret answer!")
            break
        elif round == 3: # if we reach 3 tries
            print("Sorry, the correct answer is Brian.")
        else:    # if an incorrect answer is given and < 3 rounds
            print("Sorry. Try again!")


if __name__ == "__main__":
    main()
