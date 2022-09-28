from .models import *
from django.forms import ModelForm
from django.core.exceptions import ValidationError

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

    def clean_email(self):
        e = self.cleaned_data['email']
        if dados_cadastro.objects.filter(email=e).exists():
            raise ValidationError("O email já está em uso.".format(e))
        

        

