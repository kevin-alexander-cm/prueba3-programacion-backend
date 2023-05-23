from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from general.models import Usuarios

def inicio(request):
    sesion = None
    try:
        sesion = request.session['sesion_activa']
        if sesion != 'Activa':
            sesion = None
    except:
        sesion = None
        return render(request, 'login.html')
    return render(request, 'index.html')

def login(request):
    return render(request,"login.html")

def iniciar_sesion(request):
    msj = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            usuario = Usuarios.objects.get(username = username, password = password)
        except:
            usuario = None

        if usuario != None:
            request.session["sesion_activa"] = "Activa"
            request.session["perfil"] = usuario.perfil
            return redirect('inicio')
        else:
            msj ='Las credenciales son incorrectas'
            return render(request, 'login.html', {'msj':msj})

def cerrar_sesion(request):
    try:
        if request.session['sesion_activa'] == 'Activa':
            del request.session['sesion_activa']
            del request.session['perfil']
            return render(request,"login.html")
        else:
            return render(request,"iniciar_sesion.html")
    except:
        return render(request,"iniciar_sesion.html")




