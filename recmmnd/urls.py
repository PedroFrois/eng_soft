"""recmmnd URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.api.views import pessoa_create,pessoa_view,pessoa_edit,pessoa_delete,endereco_create,endereco_view,endereco_edit,endereco_delete,cliente_create,cliente_view,cliente_edit,cliente_delete,hotel_view,hotel_create,hotel_edit,hotel_delete,precoPorTemporada_view,precoPorTemporada_create,precoPorTemporada_edit,precoPorTemporada_delete,tipoQuarto_view,tipoQuarto_create,tipoQuarto_edit,tipoQuarto_delete,quarto_view,quarto_create,quarto_edit,quarto_delete,locadora_view,locadora_create,locadora_edit,locadora_delete,carro_create,carro_view,carro_edit,carro_delete,reservaCarro_create,reservaCarro_view,reservaCarro_edit,reservaCarro_delete,reservaQuarto_create,reservaQuarto_view,reservaQuarto_edit,reservaQuarto_delete,reservaPacote_create,reservaPacote_view,reservaPacote_edit,reservaPacote_delete,pessoa,endereco,cliente,hotel,precoPorTemporada,tipoQuarto,quarto,locadora,carro,reservaCarro,reservaQuarto,reservaPacote

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    #Pessoa
    path('pessoa', pessoa, name='pessoa'),
    path('pessoa/create', pessoa_create, name='pessoa_create'),
    path('pessoa/view', pessoa_view, name='pessoa_view'),
    path('pessoa/edit/<int:pessoa_id>', pessoa_edit, name='pessoa_edit'),
    path('pessoa/delete/<int:pessoa_id>', pessoa_delete, name='pessoa_delete'),
    #Endereco
    path('endereco', endereco, name='endereco'),
    path('endereco/create', endereco_create, name='endereco_create'),
    path('endereco/view', endereco_view, name='endereco_view'),
    path('endereco/edit/<int:endereco_id>', endereco_edit, name='endereco_edit'),
    path('endereco/delete/<int:endereco_id>', endereco_delete, name='endereco_delete'),
    #Cliente
    path('cliente', cliente, name='cliente'),
    path('cliente/create', cliente_create, name='cliente_create'),
    path('cliente/view', cliente_view, name='cliente_view'),
    path('cliente/edit/<int:cliente_id>', cliente_edit, name='cliente_edit'),
    path('cliente/delete/<int:cliente_id>', cliente_delete, name='cliente_delete'),
    #Hotel
    path('hotel', hotel, name='hotel'),
    path('hotel/create', hotel_create, name='hotel_create'),
    path('hotel/view', hotel_view, name='hotel_view'),
    path('hotel/edit/<int:hotel_id>', hotel_edit, name='hotel_edit'),
    path('hotel/delete/<int:hotel_id>', hotel_delete, name='hotel_delete'),
    #PrecoPorTemporada
    path('precoPorTemporada', precoPorTemporada, name='precoPorTemporada'),
    path('precoPorTemporada/create', precoPorTemporada_create, name='precoPorTemporada_create'),
    path('precoPorTemporada/view', precoPorTemporada_view, name='precoPorTemporada_view'),
    path('precoPorTemporada/edit/<int:precoPorTemporada_id>', precoPorTemporada_edit, name='precoPorTemporada_edit'),
    path('precoPorTemporada/delete/<int:precoPorTemporada_id>', precoPorTemporada_delete, name='precoPorTemporada_delete'),
    #TipoQuarto
    path('tipoQuarto', tipoQuarto, name='tipoQuarto'),
    path('tipoQuarto/create', tipoQuarto_create, name='tipoQuarto_create'),
    path('tipoQuarto/view', tipoQuarto_view, name='tipoQuarto_view'),
    path('tipoQuarto/edit/<int:tipoQuarto_id>', tipoQuarto_edit, name='tipoQuarto_edit'),
    path('tipoQuarto/delete/<int:tipoQuarto_id>', tipoQuarto_delete, name='tipoQuarto_delete'),
    #Quarto
    path('quarto', quarto, name='quarto'),
    path('quarto/create', quarto_create, name='quarto_create'),
    path('quarto/view', quarto_view, name='quarto_view'),
    path('quarto/edit/<int:quarto_id>', quarto_edit, name='quarto_edit'),
    path('quarto/delete/<int:quarto_id>', quarto_delete, name='quarto_delete'),
    #Locadora
    path('locadora', locadora, name='locadora'),
    path('locadora/create', locadora_create, name='locadora_create'),
    path('locadora/view', locadora_view, name='locadora_view'),
    path('locadora/edit/<int:locadora_id>', locadora_edit, name='locadora_edit'),
    path('locadora/delete/<int:locadora_id>', locadora_delete, name='locadora_delete'),
    #Carro
    path('carro', carro, name='carro'),
    path('carro/create', carro_create, name='carro_create'),
    path('carro/view', carro_view, name='carro_view'),
    path('carro/edit/<int:carro_id>', carro_edit, name='carro_edit'),
    path('carro/delete/<int:carro_id>', carro_delete, name='carro_delete'),
    #ReservaCarro
    path('reservaCarro', reservaCarro, name='reservaCarro'),
    path('reservaCarro/create', reservaCarro_create, name='reservaCarro_create'),
    path('reservaCarro/view', reservaCarro_view, name='reservaCarro_view'),
    path('reservaCarro/edit/<int:reservaCarro_id>', reservaCarro_edit, name='reservaCarro_edit'),
    path('reservaCarro/delete/<int:reservaCarro_id>', reservaCarro_delete, name='reservaCarro_delete'),
    #ReservaQuarto
    path('reservaQuarto', reservaQuarto, name='reservaQuarto'),
    path('reservaQuarto/create', reservaQuarto_create, name='reservaQuarto_create'),
    path('reservaQuarto/view', reservaQuarto_view, name='reservaQuarto_view'),
    path('reservaQuarto/edit/<int:reservaQuarto_id>', reservaQuarto_edit, name='reservaQuarto_edit'),
    path('reservaQuarto/delete/<int:reservaQuarto_id>', reservaQuarto_delete, name='reservaQuarto_delete'),
    #ReservaPacote
    path('reservaPacote', reservaPacote, name='reservaPacote'),
    path('reservaPacote/create', reservaPacote_create, name='reservaPacote_create'),
    path('reservaPacote/view', reservaPacote_view, name='reservaPacote_view'),
    path('reservaPacote/edit/<int:reservaPacote_id>', reservaPacote_edit, name='reservaPacote_edit'),
    path('reservaPacote/delete/<int:reservaPacote_id>', reservaPacote_delete, name='reservaPacote_delete'),
]
