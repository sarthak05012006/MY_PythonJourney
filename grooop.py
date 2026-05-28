import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Age" : [19,20,21,22,10,20],
    "Salary" : [20000,10000,20000,15000,16000,30000],
    "Performance Score" : [90,85,90,91,80,70]
}
df = pd.DataFrame(data) 
print(df)
grouped_data = df.groupby('Age')['Salary'].sum()
print(grouped_data)