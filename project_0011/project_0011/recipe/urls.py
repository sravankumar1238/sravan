from django.urls import path
from . import views

app_name = "recipe"

urlpatterns = [
    path('', views.user_login, name='login'),
    path('index/', views.index, name="index"),
    path('register/', views.user_register, name="register"),
    path('create/', views.create, name="create"),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('logout/', views.user_logout, name='logout'),
]
