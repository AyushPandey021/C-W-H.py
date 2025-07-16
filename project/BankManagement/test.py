# ⏭️swap the value without add thrid variable
# a = int(input("Enter the first number (a):"))
# b = int(input("Enter the first number (b):"))
# print(f"\nBefore swap: a{a} , b={b}")
# a = a + b
# b = a - b
# a = a - b
# print(f"After swap a{a} , b={b}")
# ⏭️take  input and username , age and print  hello name your age  is age
# name = input("Enter your name :")
# age = int(input("Enter your age :"))
# print(f"hello {name}, your are {age}")
# check if a given number is even or odd.
# ⏭️Write a Python program that takes a number as input and checks whether it is even or odd.
# num = int(input("Enter a number : "))
# if num % 2 == 0:
#     print(f" {num} is Even.")
# else:
#     print(f"{num} is odd")
# ⏭️Find the maximum of three numbers using if-else.
# a = int(input("Enter frist :"))
# b = int(input("Enter two :"))
# c = int(input("Enter three :"))
# if a >= b and a >= c:
#     print(f" {a} is the largest ")
# elif b >= a and b >= c:
#     print(f"{b} is the largest ")
# if c >= a and c >= b:
#     print(f"{c} is the LargestNumber ")


#  loop
# print table⏭️
# n = int(input("write the number to return table "))
# for i in range(n, (n * 10 + 1), n):
#     print(f"{i} * {n} * {n}")
# factorial find⏭️
# num = int(input("Enter a number to find its factorial"))
# if num < 0:
#   print("its wroung not find it")
# elif num == 0 :
#   print("the factorial of 0 is 1.")
# else:
#   fact = 1
#   for i in range(1 , num + 1):
#     fact *= i
#     print(f"{fact} the factorial ")


# ⏭️ Create a function to calculate the sum of digits of a number.
# def sum(a, b):
#     {print(a + b)}


# sum(23, 453)


# ⏭️ Remove the Duplicate form list
# a = [1, 2, 3, 3, 2, 1]
# kahli = []
# for new in a:
#   if new not in kahli:
#     kahli.append(new)
# print(kahli)
# ⏭️ find second largest and frist largest
# num = [12,3,4,5,6,7,8,9,4,3]
# num = list(set(num))
# num.sort()
# print("frist largest number is :" ,num[-1], "second largest number is :" ,num[-2])
# ⏭️Merge two sorted lists into one.


# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 3, 1, 4, 7]
# i = j = 0
# mList = []
# while i < len(list1) and j < len(list2):
#     mList.append(list1[i])
#     i += 1
# else:
#     mList.append(list2[j])

# while i < len(list1):
#     mList.append[list1[i]]
#     i += 1
# while j < len(list2):
#     mList.append(list2[j])
#     j += 1

# print("marged list is ", mList)
# find the common in 2 list ⏭️
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 3, 1, 4, 7]
# common = []
# for item in list1:
#     if item in list2 and item not in common:
#         common.append(item)
# print(
#     f" the common number in list is {common}",
# )
