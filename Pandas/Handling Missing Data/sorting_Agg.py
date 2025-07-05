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
avg_salary = df['Salary'].mean()
print("Average Salary:", avg_salary)
mean_age = df['Age'].mean()
print("Mean Age:", mean_age)    
