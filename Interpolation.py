#estimated value are filled automatic
import pandas as pd
data = {
    #"Name" : ['Sarthak','Ram','Ghanshyam','Jagdish','Hanu','Bhanu'],
    'Age' : [19,None,None,22,10,20],
    "Salary" : [20000,None,20000,15000,16000,30000],
    "Performance Score" : [90,None,90,91,80,70]
}

df = pd.DataFrame(data)
df['Age'] = df['Age'].interpolate()
#df.interpolate(method="linear",axis = 1,inplace=True)
print(df)
