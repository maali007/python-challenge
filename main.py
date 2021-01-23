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

print("Financial Analysis")
print("------------------------------")
print("Total Months:" + str(months))
print("Total: " + str(total))

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
