import pandas as pd
data = {
    "Name" : ['Sarthak','Ram','Ghanshyam','Jagdish','Hanu','Bhanu'],
    "Age" : [19,20,21,22,10,20],
    "Salary" : [20000,10000,20000,15000,16000,30000],
    "Performance Score" : [90,85,90,91,80,70]
}
df = pd.DataFrame(data)
print(df)
#df.drops(coloumns=["coloumn_name"], inplace = True)
df = df[df['Salary']<15000]
#df.drop(columns=["Performance Score"],inplace = True)
print(df)

