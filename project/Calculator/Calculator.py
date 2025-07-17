# Calculator
try:
    a = int(input("Enter the frist number: "))
    b = int(input("Enter the Second number: "))
    print(
        "what kind of opreator do you want to perform.Press + for addition\nPress - for subtraction\npress / for division\npress * for multiplication"
    )
    o = input("Right the expression you do perform ")
    match o:
        case "+":
            print(f"Addition Perform {a+b}")
        case "-":
            print(f"Subestraction Perform {a-b}")
        case "*":
            print(f"Multiplication Perform {a*b}")
        case "/":
            print(f"Divide Perform {a/b}")

except Exception as err:
    print("Error Occured {err}")


