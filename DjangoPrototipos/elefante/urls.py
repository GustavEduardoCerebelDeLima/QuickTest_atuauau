from django.urls import path
from . import views

urlpatterns = [
    path('', views.movel, name='criacao'),
    path('cadastro/', views.cadastrin, name='cadastro'),
    path('login/', views.sign, name='login'),
]