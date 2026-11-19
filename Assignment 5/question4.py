import numpy as np

# Replace 'Your_Name' with your actual name variable
your_name = np.linspace(10, 100, 25)
print("Array details:")
print("Dimensions (ndim):", your_name.ndim)
print("Shape:", your_name.shape)
print("Total elements (size):", your_name.size)
print("Data type (dtype):", your_name.dtype)
print("Total bytes consumed:", your_name.nbytes)

# Transpose using reshape() attribute
# Transposing a 1D array of shape (25,) requires converting it to a 2D shape like (25, 1) or (1, 25)
reshaped_transpose = your_name.reshape(-1, 1)
print("\nTranspose using reshape(-1, 1):\n", reshaped_transpose)

# Can we do the same with the .T attribute?
print("\nCan we use .T on 1D directly?")
print(
    "No, using your_name.T on a true 1D array returns the exact same 1D array: ",
    your_name.T.shape,
)
print(
    "To make .T work like a matrix transpose, we must first add an axis, e.g., your_name[np.newaxis, :].T"
)
