# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Professor
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfessorForm

# Create your views here.

def listar(request):
    lista_itens = Professor.objects.all()
    return render(request, 'lista.html', {'lista_itens': lista_itens})

def editar(request):
    id_professor = request.GET.get('id')    
    print(id_professor)
    dados = {}
    if id_professor:
        dados ['professor'] = Professor.objects.get(id=id_professor)
    
    return render(request, 'edita.html', dados)

def atualizar(request, nr_item):    
    item = get_object_or_404(Professor, pk=nr_item)
    form = ProfessorForm(instance=item)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.matricula = form.cleaned_data['matricula']
            item.nome = form.cleaned_data['nome']
            item.endereco = form.cleaned_data['endereco']
            item.telefone = form.cleaned_data['telefone']
            item.titulacao = form.cleaned_data['titulacao']

            item.save()

            return render(request, 'atualizado.html', {})
        
        else:
            return render(request, 'adiciona.html', {'form':form, 'item': item})
    
    elif (request.method == 'GET'):
        return render(request, 'edita.html', {'form':form, 'item': item})

def adicionar(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'salvo.html', {})
    
    else:
        form = ProfessorForm()
    
    return render(request, 'adiciona.html', {'form':form})

def item(request, nr_item):
    item = get_object_or_404(Professor, pk=nr_item)
    return render(request, 'item.html', {'item': item})

def home(request):
    return render(request, 'home.html')

def contato(request):
    return render(request, 'contato.html')

def excluir_professor(request, nr_item):
    item = get_object_or_404(Professor, pk=nr_item)
    item.delete()
    return render(request, 'excluido.html')
    #return redirect('/lista/')