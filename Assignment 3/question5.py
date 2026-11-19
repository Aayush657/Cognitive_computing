# Question 5
import pandas as pd

# Dataset from Question 4
csv_path='Iris.csv'
dataf=pd.read_csv(csv_path)

# Part 1
dataf.drop(3,axis=0,inplace=True)
print(dataf)

# Part 2
print(dataf.drop(dataf.columns[2],axis=1,inplace=False))
