import pandas as pd
data = {
    "Name" : ['Sarthak',None,'Ghanshyam','Jagdish','Hanu','Bhanu'],
    "Age" : [19,None,21,22,10,20],
    "Salary" : [20000,None,20000,15000,16000,30000],
    "Performance Score" : [90,None,90,91,80,70]
}
df = pd.DataFrame(data)
print(df)

print(df.isnull())
print(df.isnull().sum())
#to remove the none values
#df.dropna(inplace = True)
print(df)
df.dropna(axis = 1,inplace= True)
print(df)