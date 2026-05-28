import pandas as pd
data = {
    "Name" : ['Sarthak','Ram','Ghanshyam','Jagdish','Hanu','Bhanu'],
    "Age" : [19,None,21,22,10,20],
    "Salary" : [20000,None,20000,15000,16000,30000],
    "Performance Score" : [90,None,90,91,80,70]
}
df = pd.DataFrame(data)
df.fillna(0,inplace=True)
print(df)
#df['Age'] = df['Age'].fillna(df['Age'].mean())
#df.fillna({'Age': df['Age'].mean()}, inplace=True)

print(df)