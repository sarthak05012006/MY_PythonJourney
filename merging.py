import pandas as pd
df_customer = pd.DataFrame({
    "CustomerID" :[1,2,3],
    "Name" : ['Sar','Har','Mar']
})
df_order = pd.DataFrame({
    "CustomerID" :[1,2,4],
    "Order_Amount" :[250,450,650]
})
df_merged = pd.merge(df_customer,df_order,on="CustomerID",how= "inner")
print(df_merged)
df_merged = pd.merge(df_customer,df_order,on="CustomerID",how= "outer")
print(df_merged)
df_merged = pd.merge(df_customer,df_order,on="CustomerID",how= "left")
print(df_merged)
df_merged = pd.merge(df_customer,df_order,on="CustomerID",how= "right")
print(df_merged)
