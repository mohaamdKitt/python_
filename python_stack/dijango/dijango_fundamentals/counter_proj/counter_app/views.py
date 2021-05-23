from django.shortcuts import render,redirect

def main(request):
    if 'counter' in request.session:
        request.session['counter']+=1
    else:
        request.session['counter']=0
    return render(request,'index.html')
def add2(request):
    request.session['counter']+=1
    return redirect('/')


def destroy(request):
    del request.session['counter']
    return redirect('/')
    
    