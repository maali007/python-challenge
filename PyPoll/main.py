# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
import itertools

from collections import Counter

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  # skip the headers
    data = list(csvreader)
    

    #Part 1
    votes = len(data)
    print("Total Votes:" + str(votes))
    
 
#Create empty list
list1 = []

#loop csv column 2 [1] and append values as integers to ls 
for i in data:
    list1.append(i[2])

candidates = []
for x in list1:
    if x not in candidates:
        candidates.append(x)
#print(candidates)

counts = Counter(list1)
#print(counts)

#print(len(candidates[0]))
for x in range(len(candidates)): 
    #print(candidates[x] + ":")


    totalz = sum(counts.values())
    percent = {key: value/totalz for key, value in counts.items()}
#print(percent)

# convert to list
#percent_list = [percent.get(str(i), 0.000) for i in range(len(candidates))]
#print(percent_list)


vc = list(counts.values())
vp = list(percent.values())

#nlist = []
#for i in range(len(candidates)):
 #   print(candidates[0] + str(vc[0]) + str(vp[0]))

#nlist = [candidates, vc, vp]
#print(nlist)


for (a, b, c) in zip(candidates, vc, vp): 
     print (a + ": ","{:.3%}".format(c), "(" + str(b) + ")") 

     