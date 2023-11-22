import pandas as pd
import sys

#part-a
df=pd.read_csv('Cars93.csv')
a=list(df['Model'].sort_values(ascending=True))
df=pd.DataFrame(a,columns=['Model Sorted'])
df.index=df.index+1
df.to_csv('problem1a.csv')

#part-b

df=pd.read_csv('data/Cars93.csv')
types=list(df['Type'].unique())
for i in types:
    data=df.groupby('Type').get_group(i)
    print(data[data['Price']==data['Price'].max()])
    
#part-c

if len(sys.argv)!=2:
    print('Enter Name of the Manufacturer as command line argument')

try:
    input=sys.argv[1]
    df=pd.read_csv('data/Cars93.csv')
    required_data=df[df['Manufacturer']==input]['Model']
    print(required_data)
except:
    print('Invalid Input')

#part-d
df=pd.read_csv('data/Cars93.csv')
required_data=df.groupby('Manufacturer').size().sort_values(ascending=False)
df=pd.DataFrame({'Manufacturer':required_data.index,'Count':required_data.values},index=[i for i in range(1,len(required_data)+1)])
df.to_csv('problem1d.csv')