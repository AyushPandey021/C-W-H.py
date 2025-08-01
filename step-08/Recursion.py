"""
Factotrial(1)= 1
Factotrial(1)= 2 x 1
Factotrial(1)=3 x 2 x 1
Factotrial(1)= 4 x 3 x 2 x 1 
Factotrial(1)= 5 x 4 x 3 x 2 x 1
factorial(n) = n x n-1 X....3 x 2 x 1
factorial(n) = n * factorial(n-1)


"""


# recursion
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)


n = int(input("Enter your Number "))
