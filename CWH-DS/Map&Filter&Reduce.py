# MAP  and filter and  Reduce is the higher order funtion in python 
# use map 
# map meanly use for you use list every element to performing work to use map 
"""number = [1,2,3,4,5,6,7]
def sqauare(x):
  return x * x 
new =list(map(sqauare,number))
print( "mutliple  the number ",new)

"""

#  filter
# if you filter the values to use filter like you have a one list and  1 to 5 number is here to fiter only even number so you use filter to filter the all even number in your list 
"""
def greater(x):
  if x>9:
    return True
  else:
    return False
a= [1,3,5,4,7,524,52,473,43,74,574,35,32,5]
new =list(filter( greater,a))
print("all number here to greater tham 9",new)

"""
# Reduce
#  total the all list value and oen result only to use reduce , reduce  given one ans 
# its help to combine all items
# from functools import reduce
number = [1,2,3,4,5,6]
# [3,3,4,5,6]
# [6,4,5,6]
# [10,5,6]
# [15,6]
# [21]
def sum(a,b):
 return a + b 
c=reduce(sum,number)
print("Reduced vavlue ",c)







