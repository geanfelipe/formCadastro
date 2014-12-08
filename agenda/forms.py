#-*- coding: utf-8 -*-

#from django import forms
from django.forms import ModelForm
from agenda.models import ItemAgenda
from models import ItemAgenda
from django import forms


class FormItemAgenda(forms.ModelForm):
	"""data = forms.DateField(
	widget=forms.DateInput(format='%d/%m/%Y'),
	input_formats=['%d/%m/%Y', '%d/%m/%y'])"""
	
	class Meta:
		model = ItemAgenda
		fields = ('titulo', 'data', 'hora', 'descricao')
