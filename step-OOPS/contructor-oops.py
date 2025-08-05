# ⭐⭐
# Costructor in oops and understanding the  __init__()
class Student:
    name = "Ayush"
    btach = 234
    clg = "MCU Bhopal"
    stream = "B.C.A"

    def __init__(
        self, name, btach, stream
    ):  # dunder mathod which is autometically colled ,no colling
        self.name = name
        self.stream = stream
        self.btach = btach  # its use to you put The value in perameter and acess .
        print(
            f"Hey my name is  {self.name}  i join the course {self.stream}, and batch no is {self.btach} university name is {self.clg}"
        )

    # def printFull(self):


info = Student("yash ", "Ai/Ml", 345)  # perametersied values put
# if your vlaue already give it  and give the value in perameter so its updated your perameter value has been print

info
