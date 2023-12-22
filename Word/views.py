from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Word

class WordSerializer(ModelSerializer):
    level = SerializerMethodField()

    class Meta:
        model = Word
        fields = '__all__'
    
    def get_level(self, obj):
        return obj.get_level_display()

class WordListView(APIView):
    def get(self, request):
        words = Word.objects.all()

        return Response(WordSerializer(words, many=True).data, status=status.HTTP_200_OK)