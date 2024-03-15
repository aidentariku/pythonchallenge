import csv
import os

# Define the path to the election data CSV file
election_data_file = os.path.join("C:\\Users\\AidenTariku\\Downloads\\Starter_Code (15)\\Starter_Code\\PyPoll\\Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = []
votes_by_candidate = {}
election_winner = ""
winner_votes = 0

# Read and process the election data CSV file
with open(election_data_file) as csv_file:
    csv_reader = csv.reader(csv_file)
    header_row = next(csv_reader)

    for row in csv_reader:
        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates.append(candidate_name)
            votes_by_candidate[candidate_name] = 0

        votes_by_candidate[candidate_name] += 1

# Analyze the votes for each candidate
for candidate, votes in votes_by_candidate.items():
    vote_percentage = (votes / total_votes) * 100

    if votes > winner_votes:
        winner_votes = votes
        election_winner = candidate

    # Print results to the terminal
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")

# Print election results
election_results_summary = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

print(election_results_summary)
print(f"Winner: {election_winner}")

# Define the path to the output text files
output_file_path = "C:\\Users\\AidenTariku\\Downloads\\Starter_Code (15)\\Starter_Code\\PyPoll\\Analysis"

# Write election results summary to a text file
with open(os.path.join(output_file_path, "election_results.txt"), "w") as txt_file:
    txt_file.write(election_results_summary)

# Write winning candidate summary to a text file
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {election_winner}\n"
    f"-------------------------\n"
)

with open(os.path.join(output_file_path, "winning_candidate_summary.txt"), "w") as txt_file:
    txt_file.write(winning_candidate_summary)

