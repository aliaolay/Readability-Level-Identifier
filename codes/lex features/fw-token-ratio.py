import os
import nltk
from nltk import *
from nltk.tag.stanford import StanfordPOSTagger
from nltk.tokenize import word_tokenize

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
text = "hello testing, nagsimula ang lahat sa masukal na bakuran ni aling salvacion."

#tokenize text input
words = nltk.word_tokenize(text)
temp_words = [word for word in words if word.isalnum()] # removes punctuation marks

#tag tokenized words
tagged_words = pos_tagger.tag(temp_words)

# FOREIGN WORD COUNT
fw_count = 0
for word, tag in tagged_words:
    tag = tag.split('|')[-1] #removes word before |
    if tag.startswith('FW'):
        fw_count += 1
        
print("Number of foreign words: ", fw_count)

# FOREIGN WORD - TOKEN RATIO
# = verb_count/total_token_count
total_token_count = len(temp_words)
fw_token_ratio = fw_count/total_token_count

print("Total number of tokens: ", total_token_count)
print("Foreign Word-Token Ratio: ", fw_token_ratio)