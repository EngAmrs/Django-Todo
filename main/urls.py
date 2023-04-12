from django.urls import path
from . import views

urlpatterns =[
    path('' ,views.home , name ='home' ),
    path('detailed/<str:id>' ,views.detailed , name = 'detailed' ),
    path('create/' ,views.createTodo , name = 'create' ),
    path('update/<str:pk>' ,views.updateTodo , name = 'update' ),
    path('delete/<str:pk>' ,views.delete , name = 'delete' ),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
]