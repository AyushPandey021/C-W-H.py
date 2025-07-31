# calculate the student grade

grade = int(input("enter your marks: "))
if grade >= 90 or grade == 100:
    print(" Your Grade is : Ex-A+")
elif grade >= 80 or grade == 90:
    print(" Your Grade is : A")
elif grade >= 70 or grade == 80:
    print(" Your Grade is : B")
elif grade >= 60 or grade == 70:
    print(" Your Grade is : C")
elif grade > 50 or grade == 60:
    print(" Your Grade is : D")
elif grade < 50:
    print(" Your Grade is : F")
else:
    print("Wrong Input")
