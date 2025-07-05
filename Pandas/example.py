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
# print("Sample DataFrame:")
# print(df)
# print("Names(Siglr column):")
# name = df["Name"]
# print(name)

# #selecting multiple column
# subset = df[["Name", "Occupation", "Salary"]]
# print("Subset of DataFrame with selected columns:") 
# print(subset)

#filtering rows based on a condition
high_salary = df[df["Salary"] > 70000]
print("Rows with Salary greater than 70000:")
print(high_salary)

#now multiple conditions
high_salary_and_performance = df[(df["Salary"] > 70000) & (df["Performance"] > 75)]
print("Rows with Salary greater than 70000 and Performance greater than 75:")
print(high_salary_and_performance)