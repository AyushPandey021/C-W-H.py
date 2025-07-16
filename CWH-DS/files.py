f = open("./CWH-DS/ap.txt", "r")
b = open("./CWH-DS/dev.txt", "w")
string = """
hey dev army i am developement gonee
 his favorite pakege is pandas """
content = f.read()

content2 = b.write(string)

print(content, content2)
f.close()
b.close()
