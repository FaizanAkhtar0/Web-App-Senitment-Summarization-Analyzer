from django.db import models

# Create your models_lib here.


class SentimentModel(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class SummarizationModel(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

