# class Employee:
# instance method (default)
class Employee:

    def print_info(self, a, b):
        info = f"the name is {self.name } and the salary is {self.salary}"
        print(info)

    @staticmethod
    def sum(a, b):
        return a + b

    # class mathod
    @classmethod
    def print_company(cls):
        print(cls.company)

e1 = Employee("Jack", 23433)
e2 = Employee("hill", 34523)
e1.print_info()
e2.print_info()
print(e2.sum(1, 3))
#  this is called intance mathod
# 