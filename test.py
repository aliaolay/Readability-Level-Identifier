import stopwordsiso
from stopwordsiso import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer

from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

import nltk
from nltk.tokenize import word_tokenize

import re

import os
from os import path

def word_freq(path, filename):
    stop_words = set(stopwords('tl'))
    
    with open(os.path.join(path, filename), 'r', encoding='utf-8') as file:
        
        text = file.read()
        title, _ = os.path.splitext(filename)
        cleaned_title = re.sub(r'[^a-zA-Z\s]', '', filename).replace('_cleaned', '').replace('cleanedtxt', '')
        others = cleaned_title.split()
        stop_words.update(others)

        tokens = word_tokenize(text)

        filtered = [word.lower() for word in tokens if word.lower() not in stop_words]

        # TF-IDF vectorizer
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(filtered)
        feature_names = tfidf_vectorizer.get_feature_names_out()    # words

        # wordcloud
        wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10)
        wordcloud.generate(' '.join(feature_names))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(cleaned_title)
        # plt.show()
        
        # save to file
        go_to = "tfidf-wordclouds"
        new_path = os.path.join(parent_dir, go_to)
        os.chdir(new_path)
        wordcloud.to_file('[wordcloud]' + filename.removesuffix('_cleaned.txt') + ".png")

curr_path = os.getcwd().replace('\clean-txt', '')

clean_txt_path = curr_path + '/clean-txt'
os.chdir(curr_path)

# mkdir(tfidf-wordclouds)
directory = "tfidf-wordclouds"
check = os.path.isdir(directory)
if check:
    print("Directory already exists.")
else:
    os.makedirs(directory)


# repo
parent_dir = os.path.dirname(clean_txt_path)

for file in os.listdir(clean_txt_path):
    if file.endswith('.txt'):
        word_freq(clean_txt_path, file)

