#adding columns
import pandas as pd
data = {
    "Name" : ['Sarthak','Ram','Ghanshyam','Jagdish','Hanu','Bhanu'],
    "Age" : [19,20,21,22,10,20],
    "Salary" : [20000,10000,20000,15000,16000,30000],
    "Performance Score" : [90,85,90,91,80,70]
}
df = pd.DataFrame(data)
df["Bonus"] = df["Salary"] * 0.1
print(df)

#using insert(loc,"column_name",some_data)
print("Using insert function")
df.insert(1,"Employee_id",[1001,1002,1003,1004,1005,1006])
print(df)