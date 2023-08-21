import nltk
from nltk.tokenize import word_tokenize

#uncomment line below if you haven't downloaded punkt so that the code can run
#nltk.download('punkt') 


#SOURCE: https://stackoverflow.com/questions/5074562/how-do-the-count-the-number-of-sentences-words-and-characters-in-a-file


dirpath = "C:/Users/Alia/Documents/school/THESIS/CODES/txt/" #directory of txt files
filename = "Ang Aklatang Pusa_nonewline.txt"

#SENTENCE COUNTER
#file must not contain '\n'
folder = nltk.data.find(dirpath)
corpusReader = nltk.corpus.PlaintextCorpusReader(folder, filename)

print("Number of Sentences: ", len(corpusReader.sents()))

#WORD COUNTER
file = open(dirpath + filename, "rt")
data = file.read()
words = data.split()

print("Number of Words: ", len(words))