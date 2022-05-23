from django.db import models


# Create your models here.

class Category(models.Model):
    icon = models.ImageField(upload_to='categories_images')
    name = models.CharField(max_length=50)

    def get_url(self):
        return self.icon.url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'


class Level(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Level'


class Words(models.Model):
    name = models.CharField(max_length=50)
    transcription = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    example = models.TextField()
    sound = models.FileField(upload_to='music')

    def __str__(self):
        return self.name

    def get_url(self):
        return self.sound.url

    class Meta:
        verbose_name_plural = 'Words'


class Themes(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='themes_images')
    level = models.ManyToManyField(Level)
    words = models.ManyToManyField(Words)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_url(self):
        return self.photo.url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Themes'
