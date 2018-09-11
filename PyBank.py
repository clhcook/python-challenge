import os

import csv



csvpath = os.path.join('budget_data.csv')

#print(csvpath)


with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None)
    #does making csv header and lastrow throw off the count???
    

    last_row = next(csvreader, None)
    profit = int(last_row[1])
    
    month_count = 1
    #calculate change in profit between each month and add it to the profit_change list. append all of the values and then divide them
    #reset variable last row to current row, incrementing the value of month count. divide change by month count
    profit_change = list()
    month_list = list()
    keys = month_list
    values = profit_change
    dictionary = dict(zip(keys, values))
    for row in csvreader:
        profit += int(row[1])
        change = int(row[1]) - int(last_row[1])
        last_row = row
        profit_change.append(change)
        month_count += 1 
        
        mnames = str(row[0])
        month_list.append(mnames)
        
        keys = month_list
        values = profit_change
        dictionary = dict(zip(keys, values))
    print("Financial Analysis")
    print("-------------------------------------------------------------------")
    print(f"The average change in profits is ${round(sum(profit_change)/month_count, 2)}")
    print(f"Total months {month_count}")
    print(f"Total profit is ${profit}")
    print(f"Greatest increase in profits is  {max(dictionary.items(), key = lambda x: x[1])}")
    print(f"Greatest decrease in profits is {min(dictionary.items(), key = lambda x: x[1])}")
    #print(month_list)
    #print(dictionary)
    