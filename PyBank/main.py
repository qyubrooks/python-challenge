#import module
import os
import csv

#set variables
total_row_count = 0
dates = []
total = 0
profit = []
profitChange = []

greatestIncrease = 0
greatestDecrease = 0

#set path for the file and read using CSV module
csvpath = os.path.join('.','Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    #read the header row first
    csv_header = next(csvreader)
    
    #read each row of csvreader after the header
    for row in csvreader:
        #caculate how many total of months 
        total_row_count += 1
        dates.append(row[0])
        
        #caculate the net total amount of "Profit/Losses" 
        total += int(row[1])
        profit.append(int(row[1]))
    
    #loop through each month of value of "Profit/Losses" and caculate the change between each two monthes
    for i in range(len(profit)-1):
        change = profit[i+1] - profit[i]
        profitChange.append(change)
        
        #cacualte average change in "Profit/Losses"
        averageChange = round(sum(profitChange)/len(profitChange),2)
        
        # find the greatest increase/decrease in profits (date and amount)
        if (change > greatestIncrease):
            greatestIncreaseMonth = dates[i+1]
            greatestIncrease = change
        if (change < greatestDecrease):
            greatestDecreaseMonth = dates[i+1]
            greatestDecrease = change
                 
    print(" Financial Analysis")
    print("-" * 25)
    print(f"Total Months: {total_row_count}") 
    print("Total: $" + str(total))
    print(f"Average Change: ${averageChange}")
    print(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})")
    print(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecrease})")
    
    
#open the output file to  export a text file with the results
output_file = os.path.join(".", "Financial_Analysis.txt")
with open(output_file, 'w', newline='') as text:
    text.write(" Financial Analysis\n")
    text.write("-----------------------\n")
    text.write(f"Total Months: {total_row_count}\n") 
    text.write(f"Total: $ {total}\n")
    text.write(f"Average Change: ${averageChange}\n")
    text.write(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})\n")
    text.write(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecrease})\n")