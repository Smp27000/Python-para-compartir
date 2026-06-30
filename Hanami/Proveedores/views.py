from django.shortcuts import render, redirect
from .models import Proveedor

def Proinsertar(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        nit = request.POST.get('nit', '')
        email = request.POST.get('email', '')
        observaciones = request.POST.get('observaciones', '')
        
        if nombre and direccion:
            proveedor = Proveedor(
                nombre=nombre,
                direccion=direccion,
                nit=nit,
                email=email,
                observaciones=observaciones,
                estado='1' # Activo por defecto
            )
            proveedor.save()
            return redirect('/Proveedor/mostrar')
        else:
            mensa = 'Señor usuario falta datos obligatorios (Nombre y Dirección)'
            return render(request, 'Proveedor/insertar.html', {
                'nombre': nombre, 'direccion': direccion,
                'nit': nit, 'email': email,
                'observaciones': observaciones, 'mensa': mensa
            })
    else:
        return render(request, 'Proveedor/insertar.html')

def Promostrar(request):
    # Retorna tuplas con el orden exacto esperado por el template html:
    # 0: id, 1: nombre, 2: direccion, 3: nit, 4: email, 5: observaciones, 6: estado
    mostrar = Proveedor.objects.values_list('id', 'nombre', 'direccion', 'nit', 'email', 'observaciones', 'estado')
    return render(request, 'Proveedor/mostrar.html', {'mostrar': mostrar})

def Proeditar(request, idpro):
    try:
        p = Proveedor.objects.get(id=idpro)
    except Proveedor.DoesNotExist:
        return redirect('/Proveedor/mostrar')

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        nit = request.POST.get('nit', '')
        email = request.POST.get('email', '')
        observaciones = request.POST.get('observaciones', '')
        
        if nombre and direccion:
            p.nombre = nombre
            p.direccion = direccion
            p.nit = nit
            p.email = email
            p.observaciones = observaciones
            p.save()
            return redirect('/Proveedor/mostrar')
    else:
        # Formatear como tupla para mantener compatibilidad con prover.1, prover.2, etc. en el template
        proveedor = (p.id, p.nombre, p.direccion, p.nit, p.email, p.observaciones, p.estado)
        return render(request, 'Proveedor/editarspro.html', {'prover': proveedor})

def Proeliminar(request):
    idpro = request.POST.get('idprover')
    try:
        proveedor = Proveedor.objects.get(id=idpro)
        proveedor.delete()
    except Proveedor.DoesNotExist:
        pass
    return redirect('/Proveedor/mostrar')