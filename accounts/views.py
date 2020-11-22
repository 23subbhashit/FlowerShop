from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import Form
from .models import Img
from django.contrib import messages

from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'accounts/index.html')
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")
def shop(request):
    if request.method == 'POST': 
        form = Form(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('index') 
    else: 
        form = Form() 
    return render(request, 'accounts/shop.html', {'form' : form}) 

def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username ,password = password)
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = { 'form' : form }
    return render(request,'registration/registration.html',context)

def display_images(request): 
  
    if request.method == 'GET':  
        Hotels = Img.objects.all()  
        return render(request, 'accounts/display_plants.html', {'plant_images' : Hotels})

    
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 