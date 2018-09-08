import os

import csv

csvpath = os.path.join('budget_data.csv')

#print(csvpath)


with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None)
    print(csv_header)
#print("Financial Analysis")
#print("-------------------------------------------------------------------")

    #row_count = sum(1 for row in csvreader)

    #print (f"Total Months: {row_count}")

    
    

    
    #total = 0
    #for row in csvreader:
        #total += int(row[1])
    #print(total)
    

    last_row = next(csvreader, None)
    profit = int(last_row[1])
    #print(last_row)
    month_count = 1
    #calculate change in profit between each month and add it to the profit_change list. append all of the values and then divide them
    #reset variable last row to current row, incrementing the value of month count. divide change by month count
    profit_change = list()
    for row in csvreader:
        profit += int(row[1])
        change = int(row[1]) - int(last_row[1])
        last_row = row
        profit_change.append(change)
        month_count += 1 
        #print(profit_change)
    print(sum(profit_change)/month_count)
    print(month_count)
    print(profit)
        


    
    
    
    

    

        
