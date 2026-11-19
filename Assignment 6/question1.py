import numpy as np

# Initial sensor readings
temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

# a. Add 2°C to every reading using vectorization
corrected_temp = temperature + 2
print("a. Corrected temperatures (+2°C):", corrected_temp)

# b. Convert all temperatures from Celsius to Fahrenheit
fahrenheit_temp = (9 / 5) * corrected_temp + 32
print("b. Temperatures in Fahrenheit:", fahrenheit_temp)

# c. Identify all readings greater than 32°C using Boolean indexing
# Note: Applying this to the corrected temperature array
greater_than_32 = corrected_temp[corrected_temp > 32]
print("c. Readings greater than 32°C:", greater_than_32)

# d. Count how many readings exceed 32°C
count_exceed_32 = np.sum(corrected_temp > 32)
print("d. Number of readings exceeding 32°C:", count_exceed_32)

# e. Explanation of Efficiency:
"""
e. Explanation:
Explicitly iterating through an array using a 'for' loop in Python introduces
significant overhead because Python is an interpreted language. The loop executes
at the Python layer, checking types and handling objects dynamically at each step.

Vectorization and Boolean indexing offload these computations to highly optimized,
compiled C code under the hood of NumPy. This allows operations to run at near-hardware
speeds using SIMD (Single Instruction, Multiple Data) processor instructions.
Additionally, NumPy processes continuous memory blocks, maximizing CPU cache utilization
and drastically speeding up data processing.
"""
