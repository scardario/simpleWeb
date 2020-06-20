from django.urls import path

from . import views

urlpatterns = [
    path('', views.indiceManager, name='indiceManager'),
	path('login', views.login, name='login'),
	path('usuarios', views.listaUsuarios, name='listaUsuarios'),
	path('usuarios/<str:usuario>', views.estaUsuario, name='estaUsuario'),
]