# practice one
# store the info of programmer 
class Programmer:
  company = "Google"
  def __init__(self,name,salary ,pin):
    self.name= name
    self.salary= salary
    self.pin = pin
p = Programmer("Ayush", 120000,42852)
print(p.name,p.salary,p.pin,p.company)
r = Programmer("Ritik", 1800000,42082)
print(r.name,r.salary,r.pin,r.company)
  
