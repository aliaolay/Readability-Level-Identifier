#folder directory of raw .txt files
dirpath = "C:/Users/Alia/Documents/school/THESIS/CODES/txt/"

#replace value with the book title; 
# DO NOT INLCUDE'.txt'
file_name = "Ang Aklatang Pusa"

#creates new file with cleaned text
new_file_name = dirpath + file_name + '_nonewline.txt'
new_file = open(new_file_name, 'w')

with open(dirpath + file_name + '.txt', 'r') as file:
    for line in file:
        stripped_line = line.strip()
        new_file.write(' ' + stripped_line)
        
new_file.close()
        
