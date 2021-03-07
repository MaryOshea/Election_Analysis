#1. Import csv file and add dependencies
import csv
import os

#2. Assign a variable for the file to load and its indirect file path
file_to_load = os.path.join("Resources", "election_results.csv")

#3. Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#4. Open the election file results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #5. Read and print the header row
    headers = next(file_reader)
    print(headers)

















#The data we need to retrieve from the file
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular votes