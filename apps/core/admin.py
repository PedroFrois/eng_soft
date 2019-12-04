from django.contrib import admin
from apps.core.models import Pessoa, Endereco, Cliente, Hotel, PrecoPorTemporada, TipoQuarto, Quarto, Locadora, Carro, ReservaCarro, ReservaQuarto, ReservaPacote
# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(Cliente)
admin.site.register(Hotel)
admin.site.register(PrecoPorTemporada)
admin.site.register(TipoQuarto)
admin.site.register(Quarto)
admin.site.register(Locadora)
admin.site.register(Carro)
admin.site.register(ReservaCarro)
admin.site.register(ReservaQuarto)
admin.site.register(ReservaPacote)