#!/usr/bin/env python3
"""NDE Course | Alexandra
   Applying if, else, elsif in a script"""

round = 0
answer = " "

while round < 3 and (answer != "Brian" and answer != "Shrubbery"):
    round += 1     
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    answer = answer.capitalize()
    if answer == "Brian": 
        print("Correct!")
        break
    elif round == 3:    
        print("Sorry, the answer was Brian.")
        break
    else:                 
        print("Sorry. Try again!")

