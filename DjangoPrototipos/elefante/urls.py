from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign, name='login'),
    path('home/', views.homepage, name='homepage'),
    path('cadastro/', views.cadastrin, name='cadastro'),
    path('criador/<str:link_prova>', views.movel, name='home'),
    path('index/', views.movel, name='criacao'),
    path('login/', views.sign, name='login'),
    path('redefinir/', views.sign, name='redefinir'),
]