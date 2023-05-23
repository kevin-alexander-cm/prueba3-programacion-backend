from django.shortcuts import render, redirect
from . models import InsumosOficina
from msilib.schema import Error


def inicio_oficina(request):
    return render(request, 'oficina/inicio_oficina.html')


def registrar_oficina(request):
    return render(request, 'oficina/crear_oficina.html')


# Create your views here.
def crear_oficina(request):
    msj = None
    nro_article = request.POST['nro_article']
    name_article = request.POST['name_article']
    location = request.POST['location']
    stock = request.POST['stock']
    description = request.POST['description']
    
    try:
        InsumosOficina.objects.create(
                nro_article = nro_article,
                name_article = name_article, 
                location = location,
                stock = stock, 
                description = description)
    except Exception as ex:
        if str(ex.__cause__).find('oficina_insumosoficina.nro_article') > 0:
            msj = 'Ha ocurrido un problema al registrar el artículo, número de articulo ya a sido ingresado.'

        elif str(ex.__cause__).find('oficina_insumosoficina.name_article') > 0:
            msj = 'Ha ocurrido un problema al registrar el artículo, el nombre del articulo no debe estar vacío.'

        elif str(ex.__cause__).find('oficina_insumosoficina.stock') > 0:
            msj = 'Ha ocurrido un problema al registrar el artículo, el stock no debe estar vacío.'

        elif str(ex.__cause__).find('oficina_insumosoficina.location') > 0:
            msj = 'Ha ocurrido un problema al registrar el artículo, el campo de ubicación no debe estar vacío'

        elif str(ex.__cause__).find('oficina_insumosoficina.description') > 0:
            msj = 'Ha ocurrido un problema al registrar el artículo, el camop de descripción no debe estar vacío'    

        else:
            msj = 'Ha ocurrido un problema al registrar el vehículo.'
        
        msj = 'se ha ingresado el articulo con exito'

    except Error as err:
        msj = f'ha ocurrido un problema en la operación_, {err}'
    
    return render(request,"oficina/respuesta.html",{'msj':msj})
   

def listar_oficina(request):
    articulos = InsumosOficina.objects.all()
    print(articulos)
    return render(request,"oficina/listar_oficina.html", {'articulos':articulos})


def editar_oficina(request, nro_article):
    msj = ""
    try:
        articulos = InsumosOficina.objects.get(nro_article = nro_article)
        return render(request, "oficina/actualizar_oficina.html", { "ofi":articulos})
    except:
        articulos = None
    
    if articulos == None:
        try:
            nro_article = request.POST["nro_article"]
            articulos = InsumosOficina.objects.get(nro_article = nro_article)
        except:
            nro_article = None

        if nro_article != None:
            
            nro_article = request.POST['nro_article']
            name_article = request.POST['name_article']
            location = request.POST['location']
            stock = request.POST['stock']
            description = request.POST['description']
            

            articulos.nro_article = nro_article
            articulos.name_article = name_article
            articulos.location = location
            articulos.stock = stock
            articulos.description = description

            try:
                articulos.save()
                msj = "Se ha actualizado el Articulo"
            except:
                msj = "Se ha ocurrido un error al actualizar el Articulo"

            return render(request, "oficina/respuesta.html", {"msj":msj})
        
        else:
            msj = "No se ha encontrado el Articulo"
            return render(request, "oficina/respuesta.html", {"msj":msj})
    else:
        msj = "No se encontró el Articulo solicitado"
        return render(request, "oficina/respuesta.html", {"msj":msj})    



def eliminar_oficina(request, nro_article):
    msj = None

    try:
        articulos = InsumosOficina.objects.get(nro_article = nro_article)
        articulos.delete()
        msj = "El Articulo ha sido eliminado exitosamente."

        return render(request, "oficina/respuesta.html",{"msj":msj})

    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'No se ha encontrado un articulo  asociado. Por favor, vuelva a intentarlo.'
        else:
            msj = 'Ha ocurrido un problema al eliminar el articulo.'
        
        return render(request,"oficina/respuesta.html", {"msj":msj})



def buscar_oficina(request):
    return render(request,'oficina/buscar_oficina.html')


def buscar_oficina_dato(request):
    msj = None
    articulo = None
    
    campo_busqueda = request.POST["campo_busqueda"]
    dato_buscado = request.POST["dato_buscado"]

    try:
        if campo_busqueda == 'nro_article':
            articulo = InsumosOficina.objects.filter(nro_article = dato_buscado)
        elif campo_busqueda == 'name_article':
            articulo = InsumosOficina.objects.filter(name_article = dato_buscado)
        elif campo_busqueda == 'location':
            articulo = InsumosOficina.objects.filter(location = dato_buscado)
    except Exception as ex:
        msj = 'Ha ocurrido un error al buscar el vehículo, por favor vuelva a intentarlo'

    if articulo == None or len(articulo) == 0:
        msj = "No se han encontrado registros que coincidan con los datos ingresados."
    
    context = {
        'articulos':articulo,
        'msj':msj
    }

    return render(request,'oficina/buscar_oficina.html', context)