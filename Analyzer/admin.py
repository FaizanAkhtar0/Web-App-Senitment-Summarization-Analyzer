from django.contrib import admin
from Analyzer.models import SentimentModel, SummarizationModel
# Register your models_lib here.

admin.site.register(SentimentModel)
admin.site.register(SummarizationModel)
