#-*- coding: utf-8 -*-

from django import forms

class FormItemAgenda(forms.Form): #herda de forms.Form
	#campos:
	titulo = forms.CharField(max_length=100)
	data = forms.DateField(#conversao
		widget=forms.DateInput(format='%d/%m/%Y'), #campo
		input_formats=['%d/%m/%Y','%d/%m/%y']) #formatp da entrada de dados
	hora=forms.TimeField()
	descricao=forms.CharField()