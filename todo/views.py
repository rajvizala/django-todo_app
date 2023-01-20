from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login_user')
def index(request):
    current_user = request.user
    data = ToDo.objects.filter(user=current_user) #Will filter out records with user as current user
    # data = ToDo.objects.all() Will Give all objects in the todo table
    return render(request, 'home.html', context={'data': data})


def insert(request):
    title = request.POST.get('title')
    description = request.POST.get('desc')
    current_user = request.user
    ToDo(title=title, description=description,user=current_user).save()
    return redirect('index')


def delete(request, id):
    data = ToDo.objects.get(pk=id)
    data.delete()
    return redirect('index')


def update(request, id):
    if request.method == 'POST':
        data = ToDo.objects.get(pk=id)
        title = request.POST.get('title')
        description = request.POST.get('desc')
        data.title = title
        data.description = description
        data.save()
        return redirect('index')

    data = ToDo.objects.get(pk=id)
    return render(request, 'edit.html', context={"data": data})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Incorrect Username or Password..")
    return render(request, 'login.html')


def register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Sucessfully Created..")
            return redirect('login_user')

    return render(request, 'register.html', context={'form': form})


@login_required(login_url='login_user')
def logout_user(request):
    logout(request)
    return redirect('login_user')

