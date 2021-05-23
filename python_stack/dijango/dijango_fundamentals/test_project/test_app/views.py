from typing import ContextManager
from test_project.settings import LANGUAGE_CODE
from django.shortcuts import redirect, render

def index(request):
    return render(request,'index.html')

def show(request):
    

    Context={
        'name':request.POST['name'],
        'location':request.POST['location'],
        'language':request.POST['language'],
        'text':request.POST['text']
    }

    return render(request,'show.html', Context)