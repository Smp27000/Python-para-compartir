from django.shortcuts import render, redirect
from .models import Factura
from Productos.models import Producto as Productos
from Clientes.models import Cliente

def Facmostrar(request):
    facturas = Factura.objects.all()
    return render(request, 'Factura/mostrar.html', {'mostrar': facturas})

def Facinsertar(request):
    productos = Productos.objects.all()
    clientes = Cliente.objects.all()
    
    if request.method == "POST":
        fecha = request.POST.get('fecha')
        cantidad_str = request.POST.get('cantidad')
        precio_str = request.POST.get('precio')
        prod_id = request.POST.get('producto')
        cli_id = request.POST.get('cliente')

        if fecha and cantidad_str and precio_str and prod_id and cli_id:
            try:
                cantidad = float(cantidad_str)
                precio = float(precio_str)
                total = cantidad * precio
                producto = Productos.objects.get(id=prod_id)
                cliente = Cliente.objects.get(idcliente=cli_id)
                
                factura = Factura(
                    fecha=fecha,
                    cantidad=cantidad,
                    precio=precio,
                    total=total,
                    producto=producto,
                    cliente=cliente
                )
                factura.save()
                return redirect('/Factura/mostrar')
            except Exception as e:
                mensa = f"Error al guardar la factura: {str(e)}"
                return render(request, 'Factura/insertar.html', {
                    'productos': productos, 'clientes': clientes, 'mensa': mensa
                })
        else:
            mensa = 'Todos los campos son obligatorios'
            return render(request, 'Factura/insertar.html', {
                'productos': productos, 'clientes': clientes, 'mensa': mensa
            })
            
    return render(request, 'Factura/insertar.html', {'productos': productos, 'clientes': clientes})

def Faceditar(request, idfac):
    try:
        factura = Factura.objects.get(id=idfac)
    except Factura.DoesNotExist:
        return redirect('/Factura/mostrar')

    productos = Productos.objects.all()
    clientes = Cliente.objects.all()

    if request.method == "POST":
        fecha = request.POST.get('fecha')
        cantidad_str = request.POST.get('cantidad')
        precio_str = request.POST.get('precio')
        prod_id = request.POST.get('producto')
        cli_id = request.POST.get('cliente')

        if fecha and cantidad_str and precio_str and prod_id and cli_id:
            try:
                cantidad = float(cantidad_str)
                precio = float(precio_str)
                factura.fecha = fecha
                factura.cantidad = cantidad
                factura.precio = precio
                factura.total = cantidad * precio
                factura.producto = Productos.objects.get(id=prod_id)
                factura.cliente = Cliente.objects.get(idcliente=cli_id)
                factura.save()
                return redirect('/Factura/mostrar')
            except Exception as e:
                mensa = f"Error al actualizar la factura: {str(e)}"
                return render(request, 'Factura/editar.html', {
                    'factura': factura, 'productos': productos, 'clientes': clientes, 'mensa': mensa
                })
        else:
            mensa = 'Todos los campos son obligatorios'
            return render(request, 'Factura/editar.html', {
                'factura': factura, 'productos': productos, 'clientes': clientes, 'mensa': mensa
            })

    return render(request, 'Factura/editar.html', {
        'factura': factura, 'productos': productos, 'clientes': clientes
    })

def Faceliminar(request):
    if request.method == "POST":
        idfac = request.POST.get('idfac')
        try:
            factura = Factura.objects.get(id=idfac)
            factura.delete()
        except Factura.DoesNotExist:
            pass
    return redirect('/Factura/mostrar')
