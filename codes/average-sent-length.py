import nltk

dirpath = "" #directory of txt files
filename = ""

folder = nltk.data.find(dirpath)
corpusReader = nltk.corpus.PlaintextCorpusReader(folder, filename)

# SOURCE: https://stackoverflow.com/questions/35900029/average-sentence-length-for-every-text-in-corpus-python3-nltk
avg = sum(len(sent) for sent in corpusReader.sents()) / len(corpusReader.sents())
print("Average Sentence Length: ", avg)