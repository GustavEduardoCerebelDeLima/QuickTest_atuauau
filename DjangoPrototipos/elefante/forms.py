from .models import *
from django.forms import ModelForm
from django import forms

class Cadastro(ModelForm):
    class Meta:
        model = Paper
        fields = [
            'usuario',
            'tipo_user',
            'id_prova',
            'tipo_questao',
            'numero_questao',
            'enunciado',
            'letra_questao',
            'texto1',
            'texto2',
            'alt_marcada',
            'alt_erradas',
        ]

class Registro(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Digite seu email'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Digite sua senha'}))

class cadaa(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Digite sua senha'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Digite seu nome'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Digite seu email'}))
    class Meta:
        model = DadosCadastro
        fields = [
            'nome',
            'email',
            'senha',
        ]

class Redefinir(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Digite seu email'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Digite sua senha'}))

        

        

