import statistics
## numpy is used for creating fake data
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

## agg backend is used to create plot as a .png file
mpl.use('agg')

def findUpperOutliers(upperBound, list):
    upOutliers = []
    for element in list:
        if element > upperBound:
            upOutliers.append(element)
    return upOutliers


def findLowerOutliers(lowerBound, list):
    lowOutliers = []
    for element in list:
        if element < lowerBound:
            lowOutliers.append(element)
    return lowOutliers


userEntry = []

userEntry = input("Enter the list you are interested: ").split(",")

intList = []

for element in userEntry:
    intList.append(int(element))

# sort list for use in median function

intList.sort(reverse=True)

half = int((len(intList)+1)/2)


q1 = statistics.median(intList[half:])
q2 = statistics.median(intList)
q3 = statistics.median(intList[:half])

print("q1: " + str(q1))
print("q2: " + str(q2))
print("q3: " + str(q3))

IQR = q3 - q1

print("IQR: " + str(IQR))

upperBound = q3 + (1.5*IQR)
lowerBound = q1 - (1.5*IQR)

print("Upper Outlier Bound: " + str(upperBound))
print("Lower Outlier Bound: " + str(lowerBound))

print("Upper Outliers: " + str(findUpperOutliers(upperBound, intList)))
print("Lower Outliers: " + str(findLowerOutliers(lowerBound, intList)))

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(intList)

# Save the figure
fig.savefig('fig1.png', bbox_inches='tight')