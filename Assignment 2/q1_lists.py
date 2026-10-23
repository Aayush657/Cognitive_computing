# UCS420: Cognitive Computing - Assignment 2
# Q1. Lists
# Roll number: 1024170416

roll_no = 1024170416

# i. Extract each digit of the roll number and multiply it by 10
L = [int(d) * 10 for d in str(roll_no)]
print("i.   L =", L)

# ii. Add two numbers: one with append(), one with insert()
L.append(55)
print("ii.  After append(55)   :", L)
# append() added 55 at the END of the list; length went from 10 to 11.

L.insert(2, 25)
print("     After insert(2, 25):", L)
# insert() placed 25 at index 2; every element from the old index 2 onward shifted one place right (length 12).

# iii. Remove two elements: one with remove(), one with pop()
L.remove(0)
print("iii. After remove(0)    :", L)
# remove() deletes the FIRST occurrence of the value 0 (it works by value, not position).

popped = L.pop()
print(f"     After pop() -> {popped}:", L)
# pop() with no index removes and returns the LAST element.

# iv. Sort ascending, then descending
L.sort()
print("iv.  Ascending :", L)
L.sort(reverse=True)
print("     Descending:", L)

# v. Slicing: first three and last three elements
print("v.   First three:", L[:3])
print("     Last three :", L[-3:])

# vi. List comprehension: elements greater than the average of L
avg = sum(L) / len(L)
above_avg = [x for x in L if x > avg]
print(f"vi.  Average = {avg:.2f} -> elements above average:", above_avg)
