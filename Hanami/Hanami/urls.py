"""
URL configuration for Hanami project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Productos.views import Produinsertar, Produmostrar, Produeditar, Produeliminar, Produdetalle
from Login.views import home, logint, Registeruse, logoutuser
from Proveedores.views import Proinsertar, Promostrar, Proeditar, Proeliminar
from Clientes.views import Climostrar, Cliinsertar, Clieditar, Clieliminar
from Facturas.views import Facmostrar, Facinsertar, Faceditar, Faceliminar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('User/login', logint),
    path('User/registro', Registeruse),
    path('User/salir', logoutuser),
    path('Proveedor/insertar', Proinsertar),
    path('Proveedor/mostrar', Promostrar),
    path('Proveedor/editar/<str:idpro>', Proeditar),
    path('Proveedor/eliminar/<str:idpro>', Proeliminar),
    path('Proveedor/eliminar', Proeliminar),
    path('Producto/insertar', Produinsertar),
    path('Producto/mostrar', Produmostrar),
    path('Producto/editar/<str:idpro>', Produeditar),
    path('Producto/eliminar', Produeliminar),
    path('Producto/detalle', Produdetalle),
    path('Cliente/insertar', Cliinsertar),
    path('Cliente/mostrar', Climostrar),
    path('Cliente/editar/<str:idcli>', Clieditar),
    path('Cliente/eliminar', Clieliminar),
    path('Factura/insertar', Facinsertar),
    path('Factura/mostrar', Facmostrar),
    path('Factura/editar/<str:idfac>', Faceditar),
    path('Factura/eliminar', Faceliminar),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)