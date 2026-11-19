import numpy as np

# a. Create the original array
original = np.array([1, 2, 3, 4, 5, 6])
print("a. Original array:", original)

# b. Create a slice from index 1 to 4 (exclusive of 4)
subset = original[1:4]
print("b. Subset slice:", subset)

# c. Modify the first element of subset to 999 and display both
subset[0] = 999
print("c. After modifying subset:")
print("   Subset:", subset)
print("   Original (affected because slicing creates a view):", original)

# Reset original array for clean demonstration
original = np.array([1, 2, 3, 4, 5, 6])

# d. Create another slice using .copy() and modify it
copied_array = original[1:4].copy()
copied_array[0] = 500
print("d. After modifying explicit copy:")
print("   Copied array:", copied_array)
print("   Original (unaffected because copy creates a new allocation):", original)

# e. Create 1 to 12 array and reshape it into a 3x4 matrix
matrix_3x4 = np.arange(1, 13).reshape(3, 4)
print("\ne. Reshaped 3x4 Matrix:\n", matrix_3x4)

# f. NumPy indexing and slicing extractions
print("\nf. Extractions:")
print("   First row:", matrix_3x4[0, :])
print("   Last row:", matrix_3x4[-1, :])
print("   Second column:", matrix_3x4[:, 1])
# Rows 1-2 (indices 1,2) and Columns 2-3 (indices 2,3) -> Python ranges are exclusive at the stop boundary
print("   Elements from rows 1-2 and columns 2-3:\n", matrix_3x4[1:3, 2:4])

# g. Create flattened versions using flatten() and ravel()
flattened = matrix_3x4.flatten()
raveled = matrix_3x4.ravel()
print(f"\ng. Flattened: {flattened}")
print(f"   Raveled: {raveled}")

# h. Modify an element in ravel() and observe matrix_3x4
raveled[0] = 99
print("\nh. Modifying ravel()[0] to 99...")
print("   Original 3x4 Matrix (affected because ravel returns a view whenever possible):\n", matrix_3x4)

# i. Modify an element in flatten() and observe matrix_3x4
flattened[1] = 88
print("\ni. Modifying flatten()[1] to 88...")
print("   Original 3x4 Matrix (unaffected because flatten always returns a deep copy):\n", matrix_3x4)

# j. Display metadata of the 3x4 matrix
print("\nj. Matrix Properties:")
print("   Shape:", matrix_3x4.shape)
print("   Number of dimensions (ndim):", matrix_3x4.ndim)
print("   Total size:", matrix_3x4.size)
print("   Data type (dtype):", matrix_3x4.dtype)
