from django.shortcuts import render, redirect
from .models import Cliente

def Climostrar(request):
    clientes = Cliente.objects.all()
    return render(request, 'Cliente/mostrar.html', {'mostrar': clientes})

def Cliinsertar(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        celular = request.POST.get('celular')
        email = request.POST.get('email')

        if nombre and apellido:
            cliente = Cliente(
                nombre=nombre,
                apellido=apellido,
                celular=celular,
                email=email
            )
            cliente.save()
            return redirect('/Cliente/mostrar')
        else:
            mensa = 'Señor usuario falta datos obligatorios (Nombre y Apellido)'
            return render(request, 'Cliente/insertar.html', {
                'nombre': nombre, 'apellido': apellido,
                'celular': celular, 'email': email, 'mensa': mensa
            })
    return render(request, 'Cliente/insertar.html')

def Clieditar(request, idcli):
    try:
        cliente = Cliente.objects.get(idcliente=idcli)
    except Cliente.DoesNotExist:
        return redirect('/Cliente/mostrar')

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        celular = request.POST.get('celular')
        email = request.POST.get('email')

        if nombre and apellido:
            cliente.nombre = nombre
            cliente.apellido = apellido
            cliente.celular = celular
            cliente.email = email
            cliente.save()
            return redirect('/Cliente/mostrar')
        else:
            mensa = 'Señor usuario falta datos obligatorios (Nombre y Apellido)'
            return render(request, 'Cliente/editar.html', {
                'cliente': cliente, 'mensa': mensa
            })
    return render(request, 'Cliente/editar.html', {'cliente': cliente})

def Clieliminar(request):
    if request.method == "POST":
        idcli = request.POST.get('idcli')
        try:
            cliente = Cliente.objects.get(idcliente=idcli)
            cliente.delete()
        except Cliente.DoesNotExist:
            pass
    return redirect('/Cliente/mostrar')
