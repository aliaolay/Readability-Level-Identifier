# source - https://www.geeksforgeeks.org/how-to-read-multiple-text-files-from-folder-in-python/
# this latest version (21/8/2023) allows multiple files for input for faster processing

 
import os
import stopwordsiso

from stopwordsiso import stopwords

# stopwords('tl') -> collection of stopwords in filo


  
# insert folder path containing all raw text files
path = "/Users/jerseydayao/Desktop/hckrwmn/repositories/Readability-Level-Identifier/raw-txt" 

# insert folder path where new file will be created
new_path = "/Users/jerseydayao/Desktop/hckrwmn/repositories/Readability-Level-Identifier/clean-new"

# change directory
os.chdir(path)


# writes content to new file, stripped, and converts all letters to lowercase
def read_text_file(file_path):
    path, file_name = os.path.split(file_path) # var(file_name) == ... .txt
    title = (os.path.splitext(file_name)[0]).removesuffix('_cleaned')
    new_file_name = new_path + '/' + title + '_cleaned.txt'
    new_file = open(new_file_name, 'w')

    with open(file_path, 'r') as file:
        for line in file:
            no_stop_words = ''
            for word in line.split(' '):
                if word not in stopwords('tl'):
                    no_stop_words += word
                    no_stop_words += ' '
            cleaned_line = no_stop_words.strip().lower()
            new_file.write(' ' + cleaned_line)
            
    new_file.close()


# iterate through all text files in folder
for file in os.listdir():

    # checks file format
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"    # change slash to \ if working on windows i think?
  
        read_text_file(file_path)