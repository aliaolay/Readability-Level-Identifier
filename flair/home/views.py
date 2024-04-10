from django.shortcuts import render
from django.http import HttpResponse
from .feature_extractor import *
from .flair_model import *

def home(request):
    return render(request, 'home.html')

def calculate_readability(request):
   if request.method == 'POST':
        # Check if the text was provided
        text = request.POST.get('text-input', '')

        # Check if a file was uploaded
        file = request.FILES.get('file-input')

        if text or file:
            if text:
                # If text is provided, use it
                data = text
            else:
                # If file is uploaded, read its contents
                data = file.read().decode('utf-8')

            features = extract(data)
            prediction = get_pred(*features)
            wordcloud_path = create_wordcloud(data)
           
            return render(request, 'home.html', {
                'word_count': features[0],
                'sentence_count': features[1],
                'ave_word': features[2],
                'ave_sent': features[3],
                'total_syll': features[4],
                'min_prediction': prediction[0][0],
                'max_prediction': prediction[0][1],
                'wordcloud': wordcloud_path
            })
    
        return HttpResponse("No input provided")

def extract(text):
    cleaned_text = text.strip().lower()
    
    wordcount = word_count(cleaned_text)
    sentcount = sentence_count(cleaned_text)
    avewordlength = avg_word_length(cleaned_text)
    avesentlength = avg_sent_length(cleaned_text)
    totalsyll, monosyll, polysyll = count_syllables(cleaned_text)
    
    word_tokens, tagged_text = tag_text(cleaned_text)
    NTR = ntr(word_tokens, tagged_text)
    VTR = vtr(word_tokens, tagged_text)
    TTR, root_ttr, corr_ttr, bilog_ttr = ttr(word_tokens, tagged_text)
    lexdensity = lexical_density(word_tokens, tagged_text)
    FWTR = fwtr(word_tokens, tagged_text)
    
    return wordcount, sentcount, avewordlength, avesentlength, totalsyll, monosyll, polysyll, NTR, VTR, TTR, root_ttr, corr_ttr, bilog_ttr, lexdensity, FWTR

def get_pred(wordcount, sentcount, avewordlength, avesentlength, totalsyll, monosyll, polysyll, ntr, vtr, ttr, root_ttr, corr_ttr, bilog_ttr, lexdensity, fwtr):
    import pickle

    try:
        with open("flair_model.sav", "rb") as model_file:
            model = pickle.load(model_file)
    except FileNotFoundError:
        return "Model file not found"
    except EOFError:
        return "Model file is empty or corrupted"

    try:
        with open("scaler.sav", "rb") as scaler_file:
            scaled = pickle.load(scaler_file)
    except FileNotFoundError:
        return "Scaler file not found"
    except EOFError:
        return "Scaler file is empty or corrupted"

    try:
        prediction = model.predict(scaled.transform([[wordcount, sentcount, avewordlength, avesentlength, totalsyll, monosyll, polysyll, ntr, vtr, ttr, root_ttr, corr_ttr, bilog_ttr, lexdensity, fwtr]]))
        return prediction
    except Exception as e:
        return f"Error occurred during prediction: {str(e)}"
    
def create_wordcloud(text):
    word_freq(text)
    wordcloud_path = os.getcwd() + "/wordcloud.png"
    return wordcloud_path