import pandas as pd
data ={
    "Name": ["John", "Jane", "Doe", "Alice", "Bob"],
    "Occupation": ["Engineer", "Doctor", "Artist", "Scientist", "Teacher"],
    "Salary": [70000, 80000, 60000, 90000, 50000],
    "Age": [28, 34, 45, 29, 40],
}
df = pd.DataFrame(data)
print(df)
df.sort_values(by="Salary", ascending=False, inplace=True)  # Sort by Salary in descending order
print(df)  