import random

computer = random.choice([-1 , 0 , 1])

yourstr = input("Enter your choice(s for snake, w for water, g for gun): ")
yourDict = {"s":1 , "w":-1 , "g":0}
reverseDict = {1: "Snake" , -1: "Water" , 0: "Gun"}
you = yourDict[yourstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You win!")

    else:
        print("You lose!")  