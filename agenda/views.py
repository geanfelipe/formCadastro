# Create your views here.
#-*- encoding: utf-8 -*-
from models import ItemAgenda
from forms import FormItemAgenda
from django.template import RequestContext

from django.shortcuts import render_to_response


def lista(request):
	#forma pra buscar no banco de dados 
	lista_itens = ItemAgenda.objects.all() #mesmo que select * from agenda_itemagenda;
	#abre o arqv lista.html e envia um dicionário contendo as variaveis usadas no template
	return render_to_response("lista.html",{'lista_itens':lista_itens})


#adc a agenda
def adiciona(request):

	if request.method=="POST":
		form = FormItemAgenda(request.POST)
		if form.is_valid(): # se for valido
			dados= form.cleaned_data
			item = ItemAgenda(data=dados['data'],
				hora=dados['hora'],
				titulo=dados['titulo'],
				descricao=dados['descricao'])
		#vai incluir no banco de dados relacional
		item.save()
		#irá msg de form cadastrado
		return render_to_response("salvo.html",{})

	else:
		#isntance
		form = FormItemAgenda()
	#chama adiciona.html e passa coomo parametro o form que foi instancia a cima
	#garante que as informacoes relacionadas a requisição serão enviadas para o template
	return render_to_response("adiciona.html",{'form':form},context_instance=RequestContext(request))
