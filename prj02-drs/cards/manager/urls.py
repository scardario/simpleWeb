from django.urls import path

from . import views

urlpatterns = [
    path('', views.indiceManager, name='indiceManager'),
	path('usuarios', views.listaUsuarios, name='listaUsuarios')
]