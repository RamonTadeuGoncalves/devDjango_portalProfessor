# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Professor
from django.shortcuts import render, get_object_or_404
from .forms import ProfessorForm

# Create your views here.

def lista(request):
    lista_itens = Professor.objects.all()
    return render(request, 'lista.html', {'lista_itens': lista_itens})

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