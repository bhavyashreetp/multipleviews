from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1><marquee>this is my second template</marquee></h1>')

def second(request):
    return HttpResponse('<h1>HAI GOOD MORNING</h1>')


def third(request):
    return render(request,'home1.html')

def four(request):
    return render(request,'home1.html')



