# Error Handling & Logging

# Topics: Exception handling, logging, robust Python code

import logging


# 1. Basic try-except

print("### Basic try-except ###")
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter an integer.")
print("\n")


# 2. Multiple Except Blocks

print("### Multiple Except Blocks ###")
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = x / y
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Enter numeric values.")
print("\n")


# 3. Finally Block

print("### Finally Example ###")
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("This runs regardless of exception.")
print("\n")


# 4. Logging Basics

print("### Logging Example ###")
logging.basicConfig(filename="app.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

try:
    num = int(input("Enter a number to divide 100 by: "))
    result = 100 / num
    print("Result:", result)
    logging.info(f"Division successful: 100 / {num} = {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    logging.error("Attempted division by zero.")
except ValueError:
    print("Invalid input!")
    logging.warning("Non-integer input provided.")
finally:
    print("Logging example complete.")
print("\n")


# 5. Mini Exercise: ETL-style simulation

print("### Mini ETL Simulation ###")
data = ["10", "20", "abc", "30"]
cleaned_data = []

for item in data:
    try:
        number = int(item)
        cleaned_data.append(number)
    except ValueError as e:
        logging.warning(f"Skipping invalid data: {item}")
        print(f"Skipping invalid data: {item}")
print("Cleaned Data:", cleaned_data)
