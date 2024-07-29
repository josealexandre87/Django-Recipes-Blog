from django.shortcuts import render
from django.http import HttpResponse # para receber o que está nas views como resposta do servidor.

# Create your views here.
def home(request): #usar namespaces (pastas) pare evitar conflitos de onde vai vir o arquivo html.
    return render(request, 'recipes/home.html') # tem que criar a pasta 'templates' no app recipes para o Django entender que tem um arquivo .html para renderizar e, também, tem que ser informado em projeto/settings.py a existência do app 'recipes'.

def contato(request):
    return render(request, 'recipes/contato.html')

def sobre(request):
    return HttpResponse('SOBRE')