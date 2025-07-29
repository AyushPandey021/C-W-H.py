# 1
# greet = input("Enter your name : ")
# print(f"Good Afternoon  {greet} ")
# 2
letter = """ Dear <|Name|>, \n
you are selected <|Date|>"""
print(letter.replace("<|Name|>","Ayush").replace("<|Date|>","03 Septempber 2025"))
 

# 3 
# finding duble spaces 

str = "Ayush is good   boy"
print(str.find("   "))


# 4
# resplace multi spaces to singal application
print(str.replace("  ",""))
 
#  5 
# \t  use for tab 

msg = "Dear Babu, \n \tThis python course is nice.  \nThanks!"

print(msg)
