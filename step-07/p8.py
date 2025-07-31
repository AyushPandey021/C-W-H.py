#  write a program a and return a multiplication table in reversed order
n = int(input("Enter The Number: "))

for i in range(1,11):
  print(f"{n} X {11-i} = {n*(11-i)}")
