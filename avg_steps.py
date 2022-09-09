def main():
    import csv 
    infile = open('steps.csv','r')
    outfile = open('avg_steps.csv','w')

    csvfile = csv.reader(infile, delimiter= ',')

    next (csvfile)

    outfile.write('Month, Average Steps\n')

    Count = 1
    Total_Month_Steps = 0 
    days = 0 
   

    month_names = ['Random','January','February','March','April','May','June','July','August','September','October','November','December']
    


    for record in csvfile:  
        
        if record[0] == str(Count): 
            Total_Month_Steps += int(record[1]) 
            days += 1

        else: 
            
            average_steps = format((Total_Month_Steps/days), '.2f')
            
            outfile.write(month_names[int(Count)] + ': ' + str(average_steps) + '\n')

            Count = record[0]
            Total_Month_Steps = int(record[1])
            days = 1 



    average_steps = format((Total_Month_Steps/days), '.2f')
    outfile.write(month_names[int(Count)] + ': ' + str(average_steps) + '\n')

    Count = record[0]
    Total_Month_Steps = int(record[1])
    days = 1 

            

    
    
    outfile.close()

main()
    