from django.shortcuts import render
from.models import *

def home(request):
    data = Home.objects
    return render(request,'home.html',{"data":data})

def piano(request):
    return render(request,'piano.html')

def drum(request):
    return render(request,'drum.html')

def fm(request):
    return render(request,'fm.html')

def guitar(request):
    return render(request,'guitar.html')

def pad(request):
    return render(request,'pad.html')

def music(request):
    return render(request,'music.html')