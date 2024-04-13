from django.shortcuts import render
from django.http import HttpResponse
from .feature_extractor import *
from .flair_model import *

def home(request):
    # Remove images from the static folder
    try:
        image_path = os.path.join(os.getcwd(), 'static', 'wordcloud.png')
        if os.path.exists(image_path):
            os.remove(image_path)
    except Exception as e:
        # Handle any exceptions, such as permission errors
        print(f"Error removing image: {e}")
    
    #Check if images are in the static folder
    wordcloud_exists = os.path.exists(os.path.join(os.getcwd(), 'static', 'wordcloud.png'))
    embeddings_exists = os.path.exists(os.path.join(os.getcwd(), 'static', 'word_embeddings.png'))
    
    
    return render(request, 'home.html', {
        # Your existing context data...
        'wordcloud_exists': wordcloud_exists,
        'embeddings_exists': embeddings_exists
    })

def calculate_readability(request):
   if request.method == 'POST':
        # Check if the text was provided
        text = request.POST.get('text-input', '')
        embeddings = request.POST.get('embed-input', '')
        
        # Save the text input to the session
        request.session['text_input'] = text
        request.session['embed_input'] = embeddings

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
            word_embeddings = wordembed(embeddings)
    
            
            #Check if images are in the static folder
            wordcloud_exists = os.path.exists(os.path.join(os.getcwd(), 'static', 'wordcloud.png'))
           
            return render(request, 'home.html', {
                'text_input': text,
                'word_count': features[0],
                'sentence_count': features[1],
                'ave_word': features[2],
                'ave_sent': features[3],
                'total_syll': features[4],
                'min_prediction': prediction[0][0],
                'max_prediction': prediction[0][1],
                'wordcloud': wordcloud_path,
                'embeddings': word_embeddings,
                
                'wordcloud_exists': wordcloud_exists
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
    wordcloud_path = os.getcwd() + "/static/wordcloud.png"
    return wordcloud_path