

"""
 OOPS is a basically a way to model what wwe write in a program to ral world
 its  way of programing based  and creatinf objects 
 its easyly manage and maintain also reuseable 
mainly 4 pillar in OOPS 
=> Abestration = write a code very easyly without without any line of only write and use 
=>Encapsulation= cover all things in one bandle 
=>Inheritance => borrow the vlaue
=>Polymorphism= mean that code looking like same sounds like same but its work diffrently
"""
#  what is a card 
# object : specific instance create form the template 
# class Employee:
#   company="Apple"
#   def salary(self):
#    return 34000
# e2 = Employee()
# print(e2.salary())


# constructor
class Employee:
  def __init__(self,salary,name,bond):
    pass
def get_salary(self):
   return self.salary
def get_info(self):
  print(f"the name of the employee is {self.name}. Salary is {self.salary}")
e1=Employee(34000,"Ayush", 4)
print(e1.salary())