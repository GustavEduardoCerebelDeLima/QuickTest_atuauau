from .models import *
from django.forms import ModelForm

class Cadastro(forms.Form):
    class Meta:
        model = Paper
        fields = [
            'questoes',
        ]

class Registro(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Digite seu email'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Digite sua senha'}))

class cadaa(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Digite sua senha'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Digite seu nome'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Digite seu email'}))
    class Meta:
        model = dados_cadastro
        fields = [
            'nome',
            'email',
            'senha',
        ]
