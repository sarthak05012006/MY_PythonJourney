import pandas as pd

data = {
    "Time" : [1,2,3,4,5,6],
    "Value" : [10,None,30,40,None,60]
}
df = pd.DataFrame(data)
print(df)
df['Value'] = df['Value'].interpolate()
print(df)
