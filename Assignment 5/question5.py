import numpy as np

# 1. Create a 3x4 2D array
ucs420_your_name = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])
print("Original 3x4 Array:\n", ucs420_your_name)

# 2. Compute Statistics
print("\n--- Statistics ---")
print("Mean:", np.mean(ucs420_your_name))
print("Median:", np.median(ucs420_your_name))
print("Max:", np.max(ucs420_your_name))
print("Min:", np.min(ucs420_your_name))
print("Unique elements:", np.unique(ucs420_your_name))

# 3. Reshape array to 4 rows and 3 columns
reshaped_ucs420_your_name = ucs420_your_name.reshape(4, 3)
print("\n--- Reshaped Array (4x3) ---\n", reshaped_ucs420_your_name)

# 4. Resize array to 2 rows and 3 columns
# np.resize returns a new copy, truncating data if it doesn't fit
resized_ucs420_your_name = np.resize(ucs420_your_name, (2, 3))
print("\n--- Resized Array (2x3) ---\n", resized_ucs420_your_name)
