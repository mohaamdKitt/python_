from django.shortcuts import redirect, render
import random

def index(request):
    return render(request,'index.html')

def prosc(request, method='POST'):
    if 'num' not in request.session:
        request.session['num']=random.randint(1,100)
    num=request.session['num']
    number_from_form = int(request.POST['text'])
    if number_from_form==num:
        return redirect('/winner')
    elif number_from_form < num:
        request.session['test'] = 'Too Low!'
    elif number_from_form > num:
        request.session['test'] = 'Too High!!!!'
    

    return redirect('/result')

def result(request):
    return render(request,'result.html')

def winner(request):
    
    return render(request, 'winner.html')

def play_again(request):
    request.session.clear()
    return redirect('/')