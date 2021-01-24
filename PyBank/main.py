# Import the os module, csv module and itertools modules
import os
import csv
import itertools

# Set file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open the csv file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  # skip the headers
    data = list(csvreader)
    
#The total number of months included in the dataset
months = len(data)
    
# Determine the net total amount of "Profit/Losses" over the entire period
total = sum(int(row[1]) for row in data)

# Create empty list to hold Profit/Loss values
pll = []

#loop csv column 2 and append values as integers to pll 
for i in data:
    pll.append(int(i[1]))

#Create new list for differences
plld = []

#Loop through pll items 2 to last item subtracting items in row i from items in row i+1
#append to this new list 
for i in range(len(pll) - 1):
    plld.append(pll[i + 1] - pll[i])

#Defining average function
def Average(plld):
    return sum(plld) / len(plld)

#Getting minimum, maximum, and average of differences into variables
mini = min(plld)
maxi = max(plld)
aver = round(Average(plld), 2)

print("Financial Analysis")
print("------------------------------")
print("Total Months:" + str(months))
print("Total: " + str(total))
print("Average: " + str(aver))
print("Greatest Increase in Profits: : " + str(maxi))
print("Greatest Decrease in Profits: : " + str(mini))

# Open the file using "write" mode. Specify the variable to hold the contents
file1 = open("Analysis\output.txt","a") 
file1.truncate(0)
file1.write("Financial Analysis")
file1.write("\n")
file1.write("-------------------")
file1.write("\n")
file1.write("Total Months: " + str(months))
file1.write("\n")
file1.write("Total: " + str(total))
file1.write("\n")
file1.write("Average: " + str(aver))
file1.write("\n")
file1.write("Greatest Increase in Profits: " + str(maxi))
file1.write("\n")
file1.write("Greatest Decrease in Profits: " + str(mini))
file1.close() 