# loops and conditions
#topics: if, elif, else, comparision operators, for loops,while loops, break,continue , pass


# prime numbers from 1 to 100

print("Prime numbers from 1 to 100:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  # exit inner loop if divisible
    if is_prime:
        print(num, end=" ")
print("\n")



# 2. Even/Odd Number Checker


numbers = [1, 5, 8, 12, 15, 20]
print("Even/Odd check for the list:", numbers)
for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
print("\n")


# 3. Simple Calculator


print("Simple Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == '+':
    print("Result:", a + b)
elif operation == '-':
    print("Result:", a - b)
elif operation == '*':
    print("Result:", a * b)
elif operation == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")
print("\n")




# 4. Nested if-else Example

marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
else:
    grade = 'F'

print("Your grade is:", grade)