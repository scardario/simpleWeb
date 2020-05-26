import logging
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

logger = logging.getLogger(__name__)

def indiceManager(request):
	usuarios = User.objects.all()
	return render(request, 'manager/index.html', {
			"usuarios": usuarios
	})

def listaUsuarios(request):
	usuarios = User.objects.all()
	datosUsuario = {}
	for usuario in usuarios:
		datosUsuario[usuario.username] = usuario.get_full_name()
	return JsonResponse(datosUsuario)
