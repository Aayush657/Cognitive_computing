# UCS420: Cognitive Computing - Assignment 2
# Q2. Tuples
# Roll number: 1024170416

roll_no = 1024170416
L = [int(d) * 10 for d in str(roll_no)]  # the list L from Q1 (before any changes)

scores = tuple(L[:8])
print("scores =", scores)

# i. Highest score with its index; lowest score with its count
highest = max(scores)
lowest = min(scores)
print(f"i.   Highest score = {highest} at index {scores.index(highest)}")
print(f"     Lowest score  = {lowest}, appears {scores.count(lowest)} time(s)")

# ii. Reverse the tuple and return the result as a list
reversed_scores = list(scores[::-1])
print("ii.  Reversed (as a list):", reversed_scores)
# Tuples are immutable, so they have no in-place reverse(); slicing [::-1] builds a NEW reversed sequence instead.

# iii. Search for a score entered by the user
try:
    target = int(input("iii. Enter a score to search for: "))
    if target in scores:
        print(f"     {target} is present - first occurrence at index {scores.index(target)}")
    else:
        print(f"     {target} is not present in the tuple")
except ValueError:
    print("     Invalid input - please enter a whole number")

# iv. Try to change an element directly
try:
    scores[0] = 100
except TypeError as e:
    print(f"iv.  {type(e).__name__}: {e}")
# Tuples are immutable, so their items cannot be reassigned after creation; a list is mutable and would accept L[0] = 100.

# v. Unpack into first, second and the remaining scores
first, second, *rest = scores
print(f"v.   first = {first}, second = {second}, rest = {rest}")
