import os
import csv

profitChange = []
total_row_count = 0
total = 0
previousProfit = 0
greatestIncrease = 0
greatestDecrease = 0

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        total_row_count += 1
        total += int(row[1])
        
        monthlyProfitChange = int(row[1]) - previousProfit
        previousProfit = int(row[1])
        profitChange.append(monthlyProfitChange)
        averageChange = round(sum(profitChange)/total_row_count,2)
        
        if (monthlyProfitChange > greatestIncrease):
            greatestIncreaseMonth = row[0]
            greatestIncrease = monthlyProfitChange
        if (monthlyProfitChange < greatestDecrease):
            greatestDecreaseMonth = row[0]
            greatestDecrease = monthlyProfitChange
            
    print(" Financial Analysis")
    print("-" * 25)
    print(f"Total Months: {total_row_count}") 
    print("Total: $" + str(total))
    print(f"Average Change: ${averageChange}")
    print(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})")
    print(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecrease})")
    
    

output_file = os.path.join(".", "Financial_Analysis.txt")
with open(output_file, 'w', newline='') as text:
    text.write(" Financial Analysis\n")
    text.write("-----------------------\n")
    text.write(f"Total Months: {total_row_count}\n") 
    text.write(f"Total: $ {total}\n")
    text.write(f"Average Change: ${averageChange}\n")
    text.write(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})\n")
    text.write(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecrease})\n")