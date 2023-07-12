#!/usr/bin/env python3

def main():

    # define round
    round = 0

    # make code run until I break it
    while True:
        ## increase round each time it loops
        round = round + 1

        # add the question to the screen
        print('Finish the movie title, "Monty Pythong\'s The Life of ______"')
        # get user guess
        answer = input("Your guess--> ")

        # check if answer is correct print 'Correct' and break out of loop
        if answer == 'Brian':
            print('Correct')
            break
        # if 3 guesses have been made, give the answer and break out of loop
        elif round == 3:
            print('Sorry, the answer was Brian.')
            break
        # if the answer is wrong and less than 3, keep trying
        else:
            print('Sorry! Try again!')


if __name__ == "__main__":
    main()
