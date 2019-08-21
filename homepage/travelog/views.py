from django.core import serializers
from django.shortcuts import render
from .models import TravelLog


def travel_log(request):
    '''旅行日志页'''
    data = serializers.serialize("json", TravelLog.objects.all())
    return render(request, 'travelog.html', {'tList': data})
