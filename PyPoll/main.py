import os
import csv

# connect to the csv fille

csvpath = os.path.join("python-challenge/PyPoll/Resources/election_data.csv") 


import csv

def analyze_election(csv_file, output_file):
    # Initialize variables to store election data
    total_votes = 0
    candidates = {}

    # Read the CSV file
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csv_reader:
            total_votes += 1  # Count total votes

            # Extract the candidate from the current row
            candidate = row['Candidate']

            # Update candidate's vote count
            candidates[candidate] = candidates.get(candidate, 0) + 1

    # Calculate the percentage of votes each candidate won
    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

    # Find the winner based on popular vote
    winner = max(candidates, key=candidates.get)

    # Write the election analysis results to a text file
    with open(output_file, 'w') as output:
        output.write("Election Results\n")
        output.write("-------------------------\n")
        output.write(f"Total Votes: {total_votes}\n")
        output.write("-------------------------\n")

        # Write results for each candidate
        for candidate, votes in candidates.items():
            percentage = percentages[candidate]
            output.write(f"{candidate}: {percentage:.2f}% ({votes})\n")

        output.write("-------------------------\n")
        output.write(f"Winner: {winner}\n")
        output.write("-------------------------\n")


csv_file_path = csvpath 
output_file_path = os.path.join("python-challenge/PyPoll/Analysis/analysis.txt") 

analyze_election(csv_file_path, output_file_path)
