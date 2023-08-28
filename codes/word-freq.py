import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import pandas as pd

path = r"C:/Users/Alia/Documents/school/THESIS/Readability-Level-Identifier/clean-txt"
file_name = "Ang Aklatang Pusa_clean.txt"

#SOURCE: https://dev.to/leriaetnasta/word-frequency-counter-using-nltk-40ha
text = open(path + "/" + file_name).read()
text_tokens = word_tokenize(text)
fdist = FreqDist(text_tokens)

df_fdist = pd.DataFrame.from_dict(fdist, orient='index')
df_fdist.columns = ['Frequency']
df_fdist.index.name = 'Word'
print(df_fdist)

out_path = "C:/Users/Alia/Documents/school/THESIS/Readability-Level-Identifier/word-freq output"
out_filename = "[wordfreq] " + file_name
df_fdist.to_csv(out_path + "/" + out_filename)