# rigth a program find greatest in three number 
a = 213
b = 43
c = 422
def greatestFind(a,b,c):
  if(a>b & a>c):
    print("A is Greater.")
  elif(a<b & b>c):
    print("B is Greater.")
  elif(c>a & b<c):
    print("C is Greater.")



greatestFind(a,b,c)


