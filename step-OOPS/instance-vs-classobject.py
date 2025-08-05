# learn oops
# class is the only one blueprint and structure in oops its define flow only🔝
class One:
    name = "Ayush"  # this is class attributes

    lenguage = "python "
    salary = 1200000

    def printInfo(self):
         # self is the instace of the class
        #  function always have one name vlaue like  this case is Self but you can change the name but not empty, its makes error
        # is called mathod to create for work easy and reuseable purpose
        print(
            f"My name is {self.name } and my salary: is {self.salary} and i am work on {self.lenguage} lenguage."
        )
#  but you are work on nomal text msg to not using a instance mathod name  like self 
# you use one mathod for this is @staticmethod its help to run your statice code only 
    @staticmethod
    def greet():
       
        print("Ram Ram Je me keh rha tha ki : ")


apdev = One()

apdev.lenguage = "javascipt"
# if you are update you class and and run so always get the instance data
# object is the Instance of a class Real-world entity.is called object.
print(apdev.name, "Salary is", apdev.lenguage)
apdev.greet()  # run the attribute
apdev.printInfo()  # run the attribute
