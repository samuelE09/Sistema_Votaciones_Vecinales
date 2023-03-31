from django.shortcuts import render , redirect, get_object_or_404
from .models import Votaciones

# Create your views here.
def home(request):
    actualizacion()
    return render(request, 'home.html')

def votacion_activa(request):
    votaciones_activas = Votaciones.objects.filter(state = False)
    
    return render(request, 'votaciones_activas.html',{'list_votaciones_activas':votaciones_activas})

def count_votos(request,voto_id):
    if request.method == "GET":
       pass
       #return redirect('votaciones_activas')
    else: 
        if 'voto' in request.POST:
            voto_activo = Votaciones.objects.get(pk=voto_id)
            valor = request.POST.get('voto')
            if valor == "voto_favor":
                voto_activo.count_favor +=1
                voto_activo.save()
                print(voto_activo.count_favor)
            if valor == "voto_null":
                voto_activo.count_null +=1
                voto_activo.save()
                print(voto_activo.count_null)
            if valor == "voto_contra":
                voto_activo.count_contra +=1
                voto_activo.save()
                print(voto_activo.count_contra)
                  
        return redirect('voto_exitoso') 

def voto_exitoso(request): 
    return render(request,'voto_exitoso.html')

def historial_votaciones(request):
    historial_votaciones = actualizacion()
    return render(request, 'historial.html',{'list_votaciones':historial_votaciones})

def about(request):
    return render(request, 'about.html')


def actualizacion():
    lista_votaciones = list(Votaciones.objects.all())
    for valor in lista_votaciones:
        valor.total = valor.count_contra + valor.count_favor + valor.count_null
        valor.save()
    return Votaciones.objects.all()
