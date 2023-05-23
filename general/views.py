from django.shortcuts import render
from .models import Usuarios
from msilib.schema import Error

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registrar_usuario(request):
    return render(request, 'general/ingresar_usuario.html')

def ingresar_usuario(request):
    msj = None

    username = request.POST['username'] 
    password = request.POST['password']
    email = request.POST['email']
    nombre = request.POST['nombre']
    perfil = request.POST['perfil']

    try:
        Usuarios.objects.create(
            username = username,
            password = password,
            email = email,
            nombre = nombre, 
            perfil = perfil
        )

        msj = 'El Usuario se ha registrado exitosamente.'
    except Exception as ex:
        if str(ex.__cause__).find('general_usuarios.username') > 0:
            msj = 'Ha ocurrido un problema, usuario ya ingresado'
        elif str(ex.__cause__).find('general_usuarios.email') > 0:
            msj = 'Ha ocurrido un problema en la operación, E-Mail ya ingresado'
        elif str(ex.__cause__).find('general_usuarios.nombre') > 0:
            msj = 'Ha ocurrido un problema en la operación, nombre ya ingresado'    
        else:
            'Ha ocurrido un problema en el ingreso'
    except Error as err:
        msj = f'Ha ocurrido un problema en el ingreso, {err}'

    return render(request,"general/respuesta.html",{'msj':msj})

def actualizar_usuario(request, username = None):
    msj = None

    try:
        usuarios = Usuarios.objects.get(username = username)
        return render(request, 'general/actualizar_usuario.html', {"usu":usuarios})
    except:
        usuarios = None

    if usuarios == None:
        try:
            username = request.POST["username"]
            usuarios = Usuarios.objects.get(username = username)
        except:
            username = None

        if username != None:
            username = request.POST['username'] 
            password = request.POST['password']
            email = request.POST['email']
            nombre = request.POST['nombre']
            perfil = request.POST['perfil']

            usuarios.username = username
            usuarios.password = password
            usuarios.email = email
            usuarios.nombre = nombre
            usuarios.perfil = perfil

            try:
                usuarios.save()
                msj = "Se ha actualizado el usuario"
            except:
                msj = "Ha ocurrido un error al actualizar el usuario"

            return render(request, "general/respuesta.html", {"msj":msj})

        else:
            msj ="No se ha encontrado al usuario"
            return render(request, "general/respuesta.html", {"msj":msj})
    
    else:
        msj = "No se ha encontrado el usuario"
        return render(request, "general/respuesta.html", {"msj":msj})


def eliminar_usuario(request, username):
    msj = None

    try:
        usuarios = Usuarios.objects.get(username = username)
        usuarios.delete()
        msj = "El usuario ha sido eliminado exitosamente"

        return render(request, "general/respuesta.html", {"msj":msj})

    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'No se ha encontrado al usuario'
        else:
            msj = 'Ha ocurrido un problema al eliminar el usuario'

        return render(request, "general/respuesta.html", {"msj":msj})

def listar_usuarios(request):
    usuarios = Usuarios.objects.all()
    print(usuarios)
    return render(request,"general/listar_usuarios.html", {'usuarios':usuarios})
