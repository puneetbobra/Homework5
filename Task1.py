#Create a file scores.txt and create read/write variables
FILENAME = 'scores.txt'
WRITE_MODE = 'w'
READ_MODE = 'r'

#Open file and write content in it
with open(FILENAME, WRITE_MODE) as score_file:
    # pass
    score_file.write('Alice 69\n')
    score_file.write('Bob eighty-seven\n')
    score_file.write('David 89\n')
    score_file.write('Cindy 79\n')
    score_file.write('Eric abc\n')
    
#output should be written to log.txt file
OUTPUT_FILE = 'log.txt'

#variables for counting number of students and sum of the score
counter = 0
total = 0

#open output file in write mode to write the results
with open(OUTPUT_FILE, WRITE_MODE) as out:
    #read name and scores from scores.txt file
    with open(FILENAME, READ_MODE) as score_file:
        #iterate through the contents
        for line in score_file:
            name, score = line.split()
            #count number of records in the file
            counter += line.count(name)
            
            #if there is no content in the file print 'No record found'
            if counter == 0:
                out.write(print('No record found'))
            
            #if score does not contain the correct value remove the record from the count and write the bad record            
            elif score.isdigit() == False:
                counter -= 1
                out.write(f'Bad score value for {str(name)}, ignored.\n')
            
            #for a valid record add the score to total
            else:
                total += int(score)
    
    #write the average and number of valid students
    if counter == 0:
        out.write('No average comupted')
    else:
        out.write(f'The class average is {int(total / counter)} for {counter} students')    





