# python_fundamentals

# 1
## Topics Covered 
- Variables and Constants
- Data Types: int, float, str, bool
- Arithmetic, Comparison, Logical, Assignment Operators
- Type Conversion

## Sample Outputs

Addition: 13
floor Division: 3
Is x equal to y? False
Is student and x>y? True
Converted string to int: 10

# 2
## Topics Covered
-if
-elif
-else
-comparison operators
-for loop
-while loop
-break
-continue
-pass


## Sample outputs

Prime numbers from 1 to 100:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 

Even/Odd check for the list: [1, 5, 8, 12, 15, 20]
1 is odd
5 is odd
8 is even
12 is even
15 is odd
20 is even


Simple Calculator
Enter first number: 6
Enter second number: 8
Choose operation (+, -, *, /): +
Result: 14.0


Enter your marks: 79
Your grade is: C



# 3
## Topics Covered
Defining functions, parameters, return values, modules, reusable code


## Sample outputs

Hello, Aravind!


Square of 5 is: 25


Aravind is 20 years old and lives in Coventry.
Rahul is 25 years old and lives in London.


Factorial of 5: 120


Area of rectangle 5x3: 15


# 4
## Topics Covered
Python data structures
 Lists, Tuples, Dictionaries

 ## Sample outputs

 ### Lists ###
Original list: ['apple', 'banana', 'cherry']
First fruit: apple
After append: ['apple', 'banana', 'cherry', 'orange']  
After remove: ['apple', 'cherry', 'orange']
apple
cherry
orange
Squared numbers: [1, 4, 9, 16, 25]


### Tuples ###
Coordinates tuple: (10, 20)
X coordinate: 10
Unpacked: 10 20


### Dictionaries ###
Student dictionary: {'name': 'Aravind', 'age': 24, 'grade': 'A'}
Name: Aravind
Updated age: 25
Added city: {'name': 'Aravind', 'age': 25, 'grade': 'A', 'city': 'Coventry'}
name: Aravind
age: 25
grade: A
city: Coventry
Nested dictionary: {'s1': {'name': 'Aravind', 'grade': 'A'}, 's2': {'name': 'Rahul', 'grade': 'B'}}
Grade of s2: B


Even numbers: [2, 4, 6]
Swapped values: 10 5
Average grade: 90.0


# 5
## Topics Covered
Read/Write files, CSV, JSON, context manager

## Sample outputs

### Text File Handling ###
Text file content:
 Hello, Aravind!
This is Python file handling practice.

### CSV File Handling ###
['Name', 'Age', 'Grade']
['Aravind', '24', 'A']
['Rahul', '22', 'B']

### JSON File Handling ###
JSON content: {'students': [{'name': 'Aravind', 'age': 24, 'grade': 'A'}, {'name': 'Rahul', 'age': 22, 'grade': 'B'}]}


Number of lines in example.txt: 2

Names from CSV: ['Aravind', 'Rahul']

Updated JSON content: {'students': [{'name': 'Aravind', 'age': 24, 'grade': 'A'}, {'name': 'Rahul', 'age': 22, 'grade': 'B'}, {'name': 'Priya', 'age': 23, 'grade': 'A'}]}



# 6
## Topics Covered 
Exception handling, logging, robust Python code

 ## Sample outputs

 ### Basic try-except ###
Enter a number: 23
You entered: 23


### Multiple Except Blocks ###
Enter numerator: 5
Enter denominator: 6
Result: 0.8333333333333334


### Finally Example ###
Hello, Aravind!
This is Python file handling practice.

This runs regardless of exception.


### Logging Example ###
Enter a number to divide 100 by: 500
Result: 0.2
Logging example complete.


### Mini ETL Simulation ###
Skipping invalid data: abc
Cleaned Data: [10, 20, 30]




# 7
## Topics Covered 
 NumPy arrays, indexing, slicing, reshaping, operations

 ## Sample outputs

1D array: [1 2 3 4 5]

2D array:
 [[1 2 3]
 [4 5 6]]
 
Zeros array:
 [[0. 0. 0.]
 [0. 0. 0.]]
 
Ones array:
 [[1. 1.]
 [1. 1.]
 [1. 1.]]
 
Array with range 0-9: [0 1 2 3 4 5 6 7 8 9]

Original 1D array: [1 2 3 4 5]
First element: 1
Last element: 5
Slice 1-3: [2 3 4]

Original 2D array:
 [[1 2 3]
 [4 5 6]]
 
Element at row 0, col 1: 2
First row: [1 2 3]
First column: [1 4]
Addition: [5 7 9]
Multiplication: [ 4 10 18]

Sum of arr_a: 6

Mean of arr_b: 5.0

Original array: [ 1  2  3  4  5  6  7  8  9 10 11 12]

Reshaped to 3x4:
 [[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
 
Flattened array: [ 1  2  3  4  5  6  7  8  9 10 11 12]

Transposed array:
 [[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]
 
Random 5x5 array:
 [[ 2  8  4 10 10]
 [ 9  0  3  7  1]
 [ 3  0 10  3 10]
 [10  4 10  5  3]
 [ 0  5  2  9  1]]
 
Sum of each row: [34 20 26 32 17]

Max value in array: 10
