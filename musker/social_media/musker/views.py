from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'musker/index.html', context)
