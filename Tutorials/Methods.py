# functions either preform a task or return a value, preforming a task means returning None
# parameter is the input for the function while the argument is what you pass through the function when calling it
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


def get_greeting(name):
    return f"Hi {name}"


greet("Jake", "Ryan")
greet("John", "Smith")


# cannot use method overloading in python so setting the optional one equal to a value like None is a way to make an optional parameter
# ALL OPTIONAL PARAMETERS COME AFTER REQUIRED ONES
def increment(number, by=1):
    return number + by


print(increment(2, by=1))
print(increment(2))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
