import os

import csv

#from collections import Counter

csvpath = os.path.join('election_data.csv')



with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None)

    last_row = next(csvreader, None)

    vote_count = 1

    Khan_count = 1
    Correy_count = 1
    Li_count = 1
    OTooley_count = 1

    #klist = []
    #clist = []
    #llist = []
    #olist = []



    for row in csvreader:
        vote_count += 1 
        
        vote_numbers = str(row[0])
        last_row = row
    
    
        if str(row[2]) == "Khan":
            Khan_count += 1 
            kname = str(row[2])
            #klist.append(kname)

        elif str(row[2]) == "Correy":
            Correy_count += 1
            cname = str(row[2])
            #clist.append(cname)
        
        elif str(row[2]) == "Li":
            Li_count += 1
            lname = str(row[2])
            #llist.append(lname)
        
        elif str(row[2]) == "O'Tooley":
            OTooley_count +=1
            oname = str(row[2])
            #olist.append(oname)

    print(f"{vote_count}")
    print(Khan_count/vote_count*100)
    #print(round(Khan_count/vote_count*100),4)
    print(f"{round((Khan_count/vote_count * 100),3)}%  {Khan_count}")
    print(f"{Correy_count}")
    print(f"{Li_count}")  
    print(f"{OTooley_count}")

      
          

  

    

