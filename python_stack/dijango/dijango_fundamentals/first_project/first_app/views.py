from django.shortcuts import redirect, render,HttpResponse


# def index(request):
#     return render(request,"index.html")

def index(request):
    context={
        "name":"mohammad",
        "favorite_color":"black",
        "pets":["dvcd","dsd","ksmclk"]
    }
    return render(request,"index.html",context)


def blog(request):
    return HttpResponse("placeholder to later display a list of all blogs ")

def newBlog(request):
    return HttpResponse("placeholder to display a new form to create a new blog ")

def creat (request):
     return redirect('/')

def show(request,number):
    return HttpResponse(f'placeholder to display blog number {number}')



def edit(request,number):
    return HttpResponse(f'placeholder to edit blog {number}')

def destroy (request,number):
     return redirect('/blog')


# def root2(reauest):
#     return redirect('/blog')