from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# esto escribio el profe -inicia
def saludar (request):
    saludo = "hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html
# esto escribio el profe -fin