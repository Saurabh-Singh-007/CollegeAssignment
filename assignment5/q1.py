
import pandas as pd

# Specify the full file path
file_path = "/Users/saurabhsingh/Desktop/Data.csv"

try:
    # Attempt to open the file
    df = pd.read_csv(file_path)
    # Perform operations on the DataFrame 'df' here
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

# Use pandas to read the CSV
csvData = pd.read_csv('Data.csv', sep=',')

# Convert the pandas dataframe into a NumPy array
csvDataNum = csvData[['State', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']].to_numpy()

# Convert the NumPy array into a list of lists
data = csvDataNum.tolist()


#Write functions working on data which provide information on i) population density, ii) percentage of marginal farmers and iii) percentage of women in the overall workforce, by giving:
 
# • Highest = the state with the highest value 
# • Lowest = the state with the lowest value 
# • Median = the median 
# • Average = the average value 
# • Mode = the value with highest frequency

# Don’t use predefined pandas methods for these functions. Print the information in a way you find best represented.

def popDensity(data):
    # Calculate the population density for each state
    popDensity = []
    for i in range(len(data)):
        popDensity.append(data[i][1] / data[i][2])

    # Find the highest, lowest, median, average and mode population density
    highest = max(popDensity)
    lowest = min(popDensity)
    median = sorted(popDensity)[len(popDensity) // 2]
    average = sum(popDensity) / len(popDensity)
    mode = max(set(popDensity), key=popDensity.count)

    # Print the information
    print('Population Density')
    print('Highest: ' + str(highest))
    print('Lowest: ' + str(lowest))
    print('Median: ' + str(median))
    print('Average: ' + str(average))
    print('Mode: ' + str(mode))
    print('')
    return popDensity


def PercentageMarginalFarmers(data):
    marginalFarmers = []
    for i in range(len(data)):
        marginalFarmers.append(data[i][8])
    highest = max(marginalFarmers)
    lowest = min(marginalFarmers)
    median = sorted(marginalFarmers)[len(marginalFarmers) // 2]
    average = sum(marginalFarmers) / len(marginalFarmers)
    mode = max(set(marginalFarmers), key=marginalFarmers.count)

    print('Percentage of Marginal Farmers')
    print('Highest: ' + str(highest))
    print('Lowest: ' + str(lowest))
    print('Median: ' + str(median))
    print('Average: ' + str(average))
    print('Mode: ' + str(mode))
    print('')
    return marginalFarmers


def PercentageWomenWorkforce(data):
    WomenWorkforce = []
    for i in range(len(data)):
        WomenWorkforce.append(data[i][12])
    highest = max(WomenWorkforce)
    lowest = min(WomenWorkforce)
    median = sorted(WomenWorkforce)[len(WomenWorkforce) // 2]
    average = sum(WomenWorkforce) / len(WomenWorkforce)
    mode = max(set(WomenWorkforce), key=WomenWorkforce.count)

    print('Percentage of Women Workers')
    print('Highest: ' + str(highest))
    print('Lowest: ' + str(lowest))
    print('Median: ' + str(median))
    print('Average: ' + str(average))
    print('Mode: ' + str(mode))
    print('')
    return WomenWorkforce


#For the given order of states in the first column of the csv, create a single bar chart which takes as variables the:
# the percentage area with slope > 30%
# the road density
# For each state the 2 values should be displayed next to each other.

def barChart(data):
    # Calculate the percentage area with slope > 30% for each state
    slope = []
    for i in range(len(data)):
        slope.append(data[i][3])

    # Calculate the road density for each state
    roadDensity = []
    for i in range(len(data)):
        roadDensity.append(data[i][4])

    # Plot the bar chart
    import matplotlib.pyplot as plt
    import numpy as np

    # Set the width of the bars
    barWidth = 0.25

    # Set the position of the bars on the x-axis
    r1 = np.arange(len(slope))
    r2 = [x + barWidth for x in r1]

    # Make the plot
    plt.bar(r1, slope, color='#7f6d5f', width=barWidth, edgecolor='white', label='Slope > 30%')
    plt.bar(r2, roadDensity, color='#557f2d', width=barWidth, edgecolor='white', label='Road Density')

    # Add xticks on the middle of the group bars
    plt.xlabel('State', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(slope))], ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
                                                           'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
                                                           'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala',
                                                           'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya',
                                                           'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan',
                                                           'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
                                                           'Uttar Pradesh', 'Uttarakhand', 'West Bengal'],
               rotation=90)

    # Create legend & Show graphic
    plt.legend()
    plt.show()









