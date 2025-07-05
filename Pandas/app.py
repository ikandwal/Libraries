import pandas as pd
from openpyxl.workbook import Workbook
# reading the file
# df= pd.read_csv("sales_data_sample.csv", encoding = "latin1")
# df= pd.read_excel("SampleSuperstore.xlsx", engine='openpyxl')
# df = pd.read_json("sample_Data.json")
# print(df)

data = {
    "Name": ["John", "Jane", "Doe"],
    "Age": [28, 34, 45],
    "City": ["New York", "Los Angeles", "Chicago"] 
}
df=pd.DataFrame(data)
print(df)
# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
