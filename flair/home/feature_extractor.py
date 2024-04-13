import os
from os import path
import nltk
from nltk import *
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.tag.stanford import StanfordPOSTagger
import math
import string
import re
import syllables
import csv
import pandas as pd
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import stopwordsiso
from stopwordsiso import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import shutil
import fasttext

# CURRENT PATH
curr_path = os.getcwd()

# POS-Tagger SET UP
# input local path to java.exe
java_path = os.path.realpath(shutil.which("java"))
os.environ["JAVAHOME"] = java_path
jar =  curr_path + "/stanford-postagger.jar"

# path to POS tagger model
model_path = curr_path +"/POSTagger/"
model = model_path + "filipino-left5words-owlqn2-distsim-pref6-inf2.tagger"
pos_tagger = StanfordPOSTagger(model, jar, encoding = "utf-8")

# WORD COUNT
def word_count(text):
    words = text.split()
    return len(words)

# SENTENCE COUNT
def sentence_count(text):
    sents = nltk.sent_tokenize(text)
    return len(sents)

# AVERAGE WORD LENGTH
def avg_word_length(text):
    words = text.split()
    total_word_length = sum(len(word) for word in words)
    avg = total_word_length / len(words)

    return avg

# AVERAGE SENTENCE LENGTH
def avg_sent_length(text):
    sentences = nltk.sent_tokenize(text)
    avg = sum(len(sent.split()) for sent in sentences) / len(sentences)

    return avg

# SYLLABLE COUNTS
# https://github.com/itudidyay/Tagalog-Word-Syllabization-Python
# https://pypi.org/project/syllables/

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

def count_syllables(text):

    total_syllables = 0
    monosyl_count = 0
    polysyl_count = 0
    
    tokens = word_tokenize(text)

    for token in tokens:
        syllable_count = 0
        for char in token:
            if char.lower() in vowels:
                total_syllables += 1
                syllable_count += 1
        
        # edge cases
        if token == 'ng' or token == 'mga': # edge case ng, mga
            total_syllables += 1
            syllable_count += 1
        
        elif (('io') in token): # edge case -io in names/surnames
            total_syllables -= 1
            syllable_count -= 1
            
        if syllable_count == 1:
            monosyl_count += 1
        elif syllable_count > 1:
            polysyl_count += 1

    return total_syllables, monosyl_count, polysyl_count

def word_freq(input_data):
    stop_words = set(stopwords('tl'))
    
    if isinstance(input_data, str):  # If input_data is text
        text = input_data
    else:  # If input_data is a file
        text = input_data.read().decode('utf-8')

    # Process text and remove stopwords
    cleaned_text = ' '.join([word.lower() for word in word_tokenize(text) if word.lower() not in stop_words])

    # TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([cleaned_text])
    feature_names = tfidf_vectorizer.get_feature_names_out()    # words

    # wordcloud
    wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10)
    wordcloud.generate_from_frequencies({word: 1 for word in feature_names}) 
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    save_directory = os.getcwd() + "/static"
    image_name = "wordcloud.png"
    image_path = os.path.join(save_directory, image_name)
    wordcloud.to_file(image_path)

    return image_name

#POS TAGGER
def tag_text(text):
    words = nltk.word_tokenize(text)
    tagged_words = pos_tagger.tag(words)
    return words, tagged_words
    
# NOUN COUNT
def ntr(words, tagged):
    noun_count = 0
    for word, tag in tagged:
        tag = tag.split('|')[-1] #removes word before |
        if tag.startswith('NN'):
            noun_count += 1
        
    total_token_count = len(words)
    noun_token_ratio = noun_count/total_token_count

    return noun_token_ratio

# VERB COUNT
def vtr(words, tagged):
    verb_count = 0
    for word, tag in tagged:
        tag = tag.split('|')[-1] #removes word before |
        if tag.startswith('VB'):
            verb_count += 1

    total_token_count = len(words)
    verb_token_ratio = verb_count/total_token_count

    return verb_token_ratio

#TYPE-TOKEN RATIO
def ttr(words, tagged):
# count unique lexical categories
    unique_categories = set()
    for _, tag in tagged:
        tag = tag.split('|')[-1] #removes word before |
        if len(tag) >= 2:  # make sure the tag is not empty
            category = tag[:2]  # extract the first two letters
            unique_categories.add(category)

    # print("Unique Categories:", unique_categories)

    #NUMBER OF UNIQUE CATEGORIES
    num_categories = len(unique_categories)
    # print("Number of Unique Categories:", num_categories)

    # TOTAL NUM OF TOKENS
    total_token_count = len(words)

    # TYPE TOKEN RATIO
    ttr = num_categories/total_token_count
    # print("Type-Token Ratio: ", ttr)

    #ROOT TTR
    root_ttr = num_categories/math.sqrt(total_token_count)
    # print("Root Type-Token Ratio: ", root_ttr)

    #CORR TTR
    corr_ttr = num_categories/math.sqrt(2*total_token_count)
    # print("Corrected Type-Token Ratio: ", corr_ttr)

    #BILOGARITHMIC TTR
    denominator = math.log(total_token_count)

    if denominator == 0:
        log_ttr = 0
    else:
        log_ttr = math.log(num_categories)/math.log(total_token_count)
    # print("Bilogarithmic Type-Token Ratio: ", log_ttr)

    return ttr, root_ttr, corr_ttr, log_ttr

#LEXICAL DENSITY

def lexical_density(words, tagged):

    # NUMBER OF LEXICAL WORDS
    # count number of nouns, verbs, adjectives, and adverbs
    num_lexwords = 0
    for word, tag in tagged:
        tag = tag.split('|')[-1] #removes word before |
        if tag.startswith('NN') or tag.startswith('VB') or tag.startswith('JJ') or tag.startswith('RB'):
            num_lexwords += 1
            
    # print("Number of lexical words: ", num_lexwords)

    # LEXICAL DENSITY
    # = lex_density/total_token_count
    total_token_count = len(words)
    lex_density = num_lexwords/total_token_count

    return lex_density


# FOREIGN WORD TOKEN RATIO
def fwtr(words, tagged):
    # FOREIGN WORD COUNT
    fw_count = 0
    for word, tag in tagged:
        tag = tag.split('|')[-1] #removes word before |
        if tag.startswith('FW'):
            fw_count += 1
            
    # print("Number of foreign words: ", fw_count)

    # FOREIGN WORD - TOKEN RATIO
    # = fw_count/total_token_count
    total_token_count = len(words)
    fw_token_ratio = fw_count/total_token_count

    return fw_token_ratio

#WORD EMBEDDINGS (fasttext)
def wordembed(word):
    # pre-trained model
    # https://fasttext.cc/docs/en/crawl-vectors.html
    model = fasttext.load_model('cc.tl.300.bin')

    # uses
    find = word
    similar = model.get_nearest_neighbors(find, k=100)                      # this is more like a bypass to not get repeated words
    filtered = [word for word in similar if find not in word[1]]    # filter
    filitered = filtered[:20]                                # gets top 20 based on the filter
        
    wordList = [item[1] for item in filtered]

    wordList = ', '.join(wordList)

    return(wordList)

# print("Total number of tokens: ", total_token_count)
# print("Foreign Word-Token Ratio: ", fw_token_ratio)