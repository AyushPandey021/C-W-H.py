# Question for pratice✔️✔️
# 1.find the 1 to 50 even and odd
# for i in range(1,51):
#   if i%2==0:
#    print(f"{i} is even")
# else:
#   print(f"{i} is odd")
# 2. Find the sum of the even and odd number from 1 to n
# n = int(input("even odd add "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#   if i%2 == 0:
#     even =+i
#   else:
#     odd =+ i
#     print(f"{even}, {odd}")
# Q.3  Count the number of even and odd digit in a number.
# n = int(input("Enter a number: - "))
# even = 0
# odd = 0

# for digit in n:
#     if int(digit) % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Number of even digit", {even})
# print("Number of even digit", {odd})

# Q.4 printing mutiplication table ✔️
# n = int(input("write the number to give multiplication table :- "))
# for i in range(1,11):
#   print(f"{n} * {i} = {n*i}")
# Q.5 Reverse the number✔️
# num = input("enter a number ")
# revere = num[::-1]
# print("Reverse Number:", revere)
# give any kind of word and number
# Q. FizzBuzz Problem✔️
# for i in range(1, 51):
#     if i % 3 == 0 and 1 % 5 == 0:
#         print("fizzBuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# Q.check wether the number is prime or not.
# n = int(input("Check your number is a prime or not :-"))
# count = 0
# for i in range(1, n + 1):
#  if n%i == 0:
#     count =count+1
#  if count == 2:
#         print("prime")
#  else:
#         print("not prime")

# Q.Reversed a string  using loop
a= "yes i am apdev."
b = ""
for i in range(len(a)-1,-1,-1):
  b = b + a[i]
  print(a[i])