# UCS420: Cognitive Computing - Assignment 2
# Q3. Random numbers (seeded with roll number)
# Roll number: 1024170416

import random
from collections import Counter

roll_no = 1024170416
random.seed(roll_no)  # same seed -> same "random" list every run, unique to this roll number

# i. 100 random numbers between 100 and 900 (randint includes both ends)
numbers = [random.randint(100, 900) for _ in range(100)]
print("i.   Numbers:", numbers)

# ii. Odd numbers
odds = [n for n in numbers if n % 2 != 0]
print(f"\nii.  Odd numbers (count = {len(odds)}):", odds)

# iii. Even numbers
evens = [n for n in numbers if n % 2 == 0]
print(f"\niii. Even numbers (count = {len(evens)}):", evens)


# iv. Prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


assert [n for n in range(30) if is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # quick self-check

primes = [n for n in numbers if is_prime(n)]
print(f"\niv.  Prime numbers (count = {len(primes)}):", primes)

# v. Most frequent number(s) - lists all of them if there is a tie
counts = Counter(numbers)
max_count = max(counts.values())
most_frequent = [n for n, c in counts.items() if c == max_count]
print(f"\nv.   Most frequent number(s): {most_frequent} - occurs {max_count} times")
