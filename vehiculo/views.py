from django.shortcuts import render, redirect
from .models import Vehiculo
from msilib.schema import Error
from datetime import datetime
from datetime import timedelta

# Create your views here.
def inicio_vehiculo(request):
    return render(request, 'vehiculo/inicio_vehiculo.html')

def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, "vehiculo/listar_vehiculos.html", {'vehiculos':vehiculos})

def registrar_vehiculo(request):
    return render(request, 'vehiculo/crear_vehiculo.html')

def crear_vehiculo(request):
    msj = None

    patente = None if len(request.POST['patente'].strip()) == 0 else request.POST['patente'] 
    numero_chasis = request.POST['numero_chasis']
    marca = None if len(request.POST['marca'].strip()) == 0 else request.POST['marca']
    modelo = None if len(request.POST['modelo'].strip()) == 0 else request.POST['modelo']
    ultima_revision = None if len(request.POST['ultima_revision'].strip()) == 0 else request.POST['ultima_revision']
    proxima_revision = None if len(request.POST['proxima_revision'].strip()) == 0 else request.POST['proxima_revision']
    observaciones = request.POST['observaciones']

    try:
        Vehiculo .objects.create(
            patente = patente,
            numero_chasis = numero_chasis,
            marca = marca,
            modelo = modelo, 
            ultima_revision = ultima_revision,
            proxima_revision = proxima_revision,
            observaciones = observaciones
        )

        msj = 'El vehiculo se ha registrado exitosamente.'

    except Exception as ex:
        if str(ex.__cause__).find('vehiculo_vehiculo.patente') > 0:
            msj = 'Ha ocurrido un problema al registrar el vehículo, la patente ya fue ingresado o no es válida.'

        elif str(ex.__cause__).find('vehiculo_vehiculo.numero_chasis') > 0:
            msj = 'Ha ocurrido un problema al registrar el vehículo, el número de chasis ya fue ingresado o no es válido.'

        elif str(ex.__cause__).find('vehiculo_vehiculo.marca') > 0:
            msj = 'Ha ocurrido un problema al registrar el vehículo, la marca no puede estar vacía'

        elif str(ex.__cause__).find('vehiculo_vehiculo.modelo') > 0:
            msj = 'Ha ocurrido un problema al registrar el vehículo, el modelo no puede estar vacío'

        elif str(ex.__cause__).find('vehiculo_vehiculo.ultima_revision') > 0:
            msj = 'Ha ocurrido un problema al registrar el vehículo, la fecha de última revisión no es válida.'
        
        elif str(ex.__cause__).find('vehiculo_vehiculo.proxima_revision') > 0:
            msj = 'Ha ocurrido un problema al registrar el vehículo, la fecha de próxima revisión no es válida.'

        else:
            msj = 'Ha ocurrido un problema al registrar el vehículo.'
    except Error as err:
        msj = f'Ha ocurrido un problema al registrar el certificado'

    context = {
        'msj':msj, 
    }

    return render(request,"vehiculo/respuesta.html", context)  

def editar_vehiculo(request, patente = None):
    msj = None 

    try:
        vehiculo = Vehiculo.objects.get(patente = patente)
        vehiculo.ultima_revision = vehiculo.ultima_revision.strftime('%Y-%m-%d')
        vehiculo.proxima_revision = vehiculo.proxima_revision.strftime('%Y-%m-%d')
        return render(request, "vehiculo/actualizar_vehiculo.html", {"vhcl":vehiculo})
    except:
        vehiculo = None

    if vehiculo == None:

        try:
            patente = request.POST["patente"]
            vehiculo = Vehiculo.objects.get(patente = patente)
        except:
            patente = None

        if patente != None:

            numero_chasis = request.POST["numero_chasis"]
            marca = request.POST["marca"]
            modelo = request.POST["modelo"]
            ultima_revision = request.POST["ultima_revision"]
            proxima_revision = request.POST["proxima_revision"]
            observaciones = request.POST["observaciones"]

            vehiculo.numero_chasis = numero_chasis
            vehiculo.marca = marca
            vehiculo.modelo = modelo
            vehiculo.ultima_revision = ultima_revision
            vehiculo.proxima_revision = proxima_revision
            vehiculo.observaciones = observaciones

            try:
                vehiculo.save()
                msj = "El vehículo ha sido actualizado exitosamente."
            except:
                msj = "Ha ocurrido un problema al actualizar el vehículo."

            return render(request, "vehiculo/respuesta.html", {"msj":msj})
        
        else:
            msj = "La patente ingresada no existe. Por favor, ingrese una patente válida."
            return render(request, "vehiculo/respuesta.html", {"msj":msj})

def eliminar_vehiculo(request, patente):
    msj = None

    try:
        vehiculo = Vehiculo.objects.get(patente = patente)
        vehiculo.delete()
        msj = "El vehículo ha sido eliminado exitosamente."

        return render(request, "vehiculo/respuesta.html",{"msj":msj})

    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'No se ha encontrado un vehículo asociado. Por favor, vuelva a intentarlo.'
        else:
            msj = 'Ha ocurrido un problema al eliminar el certificado.'
        
        return render(request,"vehiculo/respuesta.html", {"msj":msj})

def buscar_vehiculo(request):
    return render(request, 'vehiculo/buscar_vehiculo.html')


def buscar_vehiculo_dato(request) :
    msj = None
    vehiculos = None
    
    campo_busqueda = request.POST["campo_busqueda"]
    dato_buscado = request.POST["dato_buscado"]

    try:
        if campo_busqueda == 'patente':
            vehiculos = Vehiculo.objects.filter(patente = dato_buscado)
        elif campo_busqueda == 'numero_chasis':
            vehiculos = Vehiculo.objects.filter(numero_chasis = dato_buscado)
        elif campo_busqueda == 'modelo':
            vehiculos = Vehiculo.objects.filter(modelo = dato_buscado)
        elif campo_busqueda == 'marca':
            vehiculos = Vehiculo.objects.filter(marca = dato_buscado)
    except Exception as ex:
        msj = 'Ha ocurrido un error al buscar el vehículo, por favor vuelva a intentarlo'

    if vehiculos == None or len(vehiculos) == 0:
        msj = "No se han encontrado registros que coincidan con los datos ingresados."
    
    context = {
        'vehiculos':vehiculos,
        'msj':msj
    }

    return render(request, 'vehiculo/buscar_vehiculo.html', context)

def buscar_vehiculo_fecha(request):
    msj = None
    vehiculos = None
    fecha_actual = datetime.now()
    fecha_futura= fecha_actual + timedelta(days=31)
    fecha_actual = fecha_actual.strftime("%Y-%m-%d")
    fecha_futura = fecha_futura.strftime("%Y-%m-%d")

    try:
        campo_busqueda = request.POST["revision_vencer"]
    except:
        msj = 'Ha ocurrido un error al buscar el certificado, por favor vuelva a intentarlo'

    try:
        if campo_busqueda == 'mes':
            vehiculos = Vehiculo.objects.filter(proxima_revision__lte = fecha_futura)
        elif campo_busqueda == 'vencida':
            vehiculos = Vehiculo.objects.filter(proxima_revision__lte = fecha_actual)
    except Exception as ex:
        msj = 'Ha ocurrido un error al buscar el vehículo, por favor vuelva a intentarlo'

    if vehiculos == None:
        msj = "No se han encontrado registros que coincidan con los datos ingresados."
    
    context = {
        'vehiculos':vehiculos,
        'msj':msj
    }

    return render(request, 'vehiculo/buscar_vehiculo.html', context)