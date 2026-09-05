import numpy as np

# 1. Create array from a list
arr1 = np.array([10, 20, 30, 40, 50])
print("Array from list:", arr1)

# 2. Create 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:")
print(arr2)

# 3. Array of zeros
zeros = np.zeros(5)
print("Zeros:", zeros)

# 4. Array of ones
ones = np.ones(5)
print("Ones:", ones)

# 5. Array using arange()
numbers = np.arange(1, 11)
print("Numbers:", numbers)

# 6. Array using linspace()
values = np.linspace(1, 10, 5)
print("Linspace:", values)

# 7. Identity matrix
identity = np.eye(3)
print("Identity Matrix:")
print(identity)