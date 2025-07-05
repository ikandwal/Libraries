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

# .loc[]
# df.loc[row_index, column_name] = new_value
df.loc[0, "Salary"] = 75000  # Update John's salary
print(df)
df['salary'] = df['Salary'] * 1.05  # Increase all salaries by 10%
print(df)
