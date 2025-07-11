# Advansed Python
def decorator(func):
    def wrapper():
        print("I am about to print hello...")
        func()
        print("I have printed this function...")

    return wrapper


@decorator
def say_hello():
    print("hello")


f = decorator(say_hello)
f()


# decorator is a funtion that takes a funtion it creates a new funtion inside its body wrapper than it return that new funtion

# decorator is  also work with arguments


def repreat(n):
    def decrator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
            return wrapper
            return decorator


@repreat(2)
def say_hello(a):
    print(f"hello {a}")


"""def decrator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
            return wrapper"""

say_hello("ayush")
