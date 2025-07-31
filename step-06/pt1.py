mark1 = int(input("Enter Marks 1: "))
mark2 = int(input("Enter Marks 2: "))
mark3 = int(input("Enter Marks 3: "))

# check for total percentage
total_percentage = (100*(mark1 + mark2 + mark3) )/ 300

if total_percentage >= 40 and mark1>33 and mark2>33 and mark3>33:
    print("you are passed:🥳 ", total_percentage )

else:
    print("you failed, try  again next year!", int(total_percentage))