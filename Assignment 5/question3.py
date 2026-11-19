import numpy as np

# Creating the 2D array correctly
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# NumPy uses 0-based indexing
# a) Access 1st row (index 0), 2nd column (index 1)
elem_a = arr[0, 1]
print("a) Element at 1st row, 2nd column:", elem_a)

# b) Access 3rd row (index 2), 1st column (index 0)
elem_b = arr[2, 0]
print("b) Element at 3rd row, 1st column:", elem_b)
