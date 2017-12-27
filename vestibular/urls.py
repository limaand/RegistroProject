from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^registrar-vestibular/', registrarVestibular, name='registrar-vestibular'),
    url(r'^registrado-vestibular/', registradoVestibular, name='vestibular-registrado'),

]