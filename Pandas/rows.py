import pandas as pd
df=pd.read_json("sample_Data.json")
print("Displaying the 10 rows first")
print(df.head(10))
print("Displaying the 10 rows last")
print(df.tail(10))