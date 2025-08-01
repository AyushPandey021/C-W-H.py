# pattern program 2
n = int(input("Enter your Num"))
for i in range(1, n + 1):
    print(" *" * i, end="  ")
    print(" ")

# patttern program 3

"""
*****
*   *
*****
"""
n1 = int(input("Enter your Num: "))

for i in range(1, n1 + 1):
    if i == 1 or i == n1:
        # First and last line - print full stars
        print("*" * n1)
    else:
        # Middle lines - print star, spaces, then star
        print("*" + " " * (n1 - 2) + "*")

# print( "*" * i,end="")
# print()
