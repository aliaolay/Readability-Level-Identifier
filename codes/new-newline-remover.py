# source - https://www.geeksforgeeks.org/how-to-read-multiple-text-files-from-folder-in-python/
# this latest version (21/8/2023) allows multiple files for input for faster processing

 
import os
  
# insert folder path containing all raw text files
path = "" 
  
# change directory
os.chdir(path)
  

# writes content to new file, stripped
def read_text_file(file_path):
    path, file_name = os.path.split(file_path) # var(file_name) == ... .txt
    new_file_name = path + '/' + file_name.rstrip(".txt") + '_nonewline.txt'
    new_file = open(new_file_name, 'w')

    with open(file_path, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            new_file.write(' ' + stripped_line)
            
    new_file.close()


# iterate through all text files in folder
for file in os.listdir():

    # checks file format
    if file.endswith(".txt"):
        file_path = f"{path}/{file}" # change slash to \ if working on windows i think?
  
        read_text_file(file_path)