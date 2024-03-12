import os
import csv

# connect to the csv fille

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
print(f"Total Months: {row_count}")


# fucntion to sum all values in column 2 


def sum_column_values(csv_file, column_index):
    total_sum = 0

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader, None)  # Skip the header

        for row in csv_reader:
            try:
                value = float(row[column_index])
                total_sum += value
            except (ValueError, IndexError):
                print(f"Skipping invalid value in row {csv_reader.line_num}")

    return total_sum

# Example usage:
csv_file_path = csvpath  
column_index_to_sum = 1  

result = sum_column_values(csv_file_path, column_index_to_sum)
print(f"Total: ${result}")


# function that calcukates average change 

def calculate_profit_changes_and_average(csv_file):
    # Initialize variables
    previous_profit_loss = 0
    profit_changes = []
    
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        
        # Read the first row to get the initial value
        first_row = next(csv_reader)
        previous_profit_loss = int(first_row['Profit/Losses'])
        
        # Iterate through the remaining rows
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

print(f"Average Change: ${average_change}")




#function that calculates greatest increase on profits


def find_greatest_increase(csv_file):
    greatest_increase = {'date': None, 'amount': None}

    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        previous_profit_loss = None

        for row in csv_reader:
            current_date = row['Date']
            current_profit_loss = int(row['Profit/Losses'])

            if previous_profit_loss is not None:
                profit_change = current_profit_loss - previous_profit_loss

                if greatest_increase['amount'] is None or profit_change > greatest_increase['amount']:
                    greatest_increase['date'] = current_date
                    greatest_increase['amount'] = profit_change

            previous_profit_loss = current_profit_loss

    return greatest_increase


csv_file_path = csvpath  

greatest_increase = find_greatest_increase(csv_file_path)

print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")

import csv

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

# Example usage:
csv_file_path = csvpath  # Replace with your CSV file path

greatest_decrease = find_greatest_decrease(csv_file_path)

print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")


#output all outputs from each fucntion to txt file 

output_file_path = os.path.join("python-challenge/PyBank/Analysis/analysis.txt")

with open(output_file_path, 'w') as output_file:
    print("Financial Analysis", file=output_file)
    print("----------------------------", file=output_file)
    print(f"Total Months: {row_count}", file=output_file)
    print(f"Total: ${result}", file=output_file)
    print(f"Average Change: ${average_change}", file=output_file)
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})", file=output_file)
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})", file=output_file)