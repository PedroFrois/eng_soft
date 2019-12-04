from django.shortcuts import render, redirect
from .forms import PessoaForm, EnderecoForm, ClienteForm, HotelForm, PrecoPorTemporadaForm, TipoQuartoForm, QuartoForm, LocadoraForm, CarroForm, ReservaCarroForm, ReservaQuartoForm, ReservaPacoteForm
from apps.core.models import Pessoa, Endereco, Cliente, Hotel, PrecoPorTemporada, TipoQuarto, Quarto, Locadora, Carro, ReservaCarro, ReservaQuarto, ReservaPacote
from django.forms.models import model_to_dict
# Create your views here.


#------------------Pessoa
def pessoa(request):
    context = dict()
    context['tipo'] = 'pessoas'
    return render(request, 'model.html', context=context)

def pessoa_create(request):
    context = dict()
    context['tipo'] = 'pessoas'
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save()
            return redirect('pessoa_edit', pessoa.id)
    else:
        form = PessoaForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def pessoa_view(request):
    context = dict()
    context['pessoas'] = Pessoa.objects.all()
    context['tipo'] = 'pessoas'
    return render(request, 'view.html', context=context)

def pessoa_edit(request, pessoa_id):
    context = dict()
    pessoa = Pessoa.objects.get(id=pessoa_id)
    context['pessoa'] = pessoa
    context['tipo'] = 'pessoas'
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('pessoa_view')
    else:
        form = PessoaForm(initial=model_to_dict(pessoa))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def pessoa_delete(request, pessoa_id):
    pessoa = Pessoa.objects.get(id=pessoa_id)
    pessoa.delete()
    return redirect('pessoa_view')

#------------------Endereco
def endereco(request):
    context = dict()
    context['tipo'] = 'enderecos'
    return render(request, 'model.html', context=context)

def endereco_create(request):
    context = dict()
    context['tipo'] = 'enderecos'
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            endereco = form.save()
            return redirect('endereco_edit', endereco.id)
    else:
        form = EnderecoForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def endereco_view(request):
    context = dict()
    context['enderecos'] = Endereco.objects.all()
    context['tipo'] = 'enderecos'
    return render(request, 'view.html', context=context)

def endereco_edit(request, endereco_id):
    context = dict()
    endereco = Endereco.objects.get(id=endereco_id)
    context['endereco'] = endereco
    context['tipo'] = 'enderecos'
    if request.method == 'POST':
        form = EnderecoForm(request.POST, instance=endereco)
        if form.is_valid():
            form.save()
            return redirect('endereco_view')
    else:
        form = EnderecoForm(initial=model_to_dict(endereco))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def endereco_delete(request, endereco_id):
    endereco = Endereco.objects.get(id=endereco_id)
    endereco.delete()
    return redirect('endereco_view')

#------------------Cliente
def cliente(request):
    context = dict()
    context['tipo'] = 'clientes'
    return render(request, 'model.html', context=context)

def cliente_create(request):
    context = dict()
    context['tipo'] = 'clientes'
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect('cliente_edit', cliente.id)
    else:
        form = ClienteForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def cliente_view(request):
    context = dict()
    context['clientes'] = Cliente.objects.all()
    context['tipo'] = 'clientes'
    return render(request, 'view.html', context=context)

def cliente_edit(request, cliente_id):
    context = dict()
    cliente = Cliente.objects.get(id=cliente_id)
    context['cliente'] = cliente
    context['tipo'] = 'clientes'
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_view')
    else:
        form = ClienteForm(initial=model_to_dict(cliente))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def cliente_delete(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('cliente_view')

#------------------Hotel
def hotel(request):
    context = dict()
    context['tipo'] = 'hoteis'
    return render(request, 'model.html', context=context)

def hotel_create(request):
    context = dict()
    context['tipo'] = 'hoteis'
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            hotel = form.save()
            return redirect('hotel_edit', hotel.id)
    else:
        form = HotelForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def hotel_view(request):
    context = dict()
    context['hoteis'] = Hotel.objects.all()
    context['tipo'] = 'hoteis'
    return render(request, 'view.html', context=context)

def hotel_edit(request, hotel_id):
    context = dict()
    hotel = Hotel.objects.get(id=hotel_id)
    context['hotel'] = hotel
    context['tipo'] = 'hoteis'
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotel_view')
    else:
        form = HotelForm(initial=model_to_dict(hotel))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def hotel_delete(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    hotel.delete()
    return redirect('hotel_view')

#------------------PrecoPorTemporada
def precoPorTemporada(request):
    context = dict()
    context['tipo'] = 'precoPorTemporadas'
    return render(request, 'model.html', context=context)

def precoPorTemporada_create(request):
    context = dict()
    context['tipo'] = 'precoPorTemporadas'
    if request.method == 'POST':
        form = PrecoPorTemporadaForm(request.POST)
        if form.is_valid():
            precoPorTemporada = form.save()
            return redirect('precoPorTemporada_edit', precoPorTemporada.id)
    else:
        form = PrecoPorTemporadaForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def precoPorTemporada_view(request):
    context = dict()
    context['precoPorTemporadas'] = PrecoPorTemporada.objects.all()
    context['tipo'] = 'precoPorTemporadas'
    return render(request, 'view.html', context=context)

def precoPorTemporada_edit(request, precoPorTemporada_id):
    context = dict()
    precoPorTemporada = PrecoPorTemporada.objects.get(id=precoPorTemporada_id)
    context['precoPorTemporada'] = precoPorTemporada
    context['tipo'] = 'precoPorTemporadas'
    if request.method == 'POST':
        form = PrecoPorTemporadaForm(request.POST, instance=precoPorTemporada)
        if form.is_valid():
            form.save()
            return redirect('precoPorTemporada_view')
    else:
        form = PrecoPorTemporadaForm(initial=model_to_dict(precoPorTemporada))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def precoPorTemporada_delete(request, precoPorTemporada_id):
    precoPorTemporada = PrecoPorTemporada.objects.get(id=precoPorTemporada_id)
    precoPorTemporada.delete()
    return redirect('precoPorTemporada_view')

#------------------TipoQuarto
def tipoQuarto(request):
    context = dict()
    context['tipo'] = 'tipoQuartos'
    return render(request, 'model.html', context=context)

def tipoQuarto_create(request):
    context = dict()
    context['tipo'] = 'tipoQuartos'
    if request.method == 'POST':
        form = TipoQuartoForm(request.POST)
        if form.is_valid():
            tipoQuarto = form.save()
            return redirect('tipoQuarto_edit', tipoQuarto.id)
    else:
        form = TipoQuartoForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def tipoQuarto_view(request):
    context = dict()
    context['tipoQuartos'] = TipoQuarto.objects.all()
    context['tipo'] = 'tipoQuartos'
    return render(request, 'view.html', context=context)

def tipoQuarto_edit(request, tipoQuarto_id):
    context = dict()
    tipoQuarto = TipoQuarto.objects.get(id=tipoQuarto_id)
    context['tipoQuarto'] = tipoQuarto
    context['tipo'] = 'tipoQuartos'
    if request.method == 'POST':
        form = TipoQuartoForm(request.POST, instance=tipoQuarto)
        if form.is_valid():
            form.save()
            return redirect('tipoQuarto_view')
    else:
        form = TipoQuartoForm(initial=model_to_dict(tipoQuarto))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def tipoQuarto_delete(request, tipoQuarto_id):
    tipoQuarto = TipoQuarto.objects.get(id=tipoQuarto_id)
    tipoQuarto.delete()
    return redirect('tipoQuarto_view')

#------------------Quarto
def quarto(request):
    context = dict()
    context['tipo'] = 'quartos'
    return render(request, 'model.html', context=context)

def quarto_create(request):
    context = dict()
    context['tipo'] = 'quartos'
    if request.method == 'POST':
        form = QuartoForm(request.POST)
        if form.is_valid():
            quarto = form.save()
            return redirect('quarto_edit', quarto.id)
    else:
        form = QuartoForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def quarto_view(request):
    context = dict()
    context['quartos'] = Quarto.objects.all()
    context['tipo'] = 'quartos'
    return render(request, 'view.html', context=context)

def quarto_edit(request, quarto_id):
    context = dict()
    quarto = Quarto.objects.get(id=quarto_id)
    context['quarto'] = quarto
    context['tipo'] = 'quartos'
    if request.method == 'POST':
        form = QuartoForm(request.POST, instance=quarto)
        if form.is_valid():
            form.save()
            return redirect('quarto_view')
    else:
        form = QuartoForm(initial=model_to_dict(quarto))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def quarto_delete(request, quarto_id):
    quarto = Quarto.objects.get(id=quarto_id)
    quarto.delete()
    return redirect('quarto_view')

#------------------Locadora
def locadora(request):
    context = dict()
    context['tipo'] = 'locadoras'
    return render(request, 'model.html', context=context)

def locadora_create(request):
    context = dict()
    context['tipo'] = 'locadoras'
    if request.method == 'POST':
        form = LocadoraForm(request.POST)
        if form.is_valid():
            locadora = form.save()
            return redirect('locadora_edit', locadora.id)
    else:
        form = LocadoraForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def locadora_view(request):
    context = dict()
    context['locadoras'] = Locadora.objects.all()
    context['tipo'] = 'locadoras'
    return render(request, 'view.html', context=context)

def locadora_edit(request, locadora_id):
    context = dict()
    locadora = Locadora.objects.get(id=locadora_id)
    context['locadora'] = locadora
    context['tipo'] = 'locadoras'
    if request.method == 'POST':
        form = LocadoraForm(request.POST, instance=locadora)
        if form.is_valid():
            form.save()
            return redirect('locadora_view')
    else:
        form = LocadoraForm(initial=model_to_dict(locadora))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def locadora_delete(request, locadora_id):
    locadora = Locadora.objects.get(id=locadora_id)
    locadora.delete()
    return redirect('locadora_view')

#--------------------Carro
def carro(request):
    context = dict()
    context['tipo'] = 'carros'
    return render(request, 'model.html', context=context)

def carro_create(request):
    context = dict()
    context['tipo'] = 'carros'
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            carro = form.save()
            return redirect('carro_edit', carro.id)
    else:
        form = CarroForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def carro_view(request):
    context = dict()
    context['carros'] = Carro.objects.all()
    context['tipo'] = 'carros'
    return render(request, 'view.html', context=context)

def carro_edit(request, carro_id):
    context = dict()
    carro = Carro.objects.get(id=carro_id)
    context['carro'] = carro
    context['tipo'] = 'carros'
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('carro_view')
    else:
        form = CarroForm(initial=model_to_dict(carro))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def carro_delete(request, carro_id):
    carro = Carro.objects.get(id=carro_id)
    carro.delete()
    return redirect('carro_view')

#--------------------ReservaCarro
def reservaCarro(request):
    context = dict()
    context['tipo'] = 'reservaCarros'
    return render(request, 'model.html', context=context)

def reservaCarro_create(request):
    context = dict()
    context['tipo'] = 'reservaCarros'
    if request.method == 'POST':
        form = ReservaCarroForm(request.POST)
        if form.is_valid():
            reservaCarro = form.save()
            return redirect('reservaCarro_edit', reservaCarro.id)
    else:
        form = ReservaCarroForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def reservaCarro_view(request):
    context = dict()
    context['reservaCarros'] = ReservaCarro.objects.all()
    context['tipo'] = 'reservaCarros'
    return render(request, 'view.html', context=context)

def reservaCarro_edit(request, reservaCarro_id):
    context = dict()
    reservaCarro = ReservaCarro.objects.get(id=reservaCarro_id)
    context['reservaCarro'] = reservaCarro
    context['tipo'] = 'reservaCarros'
    if request.method == 'POST':
        form = ReservaCarroForm(request.POST, instance=reservaCarro)
        if form.is_valid():
            form.save()
            return redirect('reservaCarro_view')
    else:
        form = ReservaCarroForm(initial=model_to_dict(reservaCarro))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def reservaCarro_delete(request, reservaCarro_id):
    reservaCarro = ReservaCarro.objects.get(id=reservaCarro_id)
    reservaCarro.delete()
    return redirect('reservaCarro_view')

#--------------------ReservaQuarto
def reservaQuarto(request):
    context = dict()
    context['tipo'] = 'reservaQuartos'
    return render(request, 'model.html', context=context)

def reservaQuarto_create(request):
    context = dict()
    context['tipo'] = 'reservaQuartos'
    if request.method == 'POST':
        form = ReservaQuartoForm(request.POST)
        if form.is_valid():
            reservaQuarto = form.save()
            return redirect('reservaQuarto_edit', reservaQuarto.id)
    else:
        form = ReservaQuartoForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def reservaQuarto_view(request):
    context = dict()
    context['reservaQuartos'] = ReservaQuarto.objects.all()
    context['tipo'] = 'reservaQuartos'
    return render(request, 'view.html', context=context)

def reservaQuarto_edit(request, reservaQuarto_id):
    context = dict()
    reservaQuarto = ReservaQuarto.objects.get(id=reservaQuarto_id)
    context['reservaQuarto'] = reservaQuarto
    context['tipo'] = 'reservaQuartos'
    if request.method == 'POST':
        form = ReservaQuartoForm(request.POST, instance=reservaQuarto)
        if form.is_valid():
            form.save()
            return redirect('reservaQuarto_view')
    else:
        form = ReservaQuartoForm(initial=model_to_dict(reservaQuarto))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def reservaQuarto_delete(request, reservaQuarto_id):
    reservaQuarto = ReservaQuarto.objects.get(id=reservaQuarto_id)
    reservaQuarto.delete()
    return redirect('reservaQuarto_view')

#--------------------ReservaPacote
def reservaPacote(request):
    context = dict()
    context['tipo'] = 'reservaPacotes'
    return render(request, 'model.html', context=context)

def reservaPacote_create(request):
    context = dict()
    context['tipo'] = 'reservaPacotes'
    if request.method == 'POST':
        form = ReservaPacoteForm(request.POST)
        if form.is_valid():
            reservaPacote = form.save()
            return redirect('reservaPacote_edit', reservaPacote.id)
    else:
        form = ReservaPacoteForm()
        context['form'] = form
    return render(request, 'create.html', context=context)

def reservaPacote_view(request):
    context = dict()
    context['reservaPacotes'] = ReservaPacote.objects.all()
    context['tipo'] = 'reservaPacotes'
    return render(request, 'view.html', context=context)

def reservaPacote_edit(request, reservaPacote_id):
    context = dict()
    reservaPacote = ReservaPacote.objects.get(id=reservaPacote_id)
    context['reservaPacote'] = reservaPacote
    context['tipo'] = 'reservaPacotes'
    if request.method == 'POST':
        form = ReservaPacoteForm(request.POST, instance=reservaPacote)
        if form.is_valid():
            form.save()
            return redirect('reservaPacote_view')
    else:
        form = ReservaPacoteForm(initial=model_to_dict(reservaPacote))
        context['form'] = form
    return render(request, 'edit.html', context=context)

def reservaPacote_delete(request, reservaPacote_id):
    reservaPacote = ReservaPacote.objects.get(id=reservaPacote_id)
    reservaPacote.delete()
    return redirect('reservaPacote_view')
