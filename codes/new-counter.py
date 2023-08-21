import os

import nltk
from nltk.tokenize import word_tokenize
# nltk.download('punkt')
  
# target folder path
path = "..."
  
os.chdir(path)
  
all_sentence_count = 0
all_word_count = 0

def read_text_file(file_path):
    path, file_name = os.path.split(file_path)

    # sentence counter
    folder = nltk.data.find(path)
    corpusReader = nltk.corpus.PlaintextCorpusReader(folder, file_name)

    # word counter
    file = open(file_path, "rt")
    data = file.read()
    words = data.split()

    global all_sentence_count 
    global all_word_count
    
    all_sentence_count += len(corpusReader.sents())
    all_word_count += len(words)

    print('----------------------------------------------------------')
    print('Title: ' + file_name.rstrip("_nonewline.txt"))
    print("Sentence(s):", len(corpusReader.sents()))
    print("Words:", len(words))
  
  
# iterate through all file
for file in os.listdir():

    # checks text file format
    if file.endswith(".txt"):
        file_path = f"{path}/{file}" # change to \ for windows
  
        # call read text file function
        read_text_file(file_path)


# total tally (for faster tracking purposes mainly)
print('----------------------------------------------------------')
print('----------------------------------------------------------')
print('Current Catalogue Selection')
print('Total Sentence Count: ' + str(all_sentence_count))
print('Total Word Count: ' + str(all_word_count))
print('----------------------------------------------------------')