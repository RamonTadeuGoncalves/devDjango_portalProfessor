"""devDjango_portalProfessor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import urls
from django.contrib import admin
from django.urls import path
from portalProfessor import views
from django.views.generic import RedirectView

urlpatterns = [
    path(r'^admin/', admin.site.urls), 
    path('', RedirectView.as_view(url='home/')),   
    path('lista/', views.listar),
    path('adiciona/', views.adicionar),
    path('item/<int:nr_item>/', views.item),
    path('', views.listar),
    path('home/', views.home),
    path('contato/', views.contato),
    path('excluir/<int:nr_item>/', views.excluir_professor),
    path('/excluir/<int:nr_item>/lista/', views.listar),
    path('editar/<int:nr_item>/', views.atualizar),
]
