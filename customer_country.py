def main(): 


    import csv
    infile = open('customers.csv','r')

    csvfile = csv.reader(infile, delimiter=',')

    Header = 'Full Name' , 'Country'
    Index = [0,4]
    Data = Index

    customer_country = open('path/to/csv_file','w')
    writer = csv.writer(customer_country)

    writer.writerow(Header)
    csvfile.close()

main()






