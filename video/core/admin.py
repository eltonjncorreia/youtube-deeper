from django.contrib import admin

# Register your models here.
from video.core.models import Video, Thumb, Theme, Comment

admin.site.register(Video)
admin.site.register(Thumb)
admin.site.register(Theme)
admin.site.register(Comment)
