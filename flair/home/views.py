from django.shortcuts import render
from django.http import HttpResponse
from .feature_extractor import *

def home(request):
    return render(request, 'home.html')

def extract(text):
    cleaned_text = text.strip().lower()
    
    wordcount = word_count(cleaned_text)
    sentcount = sentence_count(cleaned_text)
    avewordlength = avg_word_length(cleaned_text)
    avesentlength = avg_sent_length(cleaned_text)
    totalsyll, monosyll, polysyll = count_syllables(cleaned_text)
    
    word_tokens, tagged_text = tag_text(cleaned_text)
    ntr = ntr(word_tokens, tagged_text)
    vtr = vtr(word_tokens, tagged_text)
    ttr, root_ttr, corr_ttr, bilog_ttr = ttr(word_tokens, tagged_text)
    lexdensity = lexical_density(word_tokens, tagged_text)
    fwtr = fwtr(word_tokens, tagged_text)
    
    return wordcount, sentcount, avewordlength, avesentlength, totalsyll, monosyll, polysyll, ntr, vtr, ttr, root_ttr, corr_ttr, bilog_ttr, lexdensity, fwtr

def get_pred(wordcount, sentcount, avewordlength, avesentlength, totalsyll, monosyll, polysyll, ntr, vtr, ttr, root_ttr, corr_ttr, bilog_ttr, lexdensity, fwtr):
    
    return 0
