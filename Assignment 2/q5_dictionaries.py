
my_dict = {
    "name": "Aayush",     
    "roll_no": "1024170416",
    "branch": "CSE",  
    "age": 18,                 
    "city": "Patiala",      
}
MY_CGPA = 8.5                
# -----------------------------------------------------------------

original = my_dict.copy()  # kept for parts vii and viii, which use the original 5 keys
print("Original:", my_dict)

# i. Rename "city" to "location" (works for any dictionary that has a "city" key)
my_dict["location"] = my_dict.pop("city")
print("i.    ", my_dict)

# ii. Add "cgpa"
my_dict["cgpa"] = MY_CGPA
print("ii.   ", my_dict)

# iii. Increase "age" by 1
my_dict["age"] += 1
print("iii.  ", my_dict)

# iv. Delete "branch" in two separate copies: pop() and del
copy_pop = my_dict.copy()
removed = copy_pop.pop("branch")
print(f"iv.   pop() returned {removed!r} ->", copy_pop)

copy_del = my_dict.copy()
del copy_del["branch"]
print("      del            ->", copy_del)
# pop() removes the key AND returns its value; del is a statement that just deletes the key and returns nothing.

# v. Iterate with .items()
print("v.")
for key, value in my_dict.items():
    print(f"      {key} → {value}")

# vi. Safe access to a key that may not exist
if "email" in my_dict:
    print("vi.   email:", my_dict["email"])
else:
    print("vi.   'email' key not found - no email on record")

# vii. Merge with a friend's (fictional) dictionary
friend_dict = {
    "name": "Arjun Mehta",
    "roll_no": "1024170999",
    "branch": "COE",
    "age": 20,
    "city": "Chandigarh",
}
merged = {**original, **friend_dict}
print("vii.  Merged:", merged)
# When both share a key, the value from the dictionary unpacked LAST (friend_dict here) wins.

# viii. Keep only the pairs whose value is a string
string_values = {k: v for k, v in original.items() if isinstance(v, str)}
print("viii. String values only:", string_values)
