# # args for arguements in python 4
# # args with prameter funtions
# def sum(*args):
#     #  args will be a tuplel of all the values pased to sum
#     print(args)
#     total = 0
#     for item in args:
#         total += item
#     return total


# print(sum(5, 65, 54, 6, 4, 4)),


# # agrument use to  multiple value in perameter and performing any opreatir


# # start Kwargs
# def marks(**kwargs):
#     # kwargs is a dictionary of all the values passed value pairs which were passed to marks
#     for item in kwargs.keys():
#         print(f"the marks of {item} are {kwargs[item]}")


# marks(shubham=43, vikrant=24, jack=21, marie=40)


def func1(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


func1(1, 2, 3, name="Alice", age=30)
