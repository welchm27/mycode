#!/usr/bin/env python3

# install pyfiglet using:
# pip install pyfiglet

def main():
    import random
    # importing pyfiglet module
    import pyfiglet

    welcome = pyfiglet.figlet_format("WELCOME TO MY SIMPLE GAME! HOW LONG CAN YOU SURVIVE?")
    print(welcome)

    # set player_health as a global variable to be used in functions
    global player_health
    player_health = 20
       
    # North encounters with (mon) being the monster of choice while moving towards the forest
    def n_enc(mon):
        input("On your way North to the forest, you encounter a " + mon + " moving South")
        run_fight() # execute the run_fight function on each encounter

    # South encounters with (mon) being the monster of choice while moving towards the smoke
    def s_enc(mon):
        input("On your way towards the smoke, you encounter a " + mon + " moving in to flank you")
        run_fight() # execute the run_fight function on each encounter
    
    # dice roll with (dice) being which die (D20, D10, etc...)
    def roll(dice):
        result = random.randint(1,dice) # roll from 1 to the max die choice
        return result   # return the result to be used when called

    # run fight method to offer the choice, then conduct the rolls
    def run_fight():
        global player_health    # call player_health in this function so it can be used here
        # record run or fight as rf variable
        rf = input("Do you want to 'Run' or 'Fight'? ")
        # Only move forward if there's a valid input (run or fight)
        while rf.lower() not in ["run", "fight"]:
            rf = input("Please choose only 'Run' or 'Fight': ")
        # if run is chosen
        if rf.lower() == "run":
            input("You chose to run away, hit ENTER to see if  you make it ")
            # conduct a roll and return the result in this function
            result = roll(20)
            # convert the result to a string and return it in a print
            print("You rolled a " + str(result))
            # if-else for the roll.  If above 10, you get away, if not you get attacked
            if result > 10:
                input("Congratulations, you got away!")
            else:
                input("You didn't make it, and are attacked. Hit ENTER to see how much damage you take")
                # if you didn't get away, roll a D10 to see how much damage you take
                result = roll(10)   # record the rolled amount to result
                player_health -= result # reduce player_health by the rolled result
                input("You took " + str(result) + " points of damage")  # convert result to str and display it
                print("Your new health is: " + str(player_health))  # display updated health

        # if fight is chosen
        else:
            input("FIGHT?!?! With what weapon? ")
            input("You immediately take damage, hit ENTER to see how much ")
            # you immediately move to damage, roll a D10 to see how much
            result = roll(10)   # record the rolled result
            player_health -= result # reduce player_health by the rolled result
            input("You took " + str(result) + " points of damage")  # convert result to str and display it
            print("Your health is now at " + str(player_health))    # convert player_health to str and display the new result

    # while player health is above 0, the game continues:
    while player_health > 0:
        print("Player Health: ", player_health) # display the current player's health
        input("HIT ENTER TO MOVE TO THE NEXT STEP") # explain how to move the story forward
        input("You wake up in a field with a splitting headache ")
        input("Looking around, you see a forest to the North, and smoke rising from the South ")
        # request an input (north or south) and save it to dec1
        dec1 = input("Do you go 'North' or 'South'? ")
        # if invalid entry, keep asking
        while dec1.lower() not in ["north", "south"]:
            dec1 = input("Please choose 'North' or 'South' only: ")
        # if North is chosen...
        if dec1.lower() == "north":
            # using the n_enc(mon) function, you can easily create North encounters
            n_enc("Bugbear") 
            n_enc("Troll")
            n_enc("Orc")
            n_enc("Gnoll")
            # End of the road (need to stop it somewhere)
            input("You encounter a dragon and are immediately killed!")
            input("Congrats for at least making it this far! ")
            player_health -= 20 # player_health immediately dropped

        # if South is chosen...
        else:
            # using the s_enc(mon) function, you can easily create South encounters
            s_enc("Wolf")
            s_enc("Orc")
            s_enc("Bugbear")
            s_enc("Gnoll")
            s_enc("Goblin")
            # End of the road (need to stop it somewhere)
            input("You make it to a burning town. There are monsters everywhere ")
            input("You are immediately surrounded and cut down ")
            input("Congrats though for making it this far! ")
            player_health -= 20 # player_health immediately dropped
    # when player_health no longer >0 print the below and end the game
    print("Game Over. Player defeated!")

if __name__ == "__main__":
    main()
