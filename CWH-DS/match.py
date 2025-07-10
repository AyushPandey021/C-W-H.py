# match
a = int(input("Enter a Number between 1 and 10: "))

match a:
  case 1: 
     print("You Won a charger🎉 ")
  case 3: 
    print("you won $4🎉")
  case 4: 
     print("you won Bike🎉")
 
  case _:
      print("better luck same time")
 