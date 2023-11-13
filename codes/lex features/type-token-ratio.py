import os
import nltk
from nltk import *
from nltk.tag.stanford import StanfordPOSTagger
from nltk.tokenize import word_tokenize
import math

# input local path to java.exe
java_path = "C:/Program Files/Java/jre1.8.0_341/bin/java.exe" 
os.environ["JAVAHOME"] = java_path

#path to POS tagger jar
current_dir = os.path.dirname(os.path.realpath(__file__))
jar_path = os.path.abspath(os.path.join(current_dir, "../../"))
jar =  jar_path + "/stanford-postagger.jar"

# path to POS tagger model
model_path = jar_path +"/POSTagger/"
model = model_path + "filipino-left5words-owlqn2-distsim-pref6-inf2.tagger"

pos_tagger = StanfordPOSTagger(model, jar, encoding = "utf-8")

# text input
text = "nagsimula ang lahat sa masukal na bakuran ni aling salvacion."

#tokenize text input
words = nltk.word_tokenize(text)
temp_words = [word for word in words if word.isalnum()] # removes punctuation marks

#tag tokenized words
tagged_words = pos_tagger.tag(temp_words)

# count unique lexical categories
unique_categories = set()
for _, tag in tagged_words:
    tag = tag.split('|')[-1] #removes word before |
    if len(tag) >= 2:  # make sure the tag is not empty
        category = tag[:2]  # extract the first two letters
        unique_categories.add(category)

print("Unique Categories:", unique_categories)

#NUMBER OF UNIQUE CATEGORIES
num_categories = len(unique_categories)
print("Number of Unique Categories:", num_categories)

# TOTAL NUM OF TOKENS
total_token_count = len(temp_words)

# TYPE TOKEN RATIO
ttr = num_categories/total_token_count
print("Type-Token Ratio: ", ttr)

#ROOT TTR
root_ttr = num_categories/math.sqrt(total_token_count)
print("Root Type-Token Ratio: ", root_ttr)

#CORR TTR
corr_ttr = num_categories/math.sqrt(2*total_token_count)
print("Corrected Type-Token Ratio: ", corr_ttr)

#BILOGARITHMIC TTR
log_ttr = math.log(num_categories)/math.log(total_token_count)
print("Bilogarithmic Type-Token Ratio: ", log_ttr)
