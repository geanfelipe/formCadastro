# Create your views here.
#-*- encoding: utf-8 -*-
from models import ItemAgenda
from forms import FormItemAgenda
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import redirect,render_to_response,get_object_or_404




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
			"""
			dados = form.cleaned_data
			item = ItemAgenda(data = dados['data'],hora=dados['hora'],titulo=dados['titulo'],
				descricao=dados['descricao'])
			"""
			form.save()
			return render_to_response("salvo.html",{})

	else:
		#isntance
		form = FormItemAgenda()

	#{'form':form} renderiza o form 
	#chama adiciona.html e passa coomo parametro o form que foi instancia a cima
	#garante que as informacoes relacionadas a requisição serão enviadas para o template
	return render_to_response("adiciona.html",{'form':form},context_instance=RequestContext(request))

#nr_item é parametro do link feito no urls.py

def item(request, nr_item):

	item=get_object_or_404(ItemAgenda,pk=nr_item)
	return render_to_response('item.html',{'item':item},
		context_instance=RequestContext(request))