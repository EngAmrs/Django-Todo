from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Todo,TodoItems
from .forms import TodoForm

from .forms import TodoForm, UserCreationForm, TodoItemsForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



def home(request):
    todos = Todo.objects.all()
    todosCount = Todo.objects.count()
    context = {
        "todos" : todos,
        "todosCount" : todosCount
    }
    return render(request,'home.html', context)

def detailed(request , id):
    todo = Todo.objects.get(id = id)
    items = todo.todoitems_set.all()
    context={
        "todo": todo,
        "items" :items
    }
    return render(request , 'detailed.html' , context)


def createTodo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request , 'create.html' , context)


def updateTodo(request , pk):
    todo = Todo.objects.get(id= pk)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST , instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request , 'update.html' , context)



def delete(request , pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')



def loginUser(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username, password=password) # ---> to find this user from database or not
        if user is not None:
            login(req, user)
            return redirect('/')
        else:
            return redirect('/')
    context = {
    }
    return render(req, "login.html", context)



def logoutUser(req):
    logout(req)
    return redirect('/')


def register(req):
    form = UserCreationForm()
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save() 
        else:
            print (form.errors)
        return redirect('/')
    context = {
        "form": form
    }
    return render(req, "register.html", context)

