from django.shortcuts import render


def home(request):
    '''首页'''
    return render(request, 'index.html')


def resume(request):
    '''简历页'''
    return render(request, 'resume.html')
