from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=32)
    mean = models.CharField(max_length=32)
    sentence = models.TextField()
    is_learned = models.BooleanField(default=False)
    
    class WordLevel(models.IntegerChoices):
        A1 = 1, 'A1'
        A2 = 2, 'A2'
        B1 = 3, 'B1'
        B2 = 4, 'B2'
        C1 = 5, 'C1'
        C2 = 6, 'C2'
    
    level = models.IntegerField(default=WordLevel.A1, choices=WordLevel.choices)