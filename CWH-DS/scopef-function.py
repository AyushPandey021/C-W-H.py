def sum(a, b):
    # a and b are a local variable  without funtion is not accpectable
    c = a + b
    z = 1
    return c


print(sum(4, 6))

print(sum(4, 6))
z = 8  # this is a global varible any buddy can access it
print(z)


#  any code inside the funtion so is called logal varible and not access anymore
# local is accessible only within the funtion


def ap(a, b):
    print("hey i am summing ")
    c = a + b
    global z  # please modify global z

    z = 0  # this will refer to global z and not create a local variable
    return c


z = 3
print(sum(3, 12))
print(z)

# can you modified the global varible its ans is :- yes i can but using global keyword


#  🙋‍♂️Docstring =Wtiting funtion Documentation
# Docstings are used to document funtion classes and modules
# its meanly called a document strig like string and write document usein comment

def add(a, b):
    """Return the sum of two number"""
    c = a + b
    return c

print(sum._doc)
# docsting is a normal funtion but its add the comment on and code and defining all code flow 
