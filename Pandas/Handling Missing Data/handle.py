import pandas as pd
data ={
    "Name": ["John",None , "Doe", "Alice", "Bob"],
    "Occupation": ["Engineer",None, "Artist", "Scientist", "Teacher"],
    "Salary": [70000, None, 60000, 90000, 50000],
    "Age": [28, None, 45, 29, 40],
    "City": ["New York", None, "Chicago", "Houston", "Phoenix"],
    "Performance": [85, None, 78, 88, 92]
}
df = pd.DataFrame(data)
print("Original DataFrame with Missing Values:")
print(df)
#print("Removig missing values:")
# print(df.dropna(inplace=True))  # Remove rows with any missing values
# print(df)
# print("Filling missing values with a specific value:")
# df.fillna(0,inplace=True)  # Fill missing values with 0
# print(df)
df['Age'].fillna(df['Age'].mean(), inplace=True)  # Fill missing values in 'Age' with the mean
print("Filling missing values in 'Age' with the mean:") 
print(df)