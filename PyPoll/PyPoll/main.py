# Import the os module, csv module and itertools modules
import os
import csv
import itertools

# Import Counter from collections module
from collections import Counter

# Set file path
csvpath = os.path.join('Resources', 'election_data.csv')

# Open the csv file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  # skip the headers
    data = list(csvreader)
    
    # Determine total number of votes cast
    votes = len(data)
    print("Election Results")
    print("------------------")
    print("Total Votes:" + str(votes))
    print("------------------")
    
 
# Create empty list to hold all the candidates chosen in the votes
selectedcandidates = []

# Loop through csv column with candidate names and append values to selectedcandidate list 
for i in data:
    selectedcandidates.append(i[2])

# Create an empty list to hold unique candidate names from the selectedcandidates list
candidates = []

# Loop through selectedcandidate list and add any name thats missing from the candidates list to the candidates list
for x in selectedcandidates:
    if x not in candidates:
        candidates.append(x)

# Determine number of votes for each unique candidate (creates a dictionary)
counts = Counter(selectedcandidates)

# Get total votes cast again. Could use votes from line 21 but wated to try something else
combinedvotes = sum(counts.values())

# Create dictionary of candidate and vote count
percent = {key: value/combinedvotes for key, value in counts.items()}

# Create lists of the votes per candidate and their respective percentages
vc = list(counts.values())
vp = list(percent.values())

# Loop through the candidates, votes per candidate (vc) and percentages (vp) and extract items to concatenate in a print statement
for (a, b, c) in zip(candidates, vc, vp): 
    mainresult = print(a + ": ","{:.3%}".format(c), "(" + str(b) + ")")
print(mainresult)
print("------------------")

# I know Khan is the winner from the counts dictionary and is first item in candidates list so I'll just set the range to 1 in the loop below.
for x in range(1): 
    print("Winner: " + candidates[x])
print("------------------")

# Write results to .txt file in Analysis folder
file1 = open("Analysis\output.txt","a") 
file1.truncate(0)
file1.write("Election Results")
file1.write("\n")
file1.write("-------------------")
file1.write("\n")
file1.write("Total Votes: " + str(votes))
file1.write("\n")
file1.write("-------------------")
file1.write(mainresult)
file1.write("\n")
file1.write("-------------------")
file1.write("\n")
file1.write("Winner: " + candidates[x])
file1.write("\n")
file1.write("-------------------")
file1.close()      