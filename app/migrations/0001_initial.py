# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome_completo', models.CharField(verbose_name='Nome Completo', max_length=50)),
                ('cpf', models.CharField(verbose_name='CPF', max_length=14, unique=True)),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(verbose_name='Sexo', max_length=10, choices=[('F', 'Feminino'), ('M', 'Masculino')])),
                ('estado_civil', models.CharField(verbose_name='Estado Civil', max_length=10, choices=[('Solteiro', 'Solteiro'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viúvo', 'Viúvo')])),
                ('telefone', models.CharField(verbose_name='Telefone', max_length=19)),
                ('logradouro', models.CharField(verbose_name='Logradouro', max_length=150)),
                ('numero_endereco', models.PositiveIntegerField(verbose_name='Número')),
                ('complemento_endereco', models.CharField(verbose_name='Complemento', max_length=200)),
                ('estado', models.CharField(max_length=15, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia '), ('CE', 'Ceará'), ('DF', 'Distrito Federal '), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('cidade', models.CharField(verbose_name='Cidade', max_length=40)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=254, unique=True)),
                ('senha', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(6)])),
            ],
        ),
    ]
