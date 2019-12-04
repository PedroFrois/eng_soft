from django.contrib.auth.models import User
from django.db import models

BAIRROS=[
	('Colégio Batista', "Colégio Batista"),
	('Gameleira', "Gameleira"),
	('Jardim Montanhes', "Jardim Montanhes"),
	('Nova Gradana', "Nova Granada"),
	('Outros', "Outros"),
]

# Create your models here.
class Pessoa(models.Model):
	nome	= models.CharField(verbose_name='Nome', max_length=100)
	cpf		= models.CharField(verbose_name='CPF', max_length=14)
	email	= models.EmailField(verbose_name='Email')
	# user = models.OneToOneField(verbose_name='Usuario', to=User, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome +' '+ self.cpf


class Endereco(models.Model):
	logradouro	= models.CharField(verbose_name='Logradouro', default=' ', max_length=100)
	numero		= models.IntegerField(verbose_name='Número', default=0)
	complemento	= models.CharField(verbose_name='Complemento', default=' ', max_length=20)
	cidade 		= models.CharField(verbose_name='Cidade', default=' ', max_length=20)

	def __str__(self):
		return self.logradouro


class Cliente(models.Model):
	telefone	= models.CharField(verbose_name='Telefone', max_length=14)
	pessoa		= models.OneToOneField(verbose_name='Pessoa', to=Pessoa, on_delete=models.CASCADE)
	endereco	= models.OneToOneField(verbose_name='Endereço', to=Endereco, on_delete=models.CASCADE)

	def __str__(self):
		return self.pessoa.nome +' '+ self.pessoa.cpf


class Hotel(models.Model):
	nome 		= models.CharField(verbose_name='Nome', max_length=100)
	endereco	= models.OneToOneField(verbose_name='Endereço', to=Endereco, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome


class TipoQuarto(models.Model):
	nome		 	= models.CharField(verbose_name='Nome', max_length=100)
	max_ocupantes	= models.IntegerField(verbose_name='Máximo de Ocupantes')
	banheiro_compartilhado	= models.BooleanField(verbose_name='Banheiro Compartilhado')

	def __str__(self):
		return self.nome


class Quarto(models.Model):
	hotel				= models.ForeignKey(verbose_name='Hotel', to=Hotel, on_delete=models.CASCADE)
	num_quarto			= models.IntegerField(verbose_name='Número do Quarto')
	num_camas_solteiro	= models.IntegerField(verbose_name='Camas de Solteiro')
	num_camas_casal		= models.IntegerField(verbose_name='Camas de Casal')
	preco 				= models.FloatField(verbose_name='Preço')
	tipo_quarto			= models.ForeignKey(verbose_name='Tipo do Quarto', to=TipoQuarto, on_delete=models.CASCADE)

	def __str__(self):
		return 'Quarto '+ str(self.num_quarto) +' no hotel ' + self.hotel.nome


class PrecoPorTemporada(models.Model):
	preco 					= models.FloatField(verbose_name='Preço')
	data_inicio_temporada	= models.DateField(verbose_name='Data de Início')
	data_fim_temporada		= models.DateField(verbose_name='Data de Fim') 
	tipo_quarto				= models.ForeignKey(verbose_name='Tipo do Quarto', to=TipoQuarto, on_delete=models.CASCADE)

	def __str__(self):
		return self.preco +' '+ self.tipo_quarto


class Locadora(models.Model):
	nome 		= models.CharField(verbose_name='Nome', max_length=20)
	endereco	= models.OneToOneField(verbose_name='Endereço', to=Endereco, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome


class Carro(models.Model):
	modelo		= models.CharField(verbose_name='Modelo', max_length=20)
	capacidade	= models.IntegerField(verbose_name='Capacidade')
	preco 		= models.FloatField(verbose_name='Preço')
	placa		= models.CharField(verbose_name='Placa', max_length=7)
	locadora	= models.ForeignKey(verbose_name='Locadora', to=Locadora, on_delete=models.CASCADE)

	def __str__(self):
		return self.modelo +' '+ self.placa


class ReservaCarro(models.Model):
	codigo			= models.IntegerField(verbose_name='Codigo')
	data_reserva	= models.DateField(verbose_name='Data de Reserva')
	data_inicio		= models.DateField(verbose_name='Data de Início')
	data_fim		= models.DateField(verbose_name='Data de Fim')
	carro			= models.ForeignKey(verbose_name='Carro', to=Carro, on_delete=models.CASCADE)

	def __str__(self):
		return self.codigo


class ReservaQuarto(models.Model):
	codigo			= models.IntegerField(verbose_name='Codigo')
	data_reserva	= models.DateField(verbose_name='Data de Reserva')
	data_inicio		= models.DateField(verbose_name='Data de Início')
	num_noites		= models.DateField(verbose_name='Quantidade de Noites')
	quarto			= models.ForeignKey(verbose_name='Quarto', to=Quarto, on_delete=models.CASCADE)

	def __str__(self):
		return self.codigo


class ReservaPacote(models.Model):
	reserva_carro	= models.OneToOneField(verbose_name='Reserva do Carrro', to=ReservaCarro, on_delete=models.CASCADE)
	reserva_quarto	= models.OneToOneField(verbose_name='Reserva do Quarto', to=ReservaQuarto, on_delete=models.CASCADE)

	def __str__(self):
		return self.codigo