import numpy as np

# Inputs
y = np.array([40, 65, 30, 85])
X = np.array([
    [6, 50, 9],
    [7, 60, 7],
    [5, 45, 6],
    [4, 30, 8]
])

# a. Display shape and dimensions of X
print("a. X Shape:", X.shape)
print("   X Dimensions:", X.ndim)

# b. Calculate X.T and explain
X_T = X.T
print("\nb. Transpose X.T:\n", X_T)
"""
Explanation: The transpose swaps the rows and columns of X.
In the context of the data, while each row of X represented a specific user's features,
each row of X.T now isolates a specific feature (Row 0 = Sleep hours, Row 1 = Activity level,
Row 2 = Stress level) across all users.
"""

# c. Calculate the matrix product: X.T @ X
XTX = X_T @ X
print("\nc. Matrix Product (X.T @ X):\n", XTX)

# d. Calculate the matrix inverse using np.linalg.inv()
XTX_inv = np.linalg.inv(XTX)
print("\nd. Inverse Matrix (X.T @ X)^-1:\n", XTX_inv)

# e. Implement the Ordinary Least Squares equation: beta = (X.T @ X)^-1 @ X.T @ y
beta = XTX_inv @ X_T @ y
print("\ne. Calculated OLS Coefficients (beta):", beta)

# f. Explain what the resulting coefficients represent
"""
f. Coefficient Explanation:
The array contains 3 values [beta_0, beta_1, beta_2] mapping directly to the features:
1. beta_0 (Sleep hours): Weight impact of sleep duration on the assistance score.
2. beta_1 (Activity level): Weight impact of daily physical activity on the score.
3. beta_2 (Stress level): Weight impact of psychological stress on the score.

Each coefficient details how much the predicted assistance score changes when that
specific feature increases by 1 unit, keeping all other features constant.
"""

# g. Predict assistance score for a new user
new_user = np.array([5, 40, 7])
predicted_score = new_user @ beta
print(f"\ng. Predicted assistance score for new user {new_user}: {predicted_score:.2f}")
