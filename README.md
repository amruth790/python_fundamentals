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


# 8
## Topics Covered 
Pandas Series, DataFrames, CSV loading, data exploration

# Sample Outputs
### Pandas Series ###
Series:
 0    10
1    20
2    30
3    40
4    50
dtype: int64


Series with custom index:
 a    10
b    20
c    30
d    40
e    50
dtype: int64
First element: 10
Element with index 'c': 30


### Pandas DataFrame ###
DataFrame:
       Name  Age Grade
0  Aravind   24     A
1    Rahul   22     B
2    Priya   23     A


Names column:
 0    Aravind
1      Rahul
2      Priya
Name: Name, dtype: object

First row:
 Name     Aravind
Age           24
Grade          A
Name: 0, dtype: object


### Load CSV ###
CSV loaded DataFrame:
       Name  Age Grade
0  Aravind   24     A
1    Rahul   22     B
2    Priya   23     A


First 2 rows:
       Name  Age Grade
0  Aravind   24     A
1    Rahul   22     B

Last row:
     Name  Age Grade
2  Priya   23     A


Info:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2


Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    3 non-null      object
 1   Age     3 non-null      int64
 2   Grade   3 non-null      object
dtypes: int64(1), object(2)
memory usage: 204.0+ bytes
None


Summary statistics:
            Name   Age Grade
count         3   3.0     3
unique        3   NaN     2
top     Aravind   NaN     A
freq          1   NaN     2
mean        NaN  23.0   NaN
std         NaN   1.0   NaN
min         NaN  22.0   NaN
25%         NaN  22.5   NaN
50%         NaN  23.0   NaN
75%         NaN  23.5   NaN
max         NaN  24.0   NaN


Name and Age columns:
       Name  Age
0  Aravind   24
1    Rahul   22
2    Priya   23

Students with grade A:
       Name  Age Grade
0  Aravind   24     A
2    Priya   23     A

Added City column:
       Name  Age Grade        City
0  Aravind   24     A    Coventry
1    Rahul   22     B      London
2    Priya   23     A  Manchester

Average age: 23.0


# 9
 # Topics covered
 Handling missing values, duplicates, formatting, replacing invalid data

 # Sample outputs
 Original DataFrame:
       Name   Age Grade        City
0  Aravind  24.0     A    Coventry
1    Rahul   NaN     B      London
2     None  23.0     C  Manchester
3    Priya  22.0  None      London
4  Aravind  24.0     A    Coventry


Missing values per column:
 Name     1
Age      1
Grade    1
City     0
dtype: int64



  df["Grade"].fillna("Unknown", inplace=True)
DataFrame after filling missing values:
       Name    Age    Grade        City
0  Aravind  24.00        A    Coventry
1    Rahul  23.25        B      London
2  Unknown  23.00        C  Manchester
3    Priya  22.00  Unknown      London
4  Aravind  24.00        A    Coventry


DataFrame after removing duplicates:
       Name    Age    Grade        City
0  Aravind  24.00        A    Coventry
1    Rahul  23.25        B      London
2  Unknown  23.00        C  Manchester
3    Priya  22.00  Unknown      London



       Name    Age    Grade        City
0  ARAVIND  24.00        A    Coventry
1    RAHUL  23.25        B      London
2  UNKNOWN  23.00        C  Manchester
3    PRIYA  22.00  Unknown      London



  df_no_duplicates["Grade"].replace("Unknown", "F", inplace=True)

       Name    Age Grade        City
0  ARAVIND  24.00     A    Coventry
1    RAHUL  23.25     B      London
2  UNKNOWN  23.00     C  Manchester
3    PRIYA  22.00     F      London


  df_no_duplicates["Pass"] = df_no_duplicates["Grade"].isin(["A", "B", "C"])
Added Pass column:
       Name    Age Grade        City   Pass
0  ARAVIND  24.00     A    Coventry   True
1    RAHUL  23.25     B      London   True
2  UNKNOWN  23.00     C  Manchester   True
3    PRIYA  22.00     F      London  False



DataFrame after index reset:
       Name    Age Grade        City   Pass
0  ARAVIND  24.00     A    Coventry   True
1    RAHUL  23.25     B      London   True
2  UNKNOWN  23.00     C  Manchester   True
3    PRIYA  22.00     F      London  False
