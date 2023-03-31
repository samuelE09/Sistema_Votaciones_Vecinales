"""Sistema_Votacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Emision_Votos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='inicio'),
    path('votacion_activa/', views.votacion_activa, name="votaciones_activas"),
    path('historial/', views.historial_votaciones, name="historial_votaciones"),
    path('votacion/<int:voto_id>', views.count_votos, name="votacion"),
    path('voto_exitoso/', views.voto_exitoso, name="voto_exitoso"),
    path('about/', views.about, name="about"),
    
]
