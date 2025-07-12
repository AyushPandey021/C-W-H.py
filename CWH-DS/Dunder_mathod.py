# Understandig a dunder mathod
# his colled magic dunder mathod in python
# use is like in double underscore at the beginning and the end of thier name
# e.g. = __init__ , __str__, __add__
#  all doule underscore mathod is called MAGIC CLASSES
class Employee:
    company = "AP"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"

    def __repr__(self):
        return f"name: {self.name}\nsalary: {self.salary} its form repr"

    def __len__(self):
        return len(self.name)


e = Employee("Harry", 45745)
print(len(e))
# print(e.name, e.salary)
# print(str(e))
# print(repr(e))


# its about of MAGIC CLASSES  IS classed DUNDER mathod 