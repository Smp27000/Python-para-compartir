from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Producto as Productos
from Proveedores.models import Proveedor

def Produinsertar(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        fecha = request.POST.get('fecha')
        foto = request.FILES.get('foto')
        cantidad = request.POST.get('cantidad')
        prover_id = request.POST.get('prover')
        descri = request.POST.get('descri')

        if nombre and precio and fecha and foto and cantidad and prover_id and descri:
            producto = Productos()
            producto.nombre = nombre
            producto.precio = precio
            # Save using FileSystemStorage
            image = FileSystemStorage()
            saved_name = image.save(foto.name, foto)
            producto.foto = saved_name
            
            producto.cantidad = cantidad
            producto.descripcion = descri
            producto.fecha = fecha
            producto.proveedor = Proveedor.objects.get(id=prover_id)
            producto.save()
            return redirect('/Producto/mostrar')
        else:
            mensa = 'Señor usuario falta datos'
            prover = Proveedor.objects.all()
            return render(request, 'Productos/insertarpro.html', {
                'nombre': nombre,
                'precio': precio,
                'fecha': fecha,
                'foto': foto,
                'cantidad': cantidad,
                'descripcion': descri,
                'mensa': mensa,
                'provers': prover
            })
    else:
        prover = Proveedor.objects.all()
        return render(request, 'Productos/insertarpro.html', {'provers': prover})

def Produmostrar(request):
    mostrar = Productos.objects.all()
    return render(request, 'Productos/mostrarpro.html', {'mostrar': mostrar})

def Produeditar(request, idpro):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        fecha = request.POST.get('fecha')
        cantidad = request.POST.get('cantidad')
        prover_id = request.POST.get('prover')
        descri = request.POST.get('descri')

        if nombre and precio and fecha and cantidad and prover_id and descri:
            producto = Productos()
            producto.id = idpro
            producto.nombre = nombre
            producto.precio = precio
            
            try:
                if request.FILES.get('foto'):
                    file = request.FILES['foto']
                    image = FileSystemStorage()
                    old_foto = request.POST.get('fotoan')
                    if old_foto:
                        image.delete(old_foto)
                    saved_name = image.save(file.name, file)
                    producto.foto = saved_name
                else:
                    producto.foto = request.POST.get('fotoan')
            except Exception:
                producto.foto = request.POST.get('fotoan')

            producto.cantidad = cantidad
            producto.descripcion = descri
            producto.fecha = fecha
            producto.proveedor = Proveedor.objects.get(id=prover_id)
            producto.save()
            return redirect('/Producto/mostrar')
    else:
        prover = Proveedor.objects.all()
        produc = Productos.objects.filter(id=idpro)
        return render(request, 'Productos/editarpro.html', {'producs': produc, 'prover': prover})

def Produeliminar(request):
    if request.method == "POST":
        idprover = request.POST.get('idprover')
        foto = request.POST.get('foto')
        try:
            producto = Productos.objects.get(id=idprover)
            producto.delete()
            if foto:
                eliminafoto = FileSystemStorage()
                eliminafoto.delete(foto)
        except Productos.DoesNotExist:
            pass
    return redirect('/Producto/mostrar')

@csrf_exempt
def Produdetalle(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idpro = data.get('idpro')
            p = Productos.objects.get(id=idpro)
            response_data = [{
                'fields': {
                    'nombre': p.nombre,
                    'descripcion': p.descripcion,
                    'precio': p.precio,
                    'cantidad': p.cantidad,
                    'foto': p.foto,
                    'fecha': p.fecha,
                    'nombreprover': p.proveedor.nombre
                }
            }]
            return JsonResponse(response_data, safe=False)
        except Exception:
            return JsonResponse([], safe=False)
    return JsonResponse([], safe=False)
