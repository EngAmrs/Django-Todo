from django.forms import ModelForm , TextInput 
from .models import Todo, TodoItems 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 

class TodoForm(ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
        widget = {
            "title": TextInput(attrs={
                "color": "blue",
                "class": "form-control"
            }),
            "email": TextInput(attrs={
                "color": "blue",
                "class": "form-control"
            }),
        }

class UserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widget = {
            "username": TextInput(attrs={
                "color": "blue",
                "class": "form-control"
                }),
            "email": TextInput(attrs={
                "color": "blue",
                "class": "form-control"
                }),
        }
        
        
class TodoItemsForm(ModelForm):
    class Meta:
        model = TodoItems
        fields = "__all__"
        exclude = ['todo']