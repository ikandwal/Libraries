import pandas as pd
data ={
    "Name": ["John", "Jane", "Doe", "Alice", "Bob"],
    "Occupation": ["Engineer", "Doctor", "Artist", "Scientist", "Teacher"],
    "Salary": [70000, 80000, 60000, 90000, 50000],
    "Age": [28, 34, 45, 29, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "Performance": [85, 90, 78, 88, 92],
}
df = pd.DataFrame(data)
print(df)

# Adding a new column 'Bonus' which is 10% of the 'Salary'
print("New column 'Bonus' added, which is 10% of Salary:")
df['Bonus'] = df['Salary'] * 0.1
print(df)

# using insert method
# df.insert(loc,"column", some data)
df.insert(0, "ID", [1, 2, 3, 4, 5, 6,7,8])
print(df)