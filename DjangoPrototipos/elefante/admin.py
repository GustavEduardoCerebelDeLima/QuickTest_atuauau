from django.contrib import admin
from .models import dados_cadastro, Paper

# Register your models here.
admin.site.register(Paper)
admin.site.register(dados_cadastro)