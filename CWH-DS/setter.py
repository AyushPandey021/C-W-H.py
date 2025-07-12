# Advanced python topic is here name is
# Getter and setter
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name


e = Employee("Jack doe", 34555)
# print(e.first_name())
# e.set_first_name("john")
# print(e.name)
# e.project= 6
# print(e.project)
print(e.first_name)
e.first_name = "john"
print(e.name)

# getter use for get the data and understand properly  to use getter
# setter perfrom to the set the data managet the data properly to use setter
