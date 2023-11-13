# https://github.com/itudidyay/Tagalog-Word-Syllabization-Python
# https://pypi.org/project/syllables/

import os
import nltk
import syllables
from nltk.tokenize import word_tokenize
import pandas as pd

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

# special_consonants = ['bl', 'br', 'dr', 'pl', 'tr']

total_syllables = 0

# def consecutive_vowels(word):
#     vowel_count = 0
#     add_syllable = 0
    
#     for char in word:
#         if char in vowels and vowel_count == 0:
#             vowel_count += 1
#         elif char in vowels and vowel_count >= 1:
#             vowel_count += 1
#             add_syllable += 1
#         else:
#             vowel_count = 0
    
#     return add_syllable


# def consecutive_cons(word):
#     return 0


# no. of vowels == no. of syllables (mostly)
# edge cases: ng, mga, -io/-ao (primarily in names/surnames)
def count_syllables(text):
    global total_syllables
    tokens = word_tokenize(text)

    for token in tokens:
        for char in token:
            if char in vowels:
                total_syllables += 1
        
        # edge cases
        if token == 'ng' or token == 'mga': # edge case ng, mga
            total_syllables += 1
        
        elif (('io') in token): # edge case -io in names/surnames
            total_syllables -= 1

    # for token in tokens:    # var(token) == each word
        
    #     if token == 'mga':  # ma-nga
    #         total_syllables += 1
        
    #     total_syllables += syllables.estimate(token)
    #     total_syllables += consecutive_vowels(token)

    return total_syllables

def main():
    path = "/Users/jerseydayao/Desktop/hckrwmn/repositories/Readability-Level-Identifier/token-sentences"
    file_name = "TEST_Ang Aklatang Pusa_sentenceTokens.txt"

    # Read the text file
    with open(os.path.join(path, file_name), 'r', encoding='utf-8') as file:
        text = file.read()

    total_syllables = count_syllables(text)

    print(f"Total syllables in the text file: {total_syllables}")

if __name__ == "__main__":
    main()






