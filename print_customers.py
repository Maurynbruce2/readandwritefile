
import csv
infile = open('customers.csv','r')

csvfile = csv.reader(infile, delimiter=',')

for record in csvfile: 
    print(record[0])
    print(record[1])

    next(csvfile)

    for record in csvfile: 
        print('ID:' ,record[0])
        print("First Name:",record[1])
        print("Last Name:",record[2])
        print("City:",record[3])
        print("County:",record[4])
        print("Phone:",record[5])
        
        input("Press enter for next customer:")




