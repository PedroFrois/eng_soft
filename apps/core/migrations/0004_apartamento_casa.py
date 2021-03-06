# Generated by Django 2.2.7 on 2019-11-26 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_merge_20191126_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_quartos', models.IntegerField(verbose_name='Número de quartos')),
                ('num_suites', models.IntegerField(verbose_name='Número de suítes')),
                ('num_salas_estar', models.IntegerField(verbose_name='Número de salas de estar')),
                ('num_salas_jantar', models.IntegerField(verbose_name='Número de salas de jantar')),
                ('num_vagas_garagem', models.IntegerField(verbose_name='Número de vagas na garagem')),
                ('area', models.FloatField(verbose_name='Área do imóvel')),
                ('armario_embutido', models.BooleanField(verbose_name='Possui armário embutido')),
                ('descricao', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descrição imóvel')),
                ('andar', models.IntegerField(verbose_name='Andar do apartamento')),
                ('valor_condominio', models.FloatField(verbose_name='Valor do condomínio')),
                ('portaria_24h', models.BooleanField(verbose_name='Possui porteiro 24h')),
                ('endereco', models.CharField(max_length=50, verbose_name='Endereço  do imóvel')),
                ('bairro', models.CharField(max_length=20, verbose_name='Bairro do imóvel')),
                ('valor_aluguel', models.FloatField(verbose_name='Valor do aluguel')),
            ],
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_quartos', models.IntegerField(verbose_name='Número de quartos')),
                ('num_suites', models.IntegerField(verbose_name='Número de suítes')),
                ('num_salas_estar', models.IntegerField(verbose_name='Número de salas de estar')),
                ('num_vagas_garagem', models.IntegerField(verbose_name='Número de vagas na garagem')),
                ('area', models.FloatField(verbose_name='Área do imóvel')),
                ('armario_embutido', models.BooleanField(verbose_name='Possui armário embutido')),
                ('descricao', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descrição do imóvel')),
                ('endereco', models.CharField(max_length=50, verbose_name='Endereço  do imóvel')),
                ('bairro', models.CharField(max_length=20, verbose_name='Bairro do imóvel')),
                ('valor_aluguel', models.FloatField(verbose_name='Valor do aluguel')),
            ],
        ),
    ]
