from decimal import Decimal
from django.shortcuts import render, redirect
from .models import Product, ProductForm

def home(request):
    data = {
        "title1": "Autor | Alain Machuca",
        "title2": "Super Mercado El Pepe"
    }
    return render(request, 'core/home.html', data)

def product_List(request):
    products = Product.objects.all()  # Obtener todos los productos
    data = {
        "title1": "Productos",
        "title2": "Consulta De Productos",
        "products": products  # Pasar los productos al contexto de la plantilla
    }
    if request.path == '/products/':  # Verificar si estamos en la página de productos
        data['show_add_form'] = True  # Agregar una bandera para mostrar el formulario de agregar producto
    return render(request, "core/products/list.html", data)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirige a la lista de productos después de agregar uno nuevo
    else:
        form = ProductForm()
    return render(request, 'core/products/add_product.html', {'form': form})

def brand_List(request):
    data = {
        "title1": "Marcas",
        "title2": "Consulta De Marcas De Productos"
    }
    return render(request, "core/brands/list.html", data)

def supplier_List(request):
    data = {
        "title1": "Proveedores",
        "title2": "Consulta De proveedores"
    }
    return render(request, "core/suppliers/list.html", data)
