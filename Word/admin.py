from django.contrib import admin
from .models import Word

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'mean', 'sentence', 'is_learned', 'level')
    list_filter = ('is_learned',)