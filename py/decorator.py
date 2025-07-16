# # class Animal:
# #   @property
# #   def show(self):
# #      print("hello how are you ")
# # obj = Animal()
# # obj.show
# def decorate(func):
#     def wrapper(a, b):
#         print("The addition to your numver are ")
#         func(a, b)
#         print("Thankyou i hope you liked it")

#     return wrapper


# @decorate
# def addition(a, b):
#     print(f"hello total i s {a+b}")


# addition(12, 67)


# # decorator is function its works is decorate and manage your existing function
# def ap(**kwargs):
#   print(kwargs)
# ap(name="pandey",age=34)



additon = lambda a,b : a + b
print(additon(12,13))