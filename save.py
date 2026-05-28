import pandas as pd
data = {
    "Name" : ['Ram','Shyam','Sarthak'],
    "Age" : [19,20,30],
    "City" : ['Nagpur','Delhi','Raipur']
}
df = pd.DataFrame(data)
print(df)
df.to_excel("output.xlsx",index= False)