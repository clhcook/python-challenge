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
    Correy_count = 0
    Li_count = 0
    OTooley_count = 0

    



    for row in csvreader:
        vote_count += 1 
        
        
        last_row = row
    
    
        if str(row[2]) == "Khan":
            Khan_count += 1 
            

        elif str(row[2]) == "Correy":
            Correy_count += 1
            
            
        
        elif str(row[2]) == "Li":
            Li_count += 1
            
        
        elif str(row[2]) == "O'Tooley":
            OTooley_count +=1
            
            

    print("Election Results")
    print("--------------------------------------------------------")
    
    print(f"Total Votes: {vote_count}")
    print("--------------------------------------------------------")
    
    print(f"Khan: {round(Khan_count/vote_count * 100, 3)}%  ({Khan_count})")
    print(f"Correy: {round(Correy_count/vote_count * 100, 3)}% ({Correy_count})")
    print(f"Li: {round(Li_count/vote_count * 100, 3)}%   ({Li_count})")  
    print(f"O'Tooley: {round(OTooley_count/vote_count * 100, 3)}% ({OTooley_count})")
    
    print("--------------------------------------------------------")

    print("Winner: Khan")


      
          

  

    

