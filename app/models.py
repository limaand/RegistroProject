from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

# Create your models here.

class Usuario(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
    )
    ESTADO_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia "),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal "),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins")
    )

    ESTADO_CIVIL_CHOICES = (
        ("Solteiro", "Solteiro"),
        ("Casado", "Casado"),
        ("Divorciado", "Divorciado"),
        ("Viúvo", "Viúvo")
    )

    nome_completo = models.CharField(max_length=50, null=False, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, null=False, verbose_name="CPF", unique=True)
    data_nascimento = models.DateField(null=False, verbose_name="Data de Nascimento")
    sexo = models.CharField(null=False, verbose_name="Sexo", choices=SEXO_CHOICES, max_length=10)
    estado_civil = models.CharField(null=False, verbose_name="Estado Civil", choices=ESTADO_CIVIL_CHOICES, max_length=10)
    telefone = models.CharField(null=False, verbose_name="Telefone", max_length=19)
    logradouro = models.CharField(null=False, max_length=150, verbose_name="Logradouro")
    numero_endereco = models.PositiveIntegerField(null=False, verbose_name="Número")
    complemento_endereco = models.CharField(max_length=200, verbose_name="Complemento", null=False)
    estado = models.CharField(null=False, choices=ESTADO_CHOICES, max_length=15)
    cidade = models.CharField(null=False, max_length=40, verbose_name="Cidade")
    email = models.EmailField(null=False, verbose_name="E-mail", unique=True)
    senha = models.CharField(null=False, max_length=100, validators=[MinLengthValidator(6)])

