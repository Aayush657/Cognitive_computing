import numpy as np

# a) Reverse the NumPy array
arr = np.array([1, 2, 3, 6, 4, 5])
reversed_arr = arr[::-1]
print("a) Reversed array:", reversed_arr)


# b) Find the most frequent value and their indices
def find_most_frequent(arr_input):
    # bincount counts occurrences of non-negative integers
    counts = np.bincount(arr_input)
    most_frequent_val = np.argmax(counts)
    indices = np.where(arr_input == most_frequent_val)[0]
    return most_frequent_val, indices


# i. Array x
x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
val_x, idx_x = find_most_frequent(x)
print(f"b) i. For array x: Most frequent value is {val_x} at indices {idx_x}")

# ii. Array y
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
# Array y has a tie (1 and 3 both appear 3 times). Let's handle multiple modes:
counts_y = np.bincount(y)
max_count = np.max(counts_y)
modes = np.where(counts_y == max_count)[0]

for mode in modes:
    idx_y = np.where(y == mode)[0]
    print(
        f"b) ii. For array y: Most frequent value is {mode} at indices {idx_y}"
    )
