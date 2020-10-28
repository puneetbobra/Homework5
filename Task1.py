import os

#Create a file scores.txt and create read/write variables
FILENAME = 'scores.txt'
WRITE_MODE = 'w'
READ_MODE = 'r'

#Open file and write content in it
with open(FILENAME, WRITE_MODE) as score_file:
    score_file.write('Alice 69\n')
    score_file.write('Bob 89\n')
    score_file.write('Cindy 79\n')

#open scores.txt and read the content to calculate number of students and the averages of all scores in the file
#output should be written to log.txt file
OUTPUT_FILE = 'log.txt'

counter = 0
sum = 0

with open(FILENAME, READ_MODE) as score_file:
    for line in score_file:
        name, score = line.split()        
        counter += line.count(name)
        sum += int(score)
    
with open(OUTPUT_FILE, WRITE_MODE) as out:
    out.write(f'Number of students: {counter}\n')
    out.write(f'Sum of scores: {sum}')
#     out.write(sum / counter)



