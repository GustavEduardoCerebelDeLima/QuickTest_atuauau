from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign, name='login'),
    path('cadastro/', views.cadastrin, name='cadastro'),
    path('criador-<int:id_prova>', views.movel, name='criador'),
    path('index/', views.movel, name='criacao'),
    path('login/', views.sign, name='login'),
]