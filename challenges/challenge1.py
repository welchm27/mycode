#!/usr/bin/env python3

"""Challenge: Shebang, input, print, concatenate, variables """

def main():

    ## Objective: Write a script that contains the following:
    ## An input asking the user's name.
    user_name = input("Please enter your name: ")
    
    ## An input asking what day of the week it is.
    week_day = input("What day of the week is it? ")
    
    ## A print statement that reads:
    ## Hello, <name>! Happy <day of the week>!
    ## print("Hello, " + user_name +"!" + " Happy " + week_day + "!")
    print(f"Hello, {user_name}! Happy {week_day}!")

    ## No cheating... print has to use both inputs, and no "hard coding in" your name and the day in your print function :)
    
    ## BONUS POINTS: no white space weirdness in your output!
if __name__ == "__main__":
    main()
