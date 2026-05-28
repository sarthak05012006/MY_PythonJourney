import pandas as pd
data = {
    "Name" : ['Sarthak','Ram','Ghanshyam','Jagdish','Hanu','Bhanu'],
    "Age" : [19,20,21,22,10,20],
    "Salary" : [20000,10000,20000,15000,16000,30000],
    "Performance Score" : [90,85,90,91,80,70]
}
print("UPDATED DATAFRAM")
df = pd.DataFrame(data)
df.loc[2,"Salary"] = 55000
print(df)

print("Increasing Salary by 0.5 % : ")
df["Salary"] = df["Salary"] * 1.05
print(df)