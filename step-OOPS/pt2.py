# pratice set 2
# calculator
# find square ,cube , sqareroot 
class Calculator():
  def __init__(self,n):
      self.n = n
  def sqauare(self):
    print(f"The Square of value is:",{self.n*self.n}
     )
  def cube(self):
    print(f"The Square of value is:",{self.n*self.n*self.n}
     )
  def squareroot(self):
    print(f"The Square of value is:",{self.n**1/2}
     )
a = Calculator(4)
a.sqauare()
a.squareroot()
a.cube()
