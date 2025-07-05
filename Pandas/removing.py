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
#removing column
print("Removing column 'Performance'")
df.drop(columns=["Performance"],inplace=True)
print(df)
