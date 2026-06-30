import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import django

# Setup django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hanami.settings')
django.setup()

from Proveedores.models import Proveedor

try:
    p = Proveedor(
        nombre="Proveedor de Prueba",
        direccion="Calle Falsa 123",
        nit="123456-7",
        email="test@proveedor.com",
        observaciones="Ninguna",
        estado="1"
    )
    p.save()
    print("SUCCESS: Provider saved successfully with ID:", p.id)
    # Clean up
    p.delete()
    print("SUCCESS: Deleted test provider successfully")
except Exception as e:
    print("ERROR OCCURRED during insert:", str(type(e)), str(e))
