# Data structure
# List,Tuple,Dictionary,Set
# a = [12, 13, 14, 15, 16.5]
# mathod to traverse the value
# .append for adding number
# a[1]=23
# # 1st way using index
# print(a)

# l = [-45, 67, 12, -70, -4, 34]
# print("Possitve elements are")
# for i in a:
#     if i >= 0:
#         print("nagitive elements are")
#         for i in l:

#             if i < 0:
#                 print(i)


# find the greatest element and print its index

# l = [1, 2, 4, 5, 7, 8, 969, 8, 97, 6, 5]
# lergest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > lergest:
#         lergest = l[i]
#         index = i

# print(f"your largest number is {lergest} at index is {index}")

# Q Second Lergest Number  and leargest number
# l = [12, 16, 13, 19,90]
# lergest = l[0]
# sec_lergest = l[0]
# for i in l:
#     if i > lergest:
#         sec_lergest = lergest
#         lergest = i
#     elif i > sec_lergest:
#          sec_lergest = i
# print(sec_lergest,lergest)
# Q check if list are sorted or not
a = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        continue
    else:
        print("your list is not sorted ")
    break
else:
    print("your list is sorted")


# 5:16 time  Tuple
