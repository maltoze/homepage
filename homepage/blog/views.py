from django.shortcuts import render


def home(request):
    '''首页'''
    return render(request, 'index.html')
