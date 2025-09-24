#  Functions & Modules
# Topics: Defining functions, parameters, return values, modules, reusable code



# 1. Function Example

def greet(name):
    """Function to greet a user"""
    print(f"Hello, {name}!")

greet("Aravind")
print("\n")


# 2. Function with Parameters and Return

def square(num):
    """Returns the square of a number"""
    return num ** 2

result = square(5)
print("Square of 5 is:", result)
print("\n")


# 3. Function with Default & Keyword Arguments

def describe_person(name, age=20, city="Coventry"):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person("Aravind")
describe_person("Rahul", age=25, city="London")
print("\n")


# 4. Recursive Function Example

def factorial(n):
    """Returns factorial of n using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
print("\n")



# Function to calculate area of rectangle
def rectangle_area(length, width):
    return length * width

print("Area of rectangle 5x3:", rectangle_area(5, 3))
