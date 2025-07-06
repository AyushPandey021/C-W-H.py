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
n = int(input("write the number to give multiplication table :- "))
for i in range(1,11):
  print(f"{n} * {i} = {n*i}")