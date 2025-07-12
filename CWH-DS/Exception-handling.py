# Exception handling is called  Error handling
# How to handle error

"""
while True:
    try:
        a = int(input("Enter Number 1 : "))
        b = int(input("Enter Number 2 : "))
        print(f"The Total sum is {a / b}")
    # except Exception as e :
    #     # print("Some error Occurred!")  # simple message
    #     print("Some error Occurred!",e)  #error in detailed to use
    except ValueError:
        print("print don't perform  bad typecaste ")

    except ZeroDivisionError:
        print("hey dont divide by 0 ")
    except Exception as e:
        print("Unknow error occurred", e)
       """

# javascript error handle by TRY CATCH block but
# PYTHON error handling with TRY and Except


# else and finally in the exception



# the exception work on devision state type tpe first number and type second number if you type second number is 0 so given the error "DIVISON BY ZERO" if you right , right number so code excutes no issue 
"""def divide(a,b):
  try:
    c = a / b
    print(c)
    return c
  except Exception as e:
    print(e)
    return None
    #  this finally is always excuted no metter if try completely excutes or not
#  finally:
#     print("this is always excuted ")
a = int(input("Enter Number 1 : "))
b = int(input("Enter Number 2 : "))
divide(a,b)

"""
