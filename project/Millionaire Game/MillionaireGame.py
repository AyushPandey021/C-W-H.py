questions = [
    ["Who is Virat Kohli?", "Footballer", "Cricketer", "Plumber", "Actor", 2],
    ["Who is Amitabh Bachchan?", "Singer", "Actor", "Politician", "Doctor", 2],
    ["Who is Lionel Messi?", "Cricketer", "Footballer", "Actor", "Chef", 2],
    ["Who is Sachin Tendulkar?", "Actor", "Footballer", "Cricketer", "Singer", 3],
    ["Who is Shah Rukh Khan?", "Actor", "Cricketer", "Politician", "God", 1],
    ["Who is Lord Krishna?", "Actor", "God", "Singer", "Cricketer", 2],
    ["Who is Taylor Swift?", "Singer", "Actor", "Cricketer", "God", 1],
    ["Who is Elon Musk?", "Scientist", "Businessman", "Actor", "God", 2],
]
prizes = [
    "₹1,000",
    "₹2,000",
    "₹5,000",
    "₹10,000",
    "₹20,000",
    "₹40,000",
    "₹60,000",
    "₹80,000",
    "₹1,00,000",
    "₹1,60,000",
]
i = 0
for questions in questions:

    print(questions[0])
    print(f"a. {questions[1]}")
    print(f"b. {questions[2]}")
    print(f"c. {questions[3]}")
    print(f"d. {questions[4]}")

    # check whethet the ans is correct or not
    a = int(input("Enter your answer , 1 for a, 2 for b, 3 for c, 4 for d\n : "))
    if questions[5] == a:
        print(" Correct Answer ✔️ 🎉")
    else:
        print(f"incorrect , the correct answer was {questions[5]}")
        print("Better luck next time")
        break

    print(f"You won {prizes[i]}")
    i += 1
