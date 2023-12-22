from django.urls import path
from .views import WordListView

urlpatterns = [
    path('words/list', WordListView.as_view())
]