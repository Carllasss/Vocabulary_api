from django.db.models import Prefetch
from rest_framework import generics, viewsets

from .models import Category, Words, Themes, Level
from .serializers import CategorySerializer, WordsSerializer, ThemeSerializer, ThemeListSerializer, LevelSerializer

from django.db import connection


class LevelView(generics.ListAPIView):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class WordsView(generics.ListAPIView):
    serializer_class = WordsSerializer
    queryset = Words.objects.all()


class ThemesView(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        queryset = Themes.objects.all()
        category = self.request.query_params.get('category')
        level = self.request.query_params.get('level')

        if level:
            queryset = queryset.filter(level=level).prefetch_related(Prefetch('level', queryset=Level.objects.filter(id=level)))

        if category:
            queryset = queryset.filter(category_id=category)

        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ThemeSerializer
        if self.action == 'list':
            return ThemeListSerializer

