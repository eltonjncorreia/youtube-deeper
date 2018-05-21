# from django.contrib.postgres.fields import ArrayField
from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=255)


class Thumb(models.Model):
    is_positive = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='thumbs')


class Comment(models.Model):
    is_positive = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='comments')


class Video(models.Model):
    title = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now_add=False)
    views = models.IntegerField()
    # themes = ArrayField(models.CharField(max_length=200), blank=True)




