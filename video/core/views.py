from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html', {})


def popular_themes(request):
    return render(request, 'core/popular-themes.html', {})
