from django.shortcuts import render
from django.shortcuts import render, redirect 
from .models import Task
from taskapp.forms import TaskForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('show')
        else:
            messages.error(request, ("Your account does not exist !"))
            return redirect( 'login')
    else:
        return render(request, 'authenticate/login.html', {})
def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successfull"))
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'authenticate/register.html', {'form': form})
    

#overview of all
@login_required(login_url="/login/")  
def show(request):  
    task = Task.objects.filter(user=request.user)  # Filter tasks by the currently logged-in user
    return render(request, "show.html", {'task': task})  

@login_required(login_url="/login/")  
def data(request):  
    if request.method == "POST":  
        form = TaskForm(request.POST)  
        if form.is_valid():             
            try:  
                task = form.save(commit=False)
                task.user = request.user  # Associate the task with the current user
                task.save()  
                return redirect('show')  
            except:  
                pass  
    else:  
        form = TaskForm()  
    return render(request,'index.html', {'form':form}) 


@login_required(login_url="/")
def edit(request, id):  
    task = Task.objects.get(id=id)  
    return render(request,'edit.html', {'task':task})

@login_required(login_url="/")
def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/show")
    return render(request, 'edit.html', {'form': form, 'task': task})

@login_required(login_url="/")
def destroy(request, id):  
    task = Task.objects.get(id=id)  
    task.delete()  
    return redirect("/show")