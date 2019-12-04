# Generated by Django 2.2.7 on 2019-11-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_apartamento_casa'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartamento',
            name='outro_bairro',
            field=models.CharField(blank=True, max_length=20, verbose_name='Outro Bairro'),
        ),
        migrations.AddField(
            model_name='casa',
            name='outro_bairro',
            field=models.CharField(blank=True, max_length=20, verbose_name='Outro Bairro'),
        ),
        migrations.AlterField(
            model_name='apartamento',
            name='bairro',
            field=models.CharField(choices=[('CB', 'Colégio Batista'), ('GM', 'Gameleira'), ('JM', 'Jardim Montanhes'), ('NG', 'Nova Granada'), ('OU', 'Outros')], max_length=20, verbose_name='Bairro do imóvel'),
        ),
        migrations.AlterField(
            model_name='casa',
            name='bairro',
            field=models.CharField(choices=[('CB', 'Colégio Batista'), ('GM', 'Gameleira'), ('JM', 'Jardim Montanhes'), ('NG', 'Nova Granada'), ('OU', 'Outros')], max_length=20, verbose_name='Bairro do imóvel'),
        ),
    ]