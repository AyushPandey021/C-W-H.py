# String in details


"""harry i am ayush i am try to learn pythoon  this is multiline comment  """

#
# name = "AyushPandey "
# print(name[2:8])
# print(name[8:-1])


# string mathod

name = "Harry "  # string are immutable
a = len(name)
print(name.strip())
# print(name.capitalize())
"""uper
lower 
capitalize

"""


# text = "Apples, Bananas, Pineapples"
# print(text.split(","))
# print(",".join(['Apples','Bananas', 'pineapples']))

# String Formetting

template = "Dear {} ,you are awesome. take this {}$ bag"
a = "john"
a1 = 3200
b = "sam"
b1 = 552
c = "mac"
c1 = 10000
# s1 = template.format(c,c1)

print(f"{b} you are awesome and take this {b1}")