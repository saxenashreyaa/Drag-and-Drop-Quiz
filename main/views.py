from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 
from .forms import NewUserForm
from .models import Quiz


def homepage(request):
    return render(request=request,
                  template_name='main/homepage.html')

def single_slug(request, single_slug):
        question = [q.ques_slug for q in Quiz.objects.all()]
        if single_slug in question:
            this_tutorial = Quiz.objects.get(ques_slug=single_slug)
            #tutorials_from_series = Quiz.objects.all
            #this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)
            return render(request = request,
                      template_name='main/questions.html',
                      context = {"que":this_tutorial,"sidebar": Quiz.objects.all})
        else:
            return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")

def t(request):
    return render(request=request,
                  template_name='main/t.html')
    
   
def questions(request):
    return render(request=request,
       template_name='main/questions.html',context={"sidebar": Quiz.objects.all})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username') 
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            return redirect("main:login")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

        return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    
    form = NewUserForm
    return render(request=request,template_name="main/register.html",context={"form":form})
    
def logout_request(request):
    logout(request)
    messages.info(request, f"Logged out successfully")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST": 
       form = AuthenticationForm(request, data = request.POST)
       if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Logged in as: {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password") 
     
    form = AuthenticationForm()
    #messages.error(request, "Invalid username or password") 

    return render(request,"main/login.html",{"form":form})