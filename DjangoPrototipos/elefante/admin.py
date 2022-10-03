from django.contrib import admin
from .models import DadosCadastro, Paper, Prova

# Register your models here.
admin.site.register(Paper)
admin.site.register(DadosCadastro)
admin.site.register(Prova)