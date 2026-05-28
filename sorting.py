import pandas as pd
data = {
    "Name": ['Arun','Varun','Karun'],
    "Age" : [10,20,30],
    "Salary" : [1000,2000,3000]
}
df = pd.DataFrame(data)
print(df)
df.sort_values(by=["Age","Salary"],ascending=[True,True],inplace=True)
print(df)