# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
import itertools
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  # skip the headers
    data = list(csvreader)
    
    #Part 1
    months = len(data)
    
    #Part2
    total = sum(int(row[1]) for row in data)

#Create empty list
ls = []

#loop csv column 2 [1] and append values as integers to ls 
for i in data:
    ls.append(int(i[1]))

#Create new list for differences
new_ls = []

#Loop through ls items 2 to last item subtracting items in row i from items in row i+1
#append to this new list 
for i in range(len(ls) - 1):
    new_ls.append(ls[i + 1] - ls[i])

#Defining average function
def Average(new_ls):
    return sum(new_ls) / len(new_ls)

#Getting minimum, maximum, and average of differences into variables
mini = min(new_ls)
maxi = max(new_ls)
aver = round(Average(new_ls), 2)

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