# importing random module
import random

# creating variable for attempts
turn = 1

# creating random number between 1 and 100
randInt = random.randint(1,100)

#enabling try and except feature to prevent error or Application crashing
try:
    # loop for user input
    while True:
        
        # taking input from user as integer
        userNum = int(input("Enter Number Between 1 to 100: "))

        # checking the conditions 
        if userNum < randInt:
            print("Enter Greater Number")
            turn += 1
        elif userNum > randInt:
            print("Enter Smaller Number")
            turn += 1
        
        # breaking loop after guessing the number
        else:
            print(f"You Guessed it! in {turn} attempts")
            print(f"Number was: {randInt}")
            break;

# if error occured
except Exception as e:
    print(f"Some Error Occured: {e}")
