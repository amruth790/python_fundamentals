# File Handling

# Topics: Read/Write files, CSV, JSON, context manager

import csv
import json


# 1. Reading and Writing Text Files

print("### Text File Handling ###")

# Writing to a text file
with open("example.txt", "w") as file:
    file.write("Hello, Aravind!\n")
    file.write("This is Python file handling practice.\n")

# Reading from a text file
with open("example.txt", "r") as file:
    content = file.read()
    print("Text file content:\n", content)


# 2. CSV File Handling

print("### CSV File Handling ###")

# Writing CSV
with open("students.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age", "Grade"])
    writer.writerow(["Aravind", 24, "A"])
    writer.writerow(["Rahul", 22, "B"])

# Reading CSV
with open("students.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


# 3. JSON File Handling

print("### JSON File Handling ###")

# Writing JSON
data = {
    "students": [
        {"name": "Aravind", "age": 24, "grade": "A"},
        {"name": "Rahul", "age": 22, "grade": "B"}
    ]
}

with open("students.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent=4)

# Reading JSON
with open("students.json", "r") as jsonfile:
    loaded_data = json.load(jsonfile)
    print("JSON content:", loaded_data)


# 4. Mini Exercises


# 1. Count number of lines in example.txt
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines in example.txt:", len(lines))

# 2. Extract names from CSV and store in a list
names = []
with open("students.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        names.append(row["Name"])
print("Names from CSV:", names)

# 3. Add a new student to JSON
new_student = {"name": "Priya", "age": 23, "grade": "A"}
loaded_data["students"].append(new_student)

with open("students.json", "w") as jsonfile:
    json.dump(loaded_data, jsonfile, indent=4)

print("Updated JSON content:", loaded_data)
