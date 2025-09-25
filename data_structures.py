#  Lists, Tuples, Dictionaries

# Topics: Python data structures


# 1. Lists

print("### Lists ###")
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Access elements
print("First fruit:", fruits[0])

# Append new element
fruits.append("orange")
print("After append:", fruits)

# Remove element
fruits.remove("banana")
print("After remove:", fruits)

# Loop through list
for fruit in fruits:
    print(fruit)

# List comprehension
squared_numbers = [x**2 for x in range(1, 6)]
print("Squared numbers:", squared_numbers)
print("\n")


# 2. Tuples

print("### Tuples ###")
coords = (10, 20)
print("Coordinates tuple:", coords)

# Indexing
print("X coordinate:", coords[0])

# Unpacking
x, y = coords
print("Unpacked:", x, y)

# Tuples are immutable
# coords[0] = 5  # This will raise an error

print("\n")


# 3. Dictionaries

print("### Dictionaries ###")
student = {"name": "Aravind", "age": 24, "grade": "A"}
print("Student dictionary:", student)

# Access values
print("Name:", student["name"])

# Update value
student["age"] = 25
print("Updated age:", student["age"])

# Add new key-value
student["city"] = "Coventry"
print("Added city:", student)

# Loop through dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Nested dictionary example
students = {
    "s1": {"name": "Aravind", "grade": "A"},
    "s2": {"name": "Rahul", "grade": "B"},
}
print("Nested dictionary:", students)

# Access nested values
print("Grade of s2:", students["s2"]["grade"])

print("\n")


# 4. Mini Exercises


# 1. List of numbers: print even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)

# 2. Tuple unpacking: swap values
a, b = 5, 10
a, b = b, a
print("Swapped values:", a, b)

# 3. Dictionary: calculate average grade
grades = {"Math": 90, "Science": 85, "English": 95}
average = sum(grades.values()) / len(grades)
print("Average grade:", average)
