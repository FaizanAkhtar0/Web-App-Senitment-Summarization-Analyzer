import spacy
import en_core_web_md
from spacy import displacy
from django.shortcuts import render

# Create your views here.
from Analyzer.forms import SentimentModelForm, SummarizationModelForm
from Analyzer.models_lib.sentiment_analyzer import SentimentAnalyzer
from Analyzer.models_lib.summarization_analyzer import SummarizationAnalyzer


sentiment_analyzer = SentimentAnalyzer()
summarize_analyzer = SummarizationAnalyzer()
nlp_spacy = en_core_web_md.load()


def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def sentiment_view(request):
    if request.method == 'GET':
        sentimentForm = SentimentModelForm()
        return render(request, 'sentiment.html', {'form': sentimentForm})
    elif request.method == 'POST':
        form = SentimentModelForm(request.POST)
        if form.is_valid():
            form.save()
            input_text = form.cleaned_data['text']
            prediction, confidence = sentiment_analyzer.Sentiment(str(input_text))
            prediction = 'Positive' if prediction == 'pos' else 'Negative'
            return render(request, 'sentiment.html', {'form': form,
                                                      'prediction': prediction, 'confidence': confidence * 100})


def summarize_view(request):
    if request.method == 'GET':
        summarizationForm = SummarizationModelForm()
        return render(request, 'summarize.html', {'form': summarizationForm})
    elif request.method == 'POST':
        form = SummarizationModelForm(request.POST)
        if form.is_valid():
            form.save()
            input_text = form.cleaned_data['text']
            summaray_sentence_list = summarize_analyzer.Summarize(str(input_text))
            summaray = ' '.join(summaray_sentence_list)
            return render(request, 'summarize.html', {'form': form,
                                                      'summaray_result': summaray})

def visualizer_view(request):
    if request.method == 'GET':
        sentimentForm = SentimentModelForm()
        return  render(request, 'visualize.html', {'form': sentimentForm})
    elif request.method == 'POST':
        form = SentimentModelForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['text']
            document = nlp_spacy(str(input_text))
            ner_plot = displacy.render(document, style='ent')
            dep_plot = displacy.render(document, style='dep', options = {"compact": True, "color": "blue"})

            return render(request, 'visualize.html', {'form': form, 'ner_plot': ner_plot, 'dep_plot': dep_plot})


