# https://github.com/itudidyay/Tagalog-Word-Syllabization-Python
# https://pypi.org/project/syllables/

import os
import nltk
import syllables
from nltk.tokenize import word_tokenize
import pandas as pd

def count_syllables(text):
    tokens = word_tokenize(text)
    total_syllables = 0

    for token in tokens:
        total_syllables += syllables.estimate(token)

    return total_syllables

def main():
    path = "/Users/stephanie/Desktop/thesis/Readability-Level-Identifier/token-sentences"
    file_name = "TEST_Ang Aklatang Pusa_sentenceTokens.txt"

    # Read the text file
    with open(os.path.join(path, file_name), 'r', encoding='utf-8') as file:
        text = file.read()

    total_syllables = count_syllables(text)

    print(f"Total syllables in the text file: {total_syllables}")

if __name__ == "__main__":
    main()






