from datetime import datetime as d
from itertools import count

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from video.core.models import Video, Theme


def home(request):
    videos = Video.objects.all().order_by('title')
    return render(request, 'core/home.html', {'videos': videos})


def detail_video(request, pk=None):
    try:
        details = get_object_or_404(Video, pk=pk)
        details.views = details.views + 1
        details.save(force_update=True)
    except Video.DoesNotExist as e:
        raise e

    return render(request, 'core/detail-video.html', {'details': details})


def popular_themes(request):
    todos = Theme.objects.prefetch_related('videos_themes').order_by('-points')
    for theme in todos:
        for v in theme.videos_themes.all():
            v.points = scores(v.pk)
            v.save(force_update=True)

        for them in theme.videos_themes.filter(themes=theme.pk):
            s = them.points
            print(s)
            s+=s
            theme.points = s
            theme.save(force_update=True)


    return render(request, 'core/popular-themes.html', {'themes': todos})


def scores(video_id):
    todos_videos = Video.objects.all().prefetch_related('thumbs')
    video = todos_videos.get(pk=video_id)

    thumbs_up = video.thumbs.filter(is_positive=True).count()
    thumbs_down = video.thumbs.filter(is_positive=False).count()

    positive_comments = video.comments.filter(is_positive=True).count()
    negative_comments = video.comments.filter(is_positive=False).count()

    if positive_comments < 1:
        positive_comments = 1

    if thumbs_up < 1:
        thumbs_up = 1

    TimeFactor = max(0, 1 - (d.now().date() - video.date_uploaded).days / 365)
    GoodComments = positive_comments/(positive_comments+negative_comments)
    ThumbsUp = thumbs_up/(thumbs_up+thumbs_down)
    PositivityFactor = 0.7 * GoodComments + 0.3 * ThumbsUp

    score = video.views * TimeFactor * PositivityFactor

    return score
