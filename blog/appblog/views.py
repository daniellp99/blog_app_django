from django.shortcuts import render
from django.http import HttpResponse
from appblog.models import Input

def index(request):
    entradas = Input.objects.all().order_by('-date')[:5]
    output = ', '.join([p.title for p in entradas])
    return HttpResponse(output)