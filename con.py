import pandas as pd
df_customer = pd.DataFrame({
    "CustomerID" :[1,2,3],
    "Name" : ['Sar','Har','Mar']
})
df_order = pd.DataFrame({
    "CustomerID" :[4,5,6],
    "Order_Amount" :[250,450,650]
})
df_concate = pd.concat([df_customer,df_order],axis = 0,ignore_index= True)
print(df_concate)
dfCon = pd.concat([df_customer,df_order],axis= 1,ignore_index=True)
print(dfCon)