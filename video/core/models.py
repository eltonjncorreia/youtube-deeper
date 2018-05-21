from datetime import datetime, timedelta
from django.core.validators import MinValueValidator
from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=255)
    points = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Thumb(models.Model):
    is_positive = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='thumbs')

    def __str__(self):
        return f'{self.video}'


class Comment(models.Model):
    is_positive = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.video}'


class Video(models.Model):
    title = models.CharField(max_length=255)
    date_uploaded = models.DateField(auto_now_add=False,
                                     validators=[MinValueValidator(
                                         datetime.now().date() - timedelta(days=365))])
    views = models.IntegerField(default=0)
    themes = models.ManyToManyField('Theme', related_name='videos_themes')
    points = models.FloatField(default=0)

    def __str__(self):
        return self.title
