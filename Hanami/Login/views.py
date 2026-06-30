from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from Proveedores.models import Proveedor  

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import connection

# Sin importar Proveedor aquí

def home(request):
    if request.user.is_authenticated:
        return render(request, 'Proveedor/home.html')
    else:
        return redirect('/User/login')

def logint(request):
    if request.method == "POST":
        if request.POST.get('usu') and request.POST.get('pass'):
            user = authenticate(
                username=request.POST.get('usu'),
                password=request.POST.get('pass')
            )
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                mensajeerror = "Usuario o contraseña incorrecta, intente de nuevo"
                return render(request, 'Usuarios/login.html',
                              {'mensajeerror': mensajeerror})
    return render(request, 'Usuarios/login.html')

def Registeruse(request):
    if request.method == "POST":
        if (request.POST.get('user') and request.POST.get('nombre')
                and request.POST.get('apellido') and request.POST.get('email')
                and request.POST.get('pass')):
            Usuario = User.objects.create_user(
                request.POST.get('user'),
                request.POST.get('email'),
                request.POST.get('pass')
            )
            Usuario.first_name = request.POST.get('nombre')
            Usuario.last_name = request.POST.get('apellido')
            Usuario.save()
            return redirect('/User/login')

def logoutuser(request):
    logout(request)
    return redirect('/User/login')