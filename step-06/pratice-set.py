# find the greator number value given by user
A1 = int(input("Enter 1 no: "))
A2 = int(input("Enter 2 no: "))
A3 = int(input("Enter 3 no: "))
A4 = int(input("Enter 4 no: "))

if A1 > A2 and A1 > A3 and A1 > A4:
    print("A1 is Greater Number")
elif A2 > A1 and A2 > A3 and A2 > A4:
    print("A2 is Greater Number")
elif A3 > A2 and A3 > A1 and A3 > A4:
    print("A3 is Greater Number")
elif A4 > A2 and A4 > A1 and A4 > A3:
    print("A4 is Greater Number")
else:
    print("invaild input ")
