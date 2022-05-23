from django.shortcuts import render
from rest_framework import serializers
from .models import Category, Level, Themes, Words
# Create your views here.


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = '__all__'


class WordsThemesSerializer(serializers.ModelSerializer):
    class Meta(WordsSerializer.Meta):
        fields = ('id', 'name')


class ThemeListSerializer(serializers.ModelSerializer):
    class Meta:
        level = serializers.IntegerField
        model = Themes
        exclude = ('words',)


class ThemeSerializer(serializers.ModelSerializer):
    words = WordsThemesSerializer(many=True)

    class Meta:
        model = Themes
        fields = '__all__'



