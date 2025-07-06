# loops
# types of loops only 2 types of loops
# for loop
# while loop

# 1st
# positive loop✔️
# for a in range(1,13 ):
#   print(a)
# # reverse nagitive loop
# for i in range(-12,-10,-1):
#   print(i)


#  tabel✔️
# for i in range(7,71,7):
#     print(i)
# any number table print✔️
# n = int(input("which table you want ?"))
# for i in range(n,(n*10+1),n):
#    print(i)

# a = "Ayush is to starting Praticeing python"


# loops questions✔️
# give the number and name  print it
# n = int(input("please tell your number :-"))
# for i in range(n,0):
#     print("hello word")
# natural number✔️
# for i in range(1,n+1):
#     print(i)
# negitive number
# for i in range(n,0,-1):
#     print(i)


# printing a table ✔️
# n = int(input("which table you want :- "))
# for i in range (1,11):
#   print(f"{n} * {i} = {n*i}")
# find factorial✔️
# n = int(input("please tell your number to find fectorial:- "))
# fact = 1
# for i in range(1,n+1):
#  fact = fact * i
#  print(f"your factorial is {fact}")
# sum of number ✔️
# n = int(input("please tell your number to find fectorial:- "))
# sum = 0
# for i in range(1, n + 1):
#     sum = sum + i
# print(f"sum of number {sum}")


# sum even and odd numbers in a range seprately✔️
# n = int(input("sum to even and odd :-"))
# even = 0
# odd = 0
# for i in range(1, n + 1):
#     if 1 % 2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
#     print(f"your values even and odd sum {even},{odd}")
# ✔️find factors  the number devid by any number to and is 0 so its factor of given number
# n = int(input("which number factors you want :-"))
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)
# ✔️accpect the number and check if it a perfect number or not a number whose sum of factor is equal to the number itself

n = int(input("plese tell your number is perfect or not:- "))
sum = 0
for i in range( 1,n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print("perfect")
else:
    print("not perfect")
