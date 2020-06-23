# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Professor
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfessorForm

# Create your views here.

def lista(request):
    lista_itens = Professor.objects.all()
    return render(request, 'lista.html', {'lista_itens': lista_itens})

def editar(request):
    id_professor = request.GET.get('id')    
    print(id_professor)
    dados = {}
    if id_professor:
        dados ['professor'] = Professor.objects.get(id=id_professor)
    
    return render(request, 'edita.html', dados)

    

def submit_editar(request):
    if request.method == 'POST':
        matricula = request.POST.get('item.matricula')
        nome = request.POST.get('nome')
        titulacao = request.POST.get('titulacao')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        id_professor = request.POST.get('id_professor')
        if id_professor:
            print(matricula)
    
    return redirect('/')




def adiciona(request):
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
    return redirect('/lista/')