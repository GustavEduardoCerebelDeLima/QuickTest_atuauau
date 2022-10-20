from django.urls import path
from . import views

urlpatterns = [
    # path('', views.cadastrin , name='login'),
    path('', views.SignUp, name='SignUp'),
    path('criador/<str:link_prova>', views.movel, name='home'),
    path('res/<str:link_prova>', views.resolver, name='resol'),
    path('nota/<str:usuario>/<str:link_prova>', views.nota, name='nota'),
    # path('index/', views.movel, name='criacao'),
    path('home/', views.homepage, name='homepage'),
    path('cadastro/', views.SignUp, name='SignUp'),

]