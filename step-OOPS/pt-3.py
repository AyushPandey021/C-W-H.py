# create a class with a class attribute a create an object form it and set 'a'
class Demo:
    
    a = 4


o = Demo()
print(o.a)  # print the class attribute because instance attribute  is not present

o.a = 0  # instance attribute is set

print(o.a)  # print the instance attribute because instancce attrbute is present
print(Demo.a)# print the class attribute 