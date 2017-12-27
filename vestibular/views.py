from django.forms import ModelForm
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.hashers import make_password

# Create your views here.



def registrarVestibular(request, template_name="registrar-vestibular.html"):
    form = VestibularForm(request.POST or None)
    if form.is_valid():
        vestibulando = form.save(commit=False)
        vestibulando.save()
        return redirect('vestibular-registrado')
    return render(request, template_name, {'form':form})

def registradoVestibular(request, template_name="registrado-vestibular.html"):
    return render(request, template_name)