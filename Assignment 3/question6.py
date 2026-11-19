# Question 6
import pandas as pd

datar = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

d = pd.DataFrame(datar)

# Save as CSV
d.to_csv("employees.csv", index=False)

print(d)

print(d.shape)

print(d.info())

print(d.describe())

print(d.head())
print(d.tail())

print(d["Salary"].mean())

print(d["Bonus"].sum())

print(d["Age"].min())

print(d["Rating"].max())

d_sorted = d.sort_values(by="Salary", ascending=False)

print(d_sorted)

def categorize_rating(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"

d["Performance"] = d["Rating"].apply(categorize_rating)

print(d)

print(d.isnull().sum())

d.rename(columns={"Employee_ID": "ID"}, inplace=True)

print(d)

print(d[d["Years_of_Experience"] > 5])

print(d[d["Department"] == "IT"])

d["Tax"] = d["Salary"] * 0.10

print(d)

d.to_csv("employees_modified.csv", index=False)
