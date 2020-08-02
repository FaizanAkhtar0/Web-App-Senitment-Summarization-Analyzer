from django import forms
from Analyzer.models import SentimentModel
from Analyzer.models import SummarizationModel

class SentimentModelForm(forms.ModelForm):
    class Meta:
        model = SentimentModel
        fields = '__all__'
        labels = {
            'text': ''
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 15, 'class': "form-control rounded-0 text-area",
                                    'name': "sentimentTextArea"})
        }


class SummarizationModelForm(forms.ModelForm):
    class Meta:
        model = SummarizationModel
        fields = '__all__'
        labels = {
            'text': ''
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 15, 'class': "form-control rounded-0 text-area",
                                    'name': "summerizationTextArea"})
        }

