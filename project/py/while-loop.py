# while loop
# a = 1
# while a <= 20:
#   print(a)
#   a =a+1

# Q.2 reverse your number  normal
# a= int(input("tell your number:-"))
# rev = 0
# while a> 0:
#   rev =  rev * 10 + a%10
#   a = a //10
# print(rev)

# Q.
# a = int(input("tell your number: "))
# copy = a
# rev = 0
# while a > 0:
#   rev = rev * 10 + a %10
#   a = a //10
# if copy == rev:
#   print('its p number')
# else:
#   print("not a p number")

# Q. Guess Random Number
import random

num = random.randint(1, 11)
tries = 0
print(num)
guess = int(input("please guess your number:-"))

if num == guess:
    tries += 1
    print(f"you are right you guessed the number between 1 and 10 in {tries} tires :-")

elif num < guess:

    print("go a little lower")
    tries += 1
elif num > guess:
    print("go a little higher")
else:
    tries += 1
    print("sorry its wrong")

