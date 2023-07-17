#!/usr/bin/env python3

# define the main function
def main():
    with open("dracula.txt", "r") as foo:  #using with to open dracula.txt as "r"ead only and set it to foo
        with open("vampirelines.txt","w") as vamp:
            # loop over every line in dracula.txt
            count = 0   # start at 0 to count the lines returned
            for line in foo:
                #print(line)  # print each line
                #if "vampire" in line:  # check if the word vampire is in the line
                if "vampire" in line.lower():  # update above line to include all variations of the word vampire
                    print(line)  # print any returned lines
                    count += 1
                    vamp.write(line)
            print(f"There are {count} lines that contain the word 'vampire'")


if __name__ == "__main__":
    main()
