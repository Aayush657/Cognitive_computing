# UCS420: Cognitive Computing - Assignment 2
# Q4. Sets
# Roll number: 1024170416
# (Part numbers vi-xi follow the numbering on the assignment sheet.)

roll_no = 1024170416
digits = [int(d) for d in str(roll_no)]  # same digits as Q1, before multiplying by 10

A = {d * 7 for d in digits}
B = {d * 9 for d in digits}
print("A =", A)
print("B =", B)

# vi. Union
print("vi.   Union        A | B =", A.union(B))

# vii. Intersection
print("vii.  Intersection A & B =", A.intersection(B))

# viii. Differences
print("viii. A - B =", A.difference(B))
print("      B - A =", B.difference(A))
# difference() is one-sided (in one set but not the other); symmetric_difference() is both sides together: (A-B) | (B-A).

# ix. Symmetric difference
print("ix.   Symmetric diff A ^ B =", A.symmetric_difference(B))

# x. Subset / superset checks
print("x.    A is a subset of B?  ", A.issubset(B))
print("      B is a superset of A?", B.issuperset(A))

# xi. Remove a user-given value from A with discard()
try:
    X = int(input("xi.   Enter a value X to remove from A: "))
    print(f"      {X} {'was' if X in A else 'was not'} in A")
    A.discard(X)
    print("      A after discard:", A)
except ValueError:
    print("      Invalid input - please enter a whole number")
# discard() silently does nothing if X is missing, while remove() raises a KeyError and would crash the program.
