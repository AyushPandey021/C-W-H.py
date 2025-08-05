# frist project
# game snake,water ,gun game
"""
1 for snake
-1 for water 
0 for gun 

"""
import random

computer = random.choice([-1, 0, 1])

youstr = input("Enter Your Choice (s/w/g): ")
youDict = {"s": 1, "w": -1, "g": 0}

reverseDict = {1: "Snake ", -1: "Water", 0: "Gun"}

you = youDict[youstr]
# you enter your value and computer value also
print(f"You choose {reverseDict[you]} \n Computer Chose {reverseDict[computer]}")


if computer == you:
    print("It's a draw!")
elif (
    (computer == -1 and you == 1)
    or (computer == 1 and you == 0)
    or (computer == 0 and you == -1)
):
    print("You Win 🥳")
else:
    print("You lose😭")


# shorten way of same  program✅✅b
# if (computer - you) == -1 or (computer - you) == 2:
#     print("you lose")
# else:
#     print("You Wiin")
