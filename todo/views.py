from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import *

# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        
        context = {}
        return render(request, 'todo/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

   
def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group= Group.objects.get(name='customer')
                user.groups.add(group)

                profile.objects.create(
				user=user,
				name=user.username,
				)

                messages.success(request, 'Account was created for ' + username)
                return redirect('login')
            
        context = {'form':form,}
        return render(request,'todo/register.html',context)

@login_required(login_url='login')
def home (request):

    
    tasks = request.user.profile.todo_set.all()
    form = todoform()
    

    if request.method == 'POST':
        #form = todoform(request.POST)
        print(request.POST)
        
        todo.objects.create(
			title = request.POST.get('title'),
            uid = request.user.profile,
			)
        return redirect('/')  


    context= {
        'tasks':tasks,
        'form': form,
        }

    return render(request,'todo/home.html',context)

@login_required(login_url='login')
def edit (request, pk):
    task = todo.objects.get(id=pk)
    
    form = todoform(instance=task)
   
    if request.method == 'POST':

        task.uid=request.user.profile
        task.title = request.POST.get('title')
        if(request.POST.get('completed')=='on'):
            task.completed = True
        else:
            task.completed = False

        task.save()
        return redirect('home')     

    context= {
        'form': form,
        }    


    return  render(request,'todo/edit.html', context)


'''def delete (request, pk):
    task = todo.objects.get(id=pk)
    
   
    if request.method == 'POST':
        task.delete()
        
        return redirect('/') 

    context= {
        'task': task,
        }    


    return  render(request,'todo/delete.html', context)'''

def delete (request, pk):
    task = todo.objects.get(id=pk)
    task.delete()
    return redirect('/') 


def complete(request,pk):
     task = todo.objects.get(id=pk)
     if task.completed != True:
        task.completed= True
        task.save()
        return redirect('/') 
