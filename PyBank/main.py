import os
import csv

# Path to the csv fille

csvpath = os.path.join("python-challenge/PyBank/Resources/budget_data.csv") 


#function to count all rows in column 1 of csv file 

def count_rows_in_column(csv_file, column_number):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row
        count = sum(1 for row in csv_reader if row)  # Count the remaining rows in column 1

    return count



csv_file =  csvpath
column_number = 0  
row_count = count_rows_in_column(csv_file, column_number)

# Print the Financial analysis results to the terminal
print(f"Total Months: {row_count}")


# fucntion to sum all values in column 2 to find total amount


def calculate_net_profit_losses(csv_file):
    net_profit_losses = 0

    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            profit_loss = int(row['Profit/Losses'])
            net_profit_losses += profit_loss

    return net_profit_losses

# Example usage:
csv_file_path = csvpath
net_profit_losses = calculate_net_profit_losses(csv_file_path)

# Print the Financial analysis results to the terminal
print(f"Total: ${net_profit_losses}")


# function that calcukates average change 

def calculate_profit_changes_and_average(csv_file):
    # Stated variables
    previous_profit_loss = 0
    profit_changes = []
    
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        
        # Read the first row to get the initial value
        first_row = next(csv_reader)
        previous_profit_loss = int(first_row['Profit/Losses'])
        
        # Iterate through the all other rows
        for row in csv_reader:
            current_profit_loss = int(row['Profit/Losses'])
            
            # Calculate the change and store it in the list
            change = current_profit_loss - previous_profit_loss
            profit_changes.append(change)
            
            # Update the previous profit/loss for the next iteration
            previous_profit_loss = current_profit_loss

    # Calculate the average of profit changes
    average_change = sum(profit_changes) / len(profit_changes) if profit_changes else 0
    
    return profit_changes, average_change


csv_file_path = csvpath
changes, average_change = calculate_profit_changes_and_average(csv_file_path)

# Print the Financial analysis results to the terminal
print(f"Average Change: ${average_change:.2f}")




#function that calculates greatest increase on profits


def find_greatest_increase(csv_file):
    # Create a dictionary to store the greatest increase and its corresponding date
    greatest_increase = {'date': None, 'amount': None}

    # Open the CSV file 
    with open(csv_file, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        # Create a variable to store the profit/loss of the previous row
        previous_profit_loss = None

        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Extract the date and profit/loss from the current row
            current_date = row['Date']
            current_profit_loss = int(row['Profit/Losses'])

            # Calculate the profit change compared to the previous row
            if previous_profit_loss is not None:
                profit_change = current_profit_loss - previous_profit_loss

                # Check if the current profit change is the greatest so far
                if greatest_increase['amount'] is None or profit_change > greatest_increase['amount']:
                    # If so, update the greatest increase and its corresponding date
                    greatest_increase['date'] = current_date
                    greatest_increase['amount'] = profit_change

            # Update the previous profit/loss for the next loop
            previous_profit_loss = current_profit_loss

    # Return the dictionary containing the greatest increase and its date
    return greatest_increase


csv_file_path = csvpath  

greatest_increase = find_greatest_increase(csv_file_path)

# Print the Financial analysis results to the terminal
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")

#function that calculates greatest decrease on profits

def find_greatest_decrease(csv_file):
    greatest_decrease = {'date': None, 'amount': None}

    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        previous_profit_loss = None

        for row in csv_reader:
            current_date = row['Date']
            current_profit_loss = int(row['Profit/Losses'])

            if previous_profit_loss is not None:
                profit_change = current_profit_loss - previous_profit_loss

                if greatest_decrease['amount'] is None or profit_change < greatest_decrease['amount']:
                    greatest_decrease['date'] = current_date
                    greatest_decrease['amount'] = profit_change

            previous_profit_loss = current_profit_loss

    return greatest_decrease


csv_file_path = csvpath 

greatest_decrease = find_greatest_decrease(csv_file_path)

# Print the Financial analysis results to the terminal
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")


#output all results from each fucntion to txt file 

output_file_path = os.path.join("python-challenge/PyBank/Analysis/analysis.txt")

with open(output_file_path, 'w') as output_file:
    print("Financial Analysis", file=output_file)
    print("                            ",file=output_file )
    print("----------------------------", file=output_file)
    print("                            ",file=output_file )
    print(f"Total Months: {row_count}", file=output_file)
    print(f"Total: ${net_profit_losses}", file=output_file)
    print(f"Average Change: ${average_change}", file=output_file)
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})", file=output_file)
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})", file=output_file)