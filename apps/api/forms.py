from django import forms
from django.forms import ModelForm
from apps.core.models import Pessoa, Endereco, Cliente, Hotel, PrecoPorTemporada, TipoQuarto, Quarto, Locadora, Carro, ReservaCarro, ReservaQuarto, ReservaPacote

#-----------Pessoa
class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

#-----------Endereco
class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'

#-----------Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

#-----------Hotel
class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

#-----------PrecoPorTemporada
class PrecoPorTemporadaForm(forms.ModelForm):
    class Meta:
        model = PrecoPorTemporada
        fields = '__all__'

#-----------TipoQuarto
class TipoQuartoForm(forms.ModelForm):
    class Meta:
        model = TipoQuarto
        fields = '__all__'

#-----------Quarto
class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = '__all__'

#-----------Locadora
class LocadoraForm(forms.ModelForm):
    class Meta:
        model = Locadora
        fields = '__all__'

#-----------Carro
class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = '__all__'

#-----------ReservaCarro
class ReservaCarroForm(forms.ModelForm):
    class Meta:
        model = ReservaCarro
        fields = '__all__'

#-----------ReservaQuarto
class ReservaQuartoForm(forms.ModelForm):
    class Meta:
        model = ReservaQuarto
        fields = '__all__'

#-----------ReservaPacote
class ReservaPacoteForm(forms.ModelForm):
    class Meta:
        model = ReservaPacote
        fields = '__all__'


