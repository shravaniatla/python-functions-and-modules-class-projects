import random
play = True
print("Welcome to the number game number ranges from 1 to 10")
computer = random.randint(1,10)
while play:
    user = int(input("enter your guess number :"))
    if computer > user:
        print("you are low")
    elif computer < user :
        print("you are high")
    elif computer == user :
        print("you got the number")
        print("computer generated number :", computer)
        play = False
        break
        