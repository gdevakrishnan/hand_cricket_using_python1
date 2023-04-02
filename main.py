## Hand Cricket using Python
## Developed By: Deva Krishnan

import random

# Get a value from the user
def getChoice():
    valid = 1
    while valid:
        try:
            user = int(input("Enter your choice: "))
            if (1 <= user <= 10):
                return user
                valid = 0
            else:
                print("Please Enter a valid choice\n")
        
        except:
            print("Please Enter a valid choice\n")

# Display the result
def result(score_user, score_com):
    print({True: "You won the match", False: "Com won the match"} [score_user > score_com])

# Computer batting
def com_bat(challenge):
    ball = 1
    score_com = 0
    run = [run for run in range(1, 11)]
    print("Now the com is batting")
    while ball <= 36:
        user = getChoice()
        com = random.choice(run)
        print(f"The com choice is: {com}")
        if com != user:
            score_com += com
            print(f"The Computer score is: {score_com}\n")
            ball += 1
        else:
            print(f"The Computer score is: {score_com}\n")
            result(challenge, score_com)
            break
        
        if challenge < score_com:
            print("The com won the match")
            break

# Player batting
def user_bat():
    ball = 1
    score_user = 0
    run = [run for run in range(1, 11)]
    while ball <= 36:
        user = getChoice()
        com = random.choice(run)
        print(f"The com choice is: {com}")
        if user != com:
            score_user += user
            print(f"Your score is: {score_user}\n")
            ball += 1
        else:
            print(f"Your score is: {score_user}\n")
            com_bat(score_user)
            break
    

# Game starts Here
print("Python Hand Cricket")
print("** 6 overs of match **\n")
print("You are batting")
user_bat()