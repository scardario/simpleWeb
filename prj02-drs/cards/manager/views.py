import logging
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

logger = logging.getLogger(__name__)

def indiceManager(request):
	usuarios = User.objects.all()
	return render(request, 'manager/index.html', {
			"usuarios": usuarios,
			"titulo": 'User list'
	})

def login(request):
	return render(request, 'manager/login.html', {
		"titulo": 'Login'
	})

def listaUsuarios(request):
	usuarios = User.objects.all()
	datosUsuario = {}
	for usuario in usuarios:
		datosUsuario[usuario.username] = usuario.get_full_name()
	return JsonResponse(datosUsuario)

def estaUsuario(request, usuario):
	dicc = {
		usuario: True
	}

	try:
		busqueda = User.objects.get(username=usuario)
	except:
		dicc = {
			usuario: False
		}

	return JsonResponse(dicc)
