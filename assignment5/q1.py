
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Use pandas to read the CSV
csvData = pd.read_csv('Data.csv', sep=',')

# Convert the pandas dataframe into a NumPy array
csvDataNum = csvData[['State', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']].to_numpy()

# Convert the NumPy array into a list of lists
data = csvDataNum.tolist()

#Function to calculate population density
def PopDensity(data):
    pop=[]
    for i in range(len(data)):
        pop.append(data[i][6])
    print("Maximum population density is: ", max(pop))
    print("Minimum population density is: ", min(pop))
    print("Average population density is: ", sum(pop)/len(pop))
    print("Median population density is: ", sorted(pop)[len(pop)//2])
    print("Mode of population density is: ", max((pop), key=pop.count))
    return pop

#Function to calculate marginal farmers
def MarginalFarmers(data):
    MarginalFarmers=[]
    for i in range(len(data)):
        MarginalFarmers.append(data[i][7])
    print("Maximum marginal farmers are: ", max(MarginalFarmers))
    print("Minimum marginal farmers are: ", min(MarginalFarmers))
    print("Average marginal farmers are: ", sum(MarginalFarmers)/len(MarginalFarmers))
    print("Median marginal farmers are: ", sorted(MarginalFarmers)[len(MarginalFarmers)//2])
    print("Mode of marginal farmers are: ", max((MarginalFarmers), key=MarginalFarmers.count))
    return MarginalFarmers

#Function to calculate percentage women in workforce
def women_in_workforce(data):
    women_in_workforce=[]
    for i in range(len(data)):
        women_in_workforce.append(data[i][11])
    print("Maximum percentage women in workforce are: ",max(women_in_workforce))
    print("Minimum percentage of women in workforce are: ",min(women_in_workforce))
    print("Average percentage of women in workforce are: ",sum(women_in_workforce)/len(women_in_workforce))
    print("Median percentage of women in workforce are: ",sorted(women_in_workforce)[len(women_in_workforce)//2])
    print("Mode percentage of women in workforce are: ",max((women_in_workforce),key=women_in_workforce.count))
    return women_in_workforce 

PopDensity(data)
MarginalFarmers(data)
women_in_workforce(data)


x=[]
y=[]
z=[]
for i in range(len(data)):
    x.append(data[i][4])
    y.append((data[i][5])*100)
    z.append(data[i][0])
width=0.2
p=np.arange(len(data))
p1=[j+width for j in p]

plt.bar(z,x,width=width,color='black',label="Percenage Area with >30 percent slope")
plt.bar(p1,y,width=width,color='red',label="Road Density*100")
plt.xlabel('States',fontsize=14)
plt.xticks(rotation=40)
plt.legend()
plt.show()

perArea30=[]
roadDen=[]
states=[]
for i in data:
    perArea30.append(i[4])      #loop for adding values to the following lists

perArea30.sort()
for i in perArea30:
    for j in data:
        if i in j:
            roadDen.append(j[5])
            states.append(j[0])

xValues=np.arange(len(roadDen))
plt.bar(xValues,roadDen,width=0.4,label='road density')
plt.xticks(xValues,states,rotation='vertical')              #rotating the x-axis labels by 90 degrees and setting the x-axis labels
plt.xlabel('States',fontsize=24)
plt.ylabel('road density',fontsize=24)
plt.title('Road density in increasing order of percentage area with slope > 30%',fontsize=24)
plt.legend()
plt.show()







