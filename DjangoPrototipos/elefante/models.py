from django.db import models
from django import forms

# Create your models here.
class Paper(models.Model):
    id_paper = models.AutoField(primary_key=True)
    # title = models.CharField(max_length=255)
    questoes = models.TextField()

class Question(models.Model):
    descrition = models.TextField()
    answer = models.TextField()
    papers = models.ManyToManyField(Paper, through='PaperQuestion')


class PaperQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    paper = models.ForeignKey(Paper, on_delete=models.PROTECT)
    active = models.BooleanField()
    order = models.IntegerField()
    class Meta():
        ordering = ['order']

class dados_cadastro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome


    
    
