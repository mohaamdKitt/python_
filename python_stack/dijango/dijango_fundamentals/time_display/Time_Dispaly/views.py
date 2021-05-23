from django.shortcuts import render,redirect
from time import gmtime, strftime



def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)

def te(request):
    if request.method == "GET":
    	print("a GET request is being made to this route")
    	return render(request, "some_template.html")
    if request.method == "POST":
        request.session['name']=request.method == "POST"
    	return redirect("/")