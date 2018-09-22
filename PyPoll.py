import os

import csv

from collections import Counter

csvpath = os.path.join('election_data.csv')

#print(csvpath)


with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None)
    #print(csv_header)


    last_row = next(csvreader, None)
    #profit = int(last_row[1])
    #print(last_row)
    vote_count = 1
    #calculate change in profit between each month and add it to the profit_change list. append all of the values and then divide them
    #reset variable last row to current row, incrementing the value of month count. divide change by month count
    #profit_change = list()
    #list1 = [(row[2])]
    #counts = Counter(list1)
    for row in csvreader:
        #profit += int(row[1])
        #change = int(row[1]) - int(last_row[1])
        last_row = row
        #profit_change.append(change)
        vote_count += 1 
        
        vote_numbers = str(row[0])
        



print(f"Total votes: {vote_count}")
#print(counts)