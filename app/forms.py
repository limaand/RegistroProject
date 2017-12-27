from django import forms
from .models import *
from input_mask.widgets import InputMask
from django_localflavor_br.forms import BRCPFField, BRPhoneNumberField
from input_mask.contrib.localflavor.br.widgets import BRCPFInput, BRPhoneNumberInput

class DataCustomInput(InputMask):
    mask = {
        'mask': '99/99/9999',
    }

class UsuarioForm(forms.ModelForm):
    nome_completo = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}), label="Nome Completo")

    cpf = BRCPFField(widget= BRCPFInput(
            attrs={'class': 'form-control','data-mask': '000.000.000-00', 'required': 'true'}), label="CPF")

    data_nascimento = forms.DateField(widget=DataCustomInput(
            attrs={'class': 'form-control', 'data-mask': '00/00/0000', 'required': 'true'}), label="Data de Nascimento")

    sexo = forms.Select(
        attrs={'class': 'form-control', 'required': 'true'})

    estado_civil = forms.Select(
        attrs={'class': 'form-control', 'required': 'true'})

    telefone = BRPhoneNumberField(widget=BRPhoneNumberInput(
            attrs={'class': 'form-control', 'data-mask': '(00) 00000-0000', 'required': 'true'}))

    logradouro = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control', 'required': 'true'}))

    numero_endereco = forms.NumberInput(
        attrs={'class': 'form-control', 'required': 'true'})

    complemento_endereco = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control', 'required':'true'}), label="Complemento")

    estado = forms.Select(
        attrs={'class': 'form-control', 'required': 'true'})

    cidade = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control', 'required': 'true'}))

    email = forms.EmailField(widget=forms.EmailInput(
            attrs={'class': 'form-control', 'required': 'true'}))

    senha = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'required': 'true', 'minlength': '6'}))

    class Meta:
        model = Usuario
        fields = ['nome_completo', 'cpf', 'data_nascimento', 'sexo', 'estado_civil', 'telefone', 'logradouro', 'numero_endereco',
                  'complemento_endereco', 'estado', 'cidade', 'email', 'senha']
