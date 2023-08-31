from nltk.tokenize import sent_tokenize
import os
import string


path = "/Users/jerseydayao/Desktop/hckrwmn/repositories/Readability-Level-Identifier/clean-txt"
new_path = "/Users/jerseydayao/Desktop/hckrwmn/repositories/Readability-Level-Identifier/token-sentences"

os.chdir(path)


def read_text_file(file_path):
    path, file_name = os.path.split(file_path) # var(file_name) == ... .txt
    title = (os.path.splitext(file_name)[0]).removesuffix('_cleaned')
    text = open(file_path, 'r').read()
    tokenized = sent_tokenize(text)

    new_file_name = new_path + '/' + title + '_sentenceTokens.txt'
    new_file = open(new_file_name, 'w')

    with open(file_path, 'r') as file:

        for line in tokenized:
            line = line.translate(str.maketrans('', '', string.punctuation)) # removes all punctuations from tokenized sentences
            new_file.write(line + '\n')
    
    new_file.close()


# iterate through all text files in folder
for file in os.listdir():

    # checks file format
    if file.endswith(".txt"):
        file_path = f"{path}/{file}" # change slash to \ if working on windows i think? ewan
  
        read_text_file(file_path)