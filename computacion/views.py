from django.shortcuts import render
from . models import InsumosComputacionales
from msilib.schema import Error
# Create your views here.

def inicio_computacion(request):
    return render(request, 'computacion/inicio_computacion.html')


def registrar_computacion(request):
    return render(request, 'computacion/crear_computacion.html')    


def crear_computacion(request):
    msj = None
    nro_insumo = request.POST['nro_insumo']
    name_insumo = request.POST['name_insumo']
    fecha_adquisicion = request.POST['fecha_adquisicion']
    marca = request.POST['marca']
    stock = request.POST['stock']
    description = request.POST['description']
    
    try:
        InsumosComputacionales.objects.create(
                nro_insumo = nro_insumo,
                name_insumo = name_insumo, 
                marca = marca,
                fecha_adquisicion = fecha_adquisicion,
                stock = stock, 
                description = description)
    except Exception as ex:
        if str(ex.__cause__).find('computacion_insumoscomputacionles.nro_insumo') > 0:
            msj = 'Ha ocurrido un problema al registrar el artículo, número de insumos ya a sido ingresado.'

        elif str(ex.__cause__).find('oficina_insumoscomputacionles.name_insumo') > 0:
            msj = 'Ha ocurrido un problema al registrar el artículo, el nombre del articulo no debe estar vacío.'

        elif str(ex.__cause__).find('oficina_insumoscomputacionles.stock') > 0:
            msj = 'Ha ocurrido un problema al registrar el artículo, el stock no debe estar vacío.'

        elif str(ex.__cause__).find('oficina_insumoscomputacionles.marca') > 0:
            msj = 'Ha ocurrido un problema al registrar el artículo, el  campo marca no debe estar vacío.'    

        elif str(ex.__cause__).find('oficina_insumoscomputacionles.fecha_adquisicion') > 0:
            msj = 'Ha ocurrido un problema al registrar el artículo, el campo de ubicación no debe estar vacío'

        elif str(ex.__cause__).find('oficina_insumoscomputacionles.description') > 0:
            msj = 'Ha ocurrido un problema al registrar el artículo, el camop de descripción no debe estar vacío'    

        else:
            msj = 'Ha ocurrido un problema al registrar el articulo.'
        
        msj = 'se ha ingresado el articulo con exito'

    except Error as err:
        msj = f'ha ocurrido un problema en la operación_, {err}'
    
    return render(request,"computacion/respuesta.html",{'msj':msj})


def listar_computacion(request):
    insumos = InsumosComputacionales.objects.all()
    print(insumos)
    return render(request,"computacion/listar_computacion.html", {'insumos':insumos})



def editar_computacion(request, nro_insumo):
    msj = ""
    try:
        insumos = InsumosComputacionales.objects.get(nro_insumo = nro_insumo)
        return render(request, "computacion/actualizar_computacion.html", { "ofi":insumos})
    except:
        insumos = None
    
    if insumos == None:
        try:
            nro_insumo = request.POST["nro_insumo"]
            insumos = InsumosComputacionales.objects.get(nro_insumo = nro_insumo)
        except:
            nro_insumo = None

        if nro_insumo != None:
            
            nro_insumo = request.POST['nro_insumo']
            name_insumo = request.POST['name_insumo']
            fecha_adquisicion = request.POST['fecha_adquisicion']
            marca = request.POST['marca']
            stock = request.POST['stock']
            description = request.POST['description']
            

            insumos.nro_insumo = nro_insumo
            insumos.name_insumo = name_insumo
            fecha_adquisicion = fecha_adquisicion
            insumos.marca = marca
            insumos.stock = stock
            insumos.description = description

            try:
                insumos.save()
                msj = "Se ha actualizado el Articulo"
            except:
                msj = "Se ha ocurrido un error al actualizar el Articulo"

            return render(request, "computacion/respuesta.html", {"msj":msj})
        
        else:
            msj = "No se ha encontrado el Articulo"
            return render(request, "computacion/respuesta.html", {"msj":msj})
    else:
        msj = "No se encontró el Articulo solicitado"
        return render(request, "computacion/respuesta.html", {"msj":msj})

def eliminar_computacion(request, nro_insumo):
    msj = None

    try:
        insumos = InsumosComputacionales.objects.get(nro_insumo = nro_insumo)
        insumos.delete()
        msj = "El Articulo ha sido eliminado exitosamente."

        return render(request, "computacion/respuesta.html",{"msj":msj})

    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'No se ha encontrado un articulo  asociado. Por favor, vuelva a intentarlo.'
        else:
            msj = 'Ha ocurrido un problema al eliminar el articulo.'
        
        return render(request,"computacion/respuesta.html", {"msj":msj})



def buscar_computacion(request):
    return render(request,'computacion/buscar_computacion.html')


def buscar_computacion_dato(request):
    msj = None
    articulo = None
    
    campo_busqueda = request.POST["campo_busqueda"]
    dato_buscado = request.POST["dato_buscado"]

    try:
        if campo_busqueda == 'name_insumo':
            insumos = InsumosComputacionales.objects.filter(name_insumo = dato_buscado)
        elif campo_busqueda == 'nro_insumo':
            insumos = InsumosComputacionales.objects.filter(nro_insumo = dato_buscado)
       
    except Exception as ex:
        msj = 'Ha ocurrido un error al buscar el vehículo, por favor vuelva a intentarlo'

    if insumos == None or len(insumos) == 0:
        msj = "No se han encontrado registros que coincidan con los datos ingresados."
    
    context = {
        'insumoss':insumos,
        'msj':msj
    }

    return render(request,'oficina/buscar_computacion.html', context)




    