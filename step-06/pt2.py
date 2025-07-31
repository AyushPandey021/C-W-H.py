p1 = "Make a lot of Money"
p2 = "buy now New course"
p3 = "Subescribe this and win more prizes"
p4 = "click this"
message = input("Enter your Comment:")
if (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):

    print("This comment is a spam ")
else:

    print("This comment is not a spam")
