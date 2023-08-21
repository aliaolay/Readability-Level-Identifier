import nltk

dirpath = "C:/Users/Alia/Documents/school/THESIS/CODES/txt/" #directory of txt files
filename = "Ang Aklatang Pusa_nonewline.txt"

folder = nltk.data.find(dirpath)
corpusReader = nltk.corpus.PlaintextCorpusReader(folder, filename)

avg = sum(len(sent) for sent in corpusReader.sents()) / len(corpusReader.sents())
print("Average Sentence Length: ", avg)