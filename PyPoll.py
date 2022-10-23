#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote


import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list if it doesn't exist
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #initialize the dictionary as new names are found
            candidate_votes[candidate_name] = 0
    
        candidate_votes[candidate_name] += 1

winning_candidate = ""
winning_count = 0
winning_percent = 0.0
candidate_results = ""

for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]
    
    vote_percentage = float(votes) / float(total_votes) * 100
   
    candidate_results += (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percent):
        winning_count = votes
        winning_percent = vote_percentage
        winning_candidate = candidate_name

print(candidate_results)
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percent:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n")
    
    print(election_results, end = "")

    txt_file.write(election_results)
    txt_file.write(candidate_results)
    txt_file.write(winning_candidate_summary)
