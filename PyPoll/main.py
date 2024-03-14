import os
import csv

# Path to the csv file
csvpath = os.path.join("python-challenge/PyPoll/Resources/election_data.csv")

def election_results(csv_file, output_file):
    # Initialize variables to store election data
    total_votes = 0
    candidates = {}

    # Read the CSV file
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)

        # Loop through each row in the CSV file
        for row in csv_reader:
            total_votes += 1  # Count total votes

            # Extract the candidate from the current row
            candidate = row['Candidate']

            # Update candidate's vote count
            candidates[candidate] = candidates.get(candidate, 0) + 1

    # Percentage of votes each candidate won
    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

    # Locate the winner based on total vote
    winner = max(candidates, key=candidates.get)

    # Print the election analysis results to the terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")

    # Print results for each candidate
    for candidate, votes in candidates.items():
        percentage = percentages[candidate]
        print(f"{candidate}: {percentage:.2f}% ({votes})")

    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

    # Add the election analysis results to a txt file
    with open(output_file, 'w') as output:
        output.write("**Election Results**\n")
        output.write("----------------------------\n")
        output.write(f"Total Votes: {total_votes}\n")
        output.write("----------------------------\n")

        # Add results for each candidate
        for candidate, votes in candidates.items():
            percentage = percentages[candidate]
            output.write(f"{candidate}: {percentage:.2f}% ({votes})\n")

        output.write("----------------------------\n")
        output.write(f"Winner: {winner}\n")
        output.write("----------------------------\n")

# Path to the csv file
csvfile = csvpath

# Output results to a txt file in a designated folder in repo
output_file_path = os.path.join("python-challenge/PyPoll/Analysis/analysis.txt")

# Analyze election results and output to the txt file
election_results(csvfile, output_file_path)
