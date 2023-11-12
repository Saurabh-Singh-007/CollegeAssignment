import pandas as pd
import csv
df=pd.read_csv("Cars93.csv")
print(df)
with open("problem1a.csv","w") as f :
    w=csv.writer(f)
    col2=df["Model"]
    col1=df.iloc[0]
    w.writerows([col1,col2])
