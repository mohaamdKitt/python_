from typing import ContextManager
from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def root(request):
    name=request.POST['name']
    location=request.POST['location']
    language=request.POST['lang']
    text=request.POST['txt']

    context={
        'name':name,
        'location':location,
        'language':language,
        'text':text
    }
    return render(request,'show.html',context)