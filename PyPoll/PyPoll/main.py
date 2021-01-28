# Import the os module, csv module and itertools modules
import os
import csv
import itertools
import sys

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

# Create new dictionary (nd) where the key is set as the vote count and the value as the corresponding candidate. This will be useful in printing out the winners name.
nd = {}

# Loop through the candidates, votes per candidate (vc) and percentages (vp) and extract items to concatenate in a print statement
for (a, b, c) in zip(candidates, vc, vp): 
    nd.update({b:a})
    #print(nd)
    print(a + ": ","{:.3%}".format(c), "(" + str(b) + ")")

print("------------------")

# Highest candidate's name (hc) is the value whose key is the highest count in the new dictionary (nd).
hc = max(counts.values())
print("Winner: " + nd[hc])


#Write results to .txt file in Analysis folder
file1 = open("Analysis\output.txt","a") 
file1.truncate(0)
file1.write("Election Results")
file1.write("\n")
file1.write("-------------------")
file1.write("\n")
file1.write("Total Votes: " + str(votes))
file1.write("\n")
file1.write("-------------------")
file1.write("\n")

# Looping through the candidates, vote oercent and vote count lists to get be able to print out each candidates name, vote percent and vote count.
for i in range(len(candidates)):
    file1.write(str(candidates[i]) + ": " + "{:.3%}".format(vp[i]) + "(" + str(vc[i]) + ")")
    file1.write("\n")
file1.write("-------------------")
file1.write("\n")
file1.write("Winner: " + nd[hc])
file1.write("\n")
file1.write("-------------------")
file1.close()      