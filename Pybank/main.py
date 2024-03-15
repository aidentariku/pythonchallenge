# Import module to read csv files
import csv

# Import module to create path for operating systems
import os

# Load csv data from Resources folder
csv_file_path = os.path.join('Resources', "budget_data.csv")

# Create variables
total_months = 0
net_total = 0
monthly_changes = []
months = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999]

# Read and process csv file from Resources folder
with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Read the header row
    header_row = next(csv_reader)

    # Process each row of data
    for row in csv_reader:
        # Calculate total number of months
        total_months += 1

        # Calculate net total amount of Profit/Losses
        net_total += int(row[1])

        # Calculate monthly changes
        if total_months > 1:
            monthly_change = int(row[1]) - prev_profit_loss
            monthly_changes.append(monthly_change)
            months.append(row[0])

            # Determine greatest increase in profits
            if monthly_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = monthly_change

            # Determine greatest decrease in profits
            if monthly_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = monthly_change

        # Store current profit/loss for next iteration
        prev_profit_loss = int(row[1])

# Calculate average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Print summary of results to the terminal
summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profit/Loss: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(summary)

# Set location in local repository to print results of data summary
output_file_path = os.path.join('Analysis', "budget_data_output.txt")

# Print out data summary results to .txt file
with open(output_file_path, "w") as txt_file:
    txt_file.write(summary)

