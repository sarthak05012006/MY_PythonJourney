import pandas as pd
data = {
    "Age" : [19,20,21,22,10,20],
    "Salary" : [20000,10000,20000,15000,16000,30000],
    "Performance Score" : [90,85,90,91,80,70]
}
df = pd.DataFrame(data) 
print(df)
print("Avg Age : ")
print(df["Age"].mean())
print("Min Age is :")
print(df["Age"].min())
print("Max age is : ")
print(df["Age"].max())
print("Sum of Age is :")
print(df["Age"].sum()) 