# NumPy Basics

# Topics: NumPy arrays, indexing, slicing, reshaping, operations

import numpy as np


# 1. Creating NumPy Arrays

arr1 = np.array([1, 2, 3, 4, 5])
print("1D array:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", arr2)

# Array of zeros
zeros = np.zeros((2, 3))
print("Zeros array:\n", zeros)

# Array of ones
ones = np.ones((3, 2))
print("Ones array:\n", ones)

# Array with range
range_arr = np.arange(10)
print("Array with range 0-9:", range_arr)


# 2. Array Indexing & Slicing

print("Original 1D array:", arr1)
print("First element:", arr1[0])
print("Last element:", arr1[-1])
print("Slice 1-3:", arr1[1:4])

print("Original 2D array:\n", arr2)
print("Element at row 0, col 1:", arr2[0, 1])
print("First row:", arr2[0, :])
print("First column:", arr2[:, 0])


# 3. Array Operations

arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])

print("Addition:", arr_a + arr_b)
print("Multiplication:", arr_a * arr_b)
print("Sum of arr_a:", np.sum(arr_a))
print("Mean of arr_b:", np.mean(arr_b))


# 4. Reshaping Arrays

arr = np.arange(1, 13)  # 1D array
print("Original array:", arr)
arr_reshaped = arr.reshape(3, 4)
print("Reshaped to 3x4:\n", arr_reshaped)

# Flatten back to 1D
arr_flat = arr_reshaped.flatten()
print("Flattened array:", arr_flat)

# Transpose
print("Transposed array:\n", arr_reshaped.T)


# 5. Mini Exercises

# 1. Create a 5x5 array of random integers (0-10)
rand_arr = np.random.randint(0, 11, (5, 5))
print("Random 5x5 array:\n", rand_arr)

# 2. Sum of each row
print("Sum of each row:", np.sum(rand_arr, axis=1))

# 3. Maximum value in array
print("Max value in array:", np.max(rand_arr))
