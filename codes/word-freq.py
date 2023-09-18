import os
import nltk
nltk.download("punkt")
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import pandas as pd

path = "/Users/stephanie/Desktop/thesis/Readability-Level-Identifier/clean-txt"
file_name = "Ang Aklatang Pusa_cleaned.txt"

# Read the text file
with open(os.path.join(path, file_name), 'r', encoding='utf-8') as file:
    text = file.read()

temp_tokens = word_tokenize(text)
text_tokens = [word for word in temp_tokens if word.isalnum()] # removes punctuation marks
fdist = FreqDist(text_tokens)

# Create a DataFrame from the frequency distribution
df_fdist = pd.DataFrame.from_dict(fdist, orient='index', columns=['Frequency'])
df_fdist.index.name = 'Word'

# Sort the DataFrame by frequency in descending order
df_fdist_sorted = df_fdist.sort_values(by='Frequency', ascending=False)

print(df_fdist_sorted)

out_path = "/Users/stephanie/Desktop/thesis/Readability-Level-Identifier/word-freq output"
out_filename = "[wordfreq] " + file_name
df_fdist_sorted.to_csv(os.path.join(out_path, out_filename), encoding='utf-8')
