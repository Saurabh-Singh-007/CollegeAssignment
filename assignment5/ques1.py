import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
csvData = pd.read_csv('Data.csv', sep = ',')
csvDataNum = csvData[['State', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']].to_numpy()
data = csvDataNum.tolist()

# a 
# i) Data Assessment of Population Density
def populationDensity(data) : 
    highestState = lowestState = ''
    median = avg = mode = highestPopulation = lowestPopulation = 0
    pDensity = []
    for i in range(len(data)) : 
        list = data[i]
        if list[6] > highestPopulation : 
            highestPopulation = list[6]
            highestState = list[0]
        if i == 0 : 
            lowestPopulation = list[6]
            lowestState = list[0]
        if list[6] < lowestPopulation : 
            lowestPopulation = list[6]
            lowestState  = list[0]
        pDensity.append(list[6])
    avg = sum(pDensity) / (i + 1)
    pDensity.sort()
    median = (pDensity[5] + pDensity[6]) / 2

    highestFreq = 0
    pDensitySet = set(pDensity)
    for element in pDensitySet : 
        freq = pDensity.count(element)
        if highestFreq < freq : highestFreq = freq
    
    print('The state with highest Population Density is', highestState)
    print('The state with lowest Population Density is', lowestState)
    print('The median Population Density of all States is', median)
    print('The average Population Density of all States is', avg)
    if highestFreq == 1 : print("No modal Population Density . . .")
    else : 
        print("The mode(s) of Population Density is/are : ", end = '')
        for element in pDensitySet : 
            if pDensity.count(element) == highestFreq : print(element, end = ', ')
        print('\b\b ')

# ii) Data Assessment of Percentage of Marginal Farmers
def marginalFarmers(data) : 
    highestState = lowestState = ''
    median = avg = mode = highestPercentage = lowestPercentage = 0
    mFarmers = []
    for i in range(len(data)) : 
        list = data[i]
        if list[7] > highestPercentage : 
            highestPercentage = list[7]
            highestState = list[0]
        if i == 0 : 
            lowestPercentage = list[7]
            lowestState = list[0]
        if list[7] < lowestPercentage : 
            lowestPercentage = list[7]
            lowestState  = list[0]
        mFarmers.append(list[7])
    avg = sum(mFarmers) / (i + 1)
    mFarmers.sort()
    median = (mFarmers[5] + mFarmers[6]) / 2

    highestFreq = 0
    mFarmersSet = set(mFarmers)
    for element in mFarmersSet : 
        freq = mFarmers.count(element)
        if highestFreq < freq : highestFreq = freq
    
    print('The state with highest Percentage of Marginal Farmers is', highestState)
    print('The state with lowest Percentage of Marginal Farmers is', lowestState)
    print('The median Percentage of Marginal Farmers of all States is', median)
    print('The average Percentage of Marginal Farmers of all States is', avg)
    if highestFreq == 1 : print("No modal Percentage of Marginal Farmers . . .")
    else : 
        print("The mode(s) of Percentage of Marginal Farmers is/are : ", end = '')
        for element in mFarmersSet : 
            if mFarmers.count(element) == highestFreq : print(element, end = ', ')
        print('\b\b ')

# iii) Data Assessment of Percentage of Women in overall workforce
def workingWomen(data) : 
    highestState = lowestState = ''
    median = avg = mode = highestPercentage = lowestPercentage = 0
    wWomen = []
    for i in range(len(data)) : 
        list = data[i]
        if list[11] > highestPercentage : 
            highestPercentage = list[11]
            highestState = list[0]
        if i == 0 : 
            lowestPercentage = list[11]
            lowestState = list[0]
        if list[11] < lowestPercentage : 
            lowestPercentage = list[11]
            lowestState  = list[0]
        wWomen.append(list[11])
    avg = sum(wWomen) / (i + 1)
    wWomen.sort()
    median = (wWomen[5] + wWomen[6]) / 2

    highestFreq = 0
    wWomenSet = set(wWomen)
    for element in wWomenSet : 
        freq = wWomen.count(element)
        if highestFreq < freq : highestFreq = freq
    
    print('The state with highest Percentage of women in overall workforce is', highestState)
    print('The state with lowest Percentage of women in overall workforce is', lowestState)
    print('The median Percentage of women in overall workforce of all States is', median)
    print('The average Percentage of women in overall workforce of all States is', avg)
    if highestFreq == 1 : print("No modal Percentage of women in overall workforce . . .")
    else : 
        print("The mode(s) of Percentage of women in overall workforce is/are : ", end = '')
        for element in wWomenSet : 
            if wWomen.count(element) == highestFreq : print(element, end = ', ')
        print('\b\b ')
print('Assessment of Population Density . . .')
populationDensity(data)
print('\nAssessment of Percentage of Marginal Farmers . . .')
marginalFarmers(data)
print('\nAssessment of Percentage of Women in overall workforce . . .')
workingWomen(data)

# b
state = []
dataSlope = []
dataRoadDensity = []
for list in data : 
    state.append(list[0])
    dataSlope.append(list[4])
    dataRoadDensity.append(list[5] * 100)
stateArr = np.arange(len(state))
State = [j + 0.4 for j in stateArr]

plt.bar(stateArr, dataSlope, width = 0.4, color = 'blue', label = 'Percentage Area with slope > 30%')
plt.bar(State, dataRoadDensity, width = 0.4, color = 'red', label = 'Road Density x 100')
for i, h in enumerate(dataSlope) :
    plt.text(i, h + 0.25, str(h), ha = 'center')
for i, h in enumerate(dataRoadDensity) :
    plt.text(i + 0.2, h + 0.50, str(h), ha = 'left')
plt.xlabel("States", fontsize = 20)
plt.ylabel("Data Readings", fontsize = 20)
plt.title("DATA ASSESSMENT", fontsize = 30)
plt.xticks(stateArr + 0.2, state, rotation = 13)
plt.legend()
plt.show()


# c
for i in range(len(dataSlope) - 1) : 
    smallest = dataSlope[i]
    s = i
    for j in range(i + 1, len(dataSlope)) : 
        if dataSlope[j] < smallest :
            smallest = dataSlope[j]
            s = j
    if s != i : 
        temp = dataSlope[i]
        dataSlope[i] = dataSlope[s]
        dataSlope[s] = temp
        temp = state[i]
        state[i] = state[s]
        state[s] = temp
        temp = dataRoadDensity[i]
        dataRoadDensity[i] = dataRoadDensity[s]
        dataRoadDensity[s] = temp

plt.bar(state, dataRoadDensity, width = 0.4, color = 'blue')
for i, h in enumerate(dataRoadDensity) :
    plt.text(i, h + 0.25, str(h), ha = 'center')
plt.xlabel('States(increasing percentage area of slope > 30%)', fontsize = 15)
plt.ylabel('Road Density x 100', fontsize = 15)
plt.title('DATA ASSESSMENT', fontsize = 30)
plt.xticks(rotation = 13)
plt.show()