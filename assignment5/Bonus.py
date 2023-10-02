import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Use pandas to read the CSV
csvData = pd.read_csv('Data.csv', sep=',')

# Convert the pandas dataframe into a NumPy array
csvDataNum = csvData[['State', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']].to_numpy()

# Convert the NumPy array into a list of lists
data = csvDataNum.tolist()
PercentFarmerTakingLoans=[]
for i in range(len(data)):
    PercentFarmerTakingLoans.append(data[i][2])


perCapitaIncome=[]
for i in range(len(data)):
    perCapitaIncome.append(data[i][9])

MeanX=sum(PercentFarmerTakingLoans)/len(PercentFarmerTakingLoans)
MeanY=sum(perCapitaIncome)/len(perCapitaIncome)

#Calculate Pearson Correlation Coefficient
numerator=0
denominator1=0
denominator2=0
for i in range(len(data)):
    numerator+=(PercentFarmerTakingLoans[i]-MeanX)*(perCapitaIncome[i]-MeanY)
    denominator1+=(PercentFarmerTakingLoans[i]-MeanX)**2
    denominator2+=(perCapitaIncome[i]-MeanY)**2
r=numerator/((denominator1*denominator2)**0.5)
print("Pearson Correlation Coefficient is: ",r)

#create scatter plot to determine correlation
plt.scatter(PercentFarmerTakingLoans,perCapitaIncome)
plt.xlabel("Percentage of farmers taking loans")
plt.ylabel("Per Capita Income")
plt.title("Correlation between percentage of farmers taking loans and per capita income")
plt.show()

