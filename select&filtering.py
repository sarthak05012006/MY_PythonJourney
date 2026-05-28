import pandas as pd
data = {
    "Name" : ['Sarthak','Ram','Ghanshyam','Jagdish','Hanu','Bhanu'],
    "Age" : [19,20,21,22,10,20],
    "Salary" : [20000,10000,20000,15000,16000,30000],
    "Performance Score" : [90,85,90,91,80,70]
}
df = pd.DataFrame(data)
print("Sample DataFrame : ")
print(df)
print("Sinhgle coloumn return series")
single_col = df["Name"]
print(single_col)
print("Multiple Coloumns")
multi_col = df[["Age","Salary","Age"]]

print("filtering the data :")
print("Single condition")
high_salary = df[df["Salary"] > 15000]
print(high_salary)

print("Multiple condition :")
filtered = df[(df["Age"] > 20) & (df["Salary"] > 15000)]
print(filtered)