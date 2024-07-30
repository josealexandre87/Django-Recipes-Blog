from django.shortcuts import render

# Create your views here.
def home(request): #usar namespaces (pastas) pare evitar conflitos de onde vai vir o arquivo html.
    return render(request, 'recipes/home.html') # tem que criar a pasta 'templates' no app recipes para o Django entender que tem um arquivo .html para renderizar e, também, tem que ser informado em projeto/settings.py a existência do app 'recipes'.