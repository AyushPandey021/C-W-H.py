# Object orriented programming in Python
# oops is a prpogramming paradigm that uses objects and classes to structure code.which can contain data (attributed) and code (methods)
# oops strucuture of code
# class is the blueprint for your creating object


# obj is the object keyword it help to use any thing inside class to use in obj
# all classes access in object obj


class Factory:
    def __init__(self, material, zip, pocket):
        self.material = material
        self.zip = zip
        self.pocket = pocket

    def show(self):
        print(
            f"your object details are Material is : {self.material}, Pokets are :{self.pocket}, Zips are :{self.zip}"
        )


reebook = Factory("cotton", 4, 2)  # creating an object of the class Factory
compus = Factory("polystart", 14, 12)  # creating an object of the class Factory

compus.show()  # accessing the attribute of the object reebook

# this is mainly useing object orriented programming  use creating one object class and use multiple timems


# class insider varible is called atribute




# 🎉 4 piller of oops 
# Abstracting, Encapsulation, Inheritance, Polymorphism
# Inheritance is the process by which one class can inherit the attributes and methods of another class. This allows for code reuse and the creation of a hierarchy of classes.
# inherit type 
# single level inherit
# multilevel inherit





# 8:20 time 