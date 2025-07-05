import pandas as pd
data ={
    "Name": ["John",'Jane' , "Doe", "Alice", "Bob"],
    "Salary": [70000, None, 60000, 90000, 50000],
    "Age": [28, None, 45, 29, 40],
    "City": ["New York", None, "Chicago", "Houston", "Phoenix"],
    "Performance": [85, None, 78, 88, 92]
}
df = pd.DataFrame(data)
print(df)
df.interpolate(method='linear',axis =0,  inplace=True)  # Interpolate missing values