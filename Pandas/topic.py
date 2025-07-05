import pandas as pd
data ={
    "Name": ["John", "Jane", "Doe", "Alice", "Bob"],
    "Occupation": ["Engineer", "Doctor", "Artist", "Scientist", "Teacher"],
    "Salary": [70000, 80000, 60000, 90000, 50000],
    "Age": [28, 34, 45, 29, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}
df = pd.DataFrame(data)
print(df)
print(f'Shape:{df.shape}')
print(f'Columns Name:{df.columns}')