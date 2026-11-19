import numpy as np

# Step tracking matrix (4 users x 3 days)
steps = np.array([
    [7000, 7500, 8000],
    [10000, 11000, 10500],
    [5000, 5500, 6000],
    [9000, 8500, 9500]
])

# a. Calculate the total steps recorded
total_steps = np.sum(steps)
print("a. Total steps recorded:", total_steps)

# b. Calculate the mean number of steps
mean_steps = np.mean(steps)
print("b. Mean number of steps:", mean_steps)

# c. Find the maximum and minimum values
max_steps = np.max(steps)
min_steps = np.min(steps)
print(f"c. Maximum steps: {max_steps}, Minimum steps: {min_steps}")

# d. Calculate the total steps for each day using axis=0
daily_total_steps = np.sum(steps, axis=0)
print("d. Total steps for each day (Day 1, 2, 3):", daily_total_steps)

# e. Calculate the total steps for each user using axis=1
user_total_steps = np.sum(steps, axis=1)
print("e. Total steps for each user (User 1, 2, 3, 4):", user_total_steps)

# f. Find the user/day position containing the maximum number of steps using argmax()
flat_max_idx = np.argmax(steps)
# Convert flat index back to 2D coordinates (row, col)
user_idx, day_idx = np.unravel_index(flat_max_idx, steps.shape)
print(f"f. Maximum steps position: Row {user_idx} (User {user_idx+1}), Column {day_idx} (Day {day_idx+1})")
