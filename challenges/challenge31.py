#!/usr/bin/env python3
import random


def main():
    ## list 1 defined
    wordbank = ["indentation", "spaces"]

    ## list 2 defined
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    ## append 4 to wordbank
    wordbank.append(4)
    ## print(wordbank)
    
    ## include an input asking for a number between 0 and 20, saved as variable <num>
    ## make sure it's an int
    ## num = int(input("Please provide a number between 0 and 20: "))
    
    ## get the size of tlgstudents minus 1 to give the correct end location
    max = int(len(tlgstudents))-1
    print("The max number in the list is: " + str(max))

    ## return a random number between 0 and 20 instead
    num = int(random.randrange(0,max))
    print(f"Random number is: {num}")

    ## use integer <num> to slice one of the elements from the list <tlgstudents>
    ## save the name returned as <student_name>
    student_name = tlgstudents[num]
    ## print(student_name)

    ## using elements from <tlgstudents> list and the <student_name> string, print the output:
    ## <student_name> always uses <4> <spaces> to indent.
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")
if __name__ == "__main__":
    main()
