import pandas as pd
import csv
df=pd.read_csv("Cars93.csv")
print(df)
df1=pd.DataFrame({"Model Sorted":list(df["Model"].sort_values())})
df1.index=df1.index+1
df1.to_csv("problem1ai.csv")

df2=pd.DataFrame(df.groupby('Type').get_group('Small'))
df1.to_csv("problem1aii.csv")
