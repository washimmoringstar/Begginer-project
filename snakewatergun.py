import random
''' A simple implementation of the Snake-Water-Gun game. 
The rules are as follows:
1 for snake 2 for water 3 for gun'''
computer = random.randint(1,3)
user = int(input("Enter 1 for snake, 2 for water, 3 for gun: "))
youdict = {1: "snake", 2: "water", 3: "gun"}

print(f"You chose {youdict[user]}")
print(f"Computer chose {youdict[computer]}")

if user == computer:   
    print("It's a tie!")
elif (computer == 2 and user == 1):
    print("You win!")
elif (computer == 1 and user == 2):
    print("You lose!")
elif (computer == 1 and user == 3):
    print("You win!")
elif (computer == 3 and user == 1):
    print("You lose!")  
elif (computer == 3 and user == 2):
    print("You win!")
elif (computer == 2 and user == 3):
    print("You lose!")
else:
    print("Something went wrong!")
