from django.shortcuts import render

from video.core.models import Video


def home(request):
    videos = Video.objects.all()
    return render(request, 'core/home.html', {'videos': videos})


def detail_video(request, pk):
    try:
        details = Video.objects.get(pk=pk)
        details.views + 1
    except Video.DoesNotExist as e:
        raise e

    return render(request, 'core/detail-video.html', {'details': details})


def popular_themes(request):
    themes = Video.objects.all()
    scores(themes.get(pk=1))
    return render(request, 'core/popular-themes.html', {'themes': themes})


def scores(video_id):
    todos_videos = Video.objects.all().prefetch_related('thumbs')
    video = todos_videos.get(pk=video_id)

    thumbs_up = video.thumbs.filter(is_positive=True).count()
    thumbs_down = video.thumbs.filter(is_positive=False).count()

    positive_comments = video.comments.filter(is_positive=True).count()
    negative_comments = video.comments.filter(is_positive=False).count()

    TimeFactor = max(0, 1 - (video.date_uploaded/365))
    GoodComments = positive_comments/(positive_comments+negative_comments)
    ThumbsUp = thumbs_up/(thumbs_up+thumbs_down)
    PositivityFactor = 0.7 * GoodComments + 0.3 * ThumbsUp

    score = video.views * TimeFactor * PositivityFactor
    return score