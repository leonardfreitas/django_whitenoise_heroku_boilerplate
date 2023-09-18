from django.shortcuts import render


def index(request):
    context = {'message': 'Django & WhiteNoise & Heroku'}
    return render(request, 'index.html', context)
