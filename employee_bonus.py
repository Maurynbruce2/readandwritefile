def main():
    import csv
    infile = open('EmployeePay.csv','r')
    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)

    for record in csvfile: 
        i_d = record[0]
        full_name = record[1] + ' ' + record[2]
        salary = int(record[3])
        bonus = float(record[4])
        added_bonus = (salary*bonus)
        Total_salary = (salary+added_bonus)

        #print(i_d + ',' + full_name + ', $' + salary + ', $' + bonus + ', $' + Total_salary + '\n')

        print('ID:', i_d)
        print('Full Name:', full_name)
        print('Salary:', (format(salary,",.2f")))
        print('Bonus:', (format(bonus,",.2f")))
        print('Total Salary:', (format(Total_salary,",.2f")))

        input('Press enter for next employee')
main() 

