#Este arquivo foi criado no app recipes. ELe não existia.
#Ele permitiu mover as urls que estavam no arquivo projeto/urls.py para cá.
#E todas essas URLs estão sendo importadas a partir daqui lá para a pasta de entrada projeto/urls.py usando `path('', include('recipes.urls'))`, da lista de urlpatterns[].

from django.urls import path
from recipes.views import home, contato, sobre # importa do app recipes funções que renderizam as páginas

urlpatterns = [
    path('', home), # importa de recipes/views a função home e o que retorna dela.
    path('contato/', contato), # importa de recipes/views a função contatoe o que retorna dela
    path('sobre/', sobre), # importa de recipes/views a função sobre e o que retorna dela.
]