#Read the file book.txt and write the output in summary.txt
FILENAME = 'book.txt'
OUTPUT_FILE = 'summary.txt'
READ_MODE = 'r'
WRITE_MODE = 'w'

#open output file in write mode to write the results
with open(OUTPUT_FILE, WRITE_MODE) as out:
    #Read the book.txt file
    with open(FILENAME, READ_MODE) as book_file:
        lines = book_file.read()    
        
        #make all alphabets lower case to make it case insensitive
        lines = lines.lower()
        
        #sort the characters ascending
        lines = sorted(lines)
        
        t = []
        all_alphabets = ' '

        # populate all lower case characters of alphabets to check if all letters exist in the book or not
        for j in range(97, 123):        
            count = 0
            # read the lines 
            for i in lines:    
                
                #remove spaces and non alphabet characters like .!,
                if i.isalpha == False: pass
                elif i == '\n': pass
                elif i == ' ': pass
                
                #if it is an alphabet then increase the count
                if i == chr(j): count += 1
                
                #append the characters in list t which would be used for checking if all alphabets exist or not
                t.append(i)                

        # print letters and their count which exist
            if count == 0: 
                all_alphabets = False
            else: out.write(f'{chr(j).upper()} {count}\n')
        
        #if all_alphabets is flase then all letters do not exist in the book
        if all_alphabets == False: 
            out.write("\nIt doesn't have all letters")
        else: out.write('\nIt has all letters')
        

    