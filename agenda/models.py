#-*- encoding: utf-8 -*-
from django.db import models


# Create your models here.

class ItemAgenda(models.Model):
	#meus atributos
	data = models.DateField()				#armazenará data do evento
	hora= models.TimeField()				#armazenará hora do evento
	titulo=models.CharField(max_length=100) #armazenará título do evento
	descricao=models.TextField()