from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign, name='login'),
    path('cadastro/', views.cadastrin, name='cadastro'),
    path('index/', views.movel, name='criacao'),
    path('login/', views.sign, name='login'),
]