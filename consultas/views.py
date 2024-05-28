from django.contrib.auth.decorators import login_required
import BancoDeLosAlpes.auth0backend 
from django.shortcuts import render
import __main__

@login_required
def getConsulta(request):
    context = {
        'Nombre' : 'Usuario Prueba', 'Estado': 'En Revisión'
    }
    return render(request, 'Consulta/consultas.html', context)
