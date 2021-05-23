from django.shortcuts import render,redirect
import random
def index(request):
    if 'gold_counter' not in request.session:
        request.session['gold_counter']=0
        request.session['activate']=[]

    return render(request,'index.html')


def process(request,method='POST'):
    if request.POST['process']== 'farm':
        gold=random.randint(10,20)


    elif request.POST['process']== 'cave':
        gold=random.randint(5,10)


    elif request.POST['process']== 'house':
        gold=random.randint(2,5)

    elif request.POST['process']== 'casino':
        gold=random.randint(-50,50)

    if gold>0:
         request.session['activate'].append('You earned '+ str(gold) +' gold')
    else:
        request.session['activate'].append('You lost '+ str(gold) +' gold')
    request.session['gold_counter']+=gold

    return redirect('/')

def delete(request):
    request.session.clear()
    return redirect('/')