# find the factorial
int = int(input("Enter the number"))
fact = 1
for i in range(1, int + 1):
    fact = fact * i
print(f"this {int} number factorial is {fact}")
