from django.shortcuts import render, redirect
from productos.models import Producto
import re

# Create your views here.

def validar_nombre_producto(nombre):
    """Valida que el nombre contenga al menos una letra"""
    # Verifica que haya al menos una letra en el nombre
    return bool(re.search(r'[a-zA-ZáéíóúÁÉÍÓÚñÑ]', nombre))

def mostrarIndex(request):
    return render(request,"index.html")

def mostrarListado(request):
    # Obtenemos todos los productos de la base de datos
    productos = Producto.objects.all()
    datos = {'productos': productos}
    return render(request,"listado.html", datos)

def mostrarFormRegistrar(request):
    return render(request,"form_registrar.html")

def mostrarFormActualizar(request, id):
    # Buscamos el producto por ID
    producto = Producto.objects.get(id=id)
    datos = {'producto': producto}
    return render(request,"form_actualizar.html", datos)

def insertarProducto(request):
    if request.method == 'POST':
        # capturamos los datos ingresados en el formulario
        nom=request.POST['txtnom']
        mar=request.POST['cbomar']
        pre=request.POST['txtpre']
        
        # Validamos que el nombre contenga al menos una letra
        if not validar_nombre_producto(nom):
            datos = {'msjErr': 'El nombre del producto debe contener al menos una letra'}
            return render(request,'form_registrar.html',datos)
        
        # creamos un objeto de tipo Producto
        pro=Producto(nombre=nom,marca=mar,precio=pre)
        # grabamos 
        pro.save()
        datos = {'msjOk': 'Producto registrado exitosamente'}
        return render(request,'form_registrar.html',datos)        
    else:
        datos = {'msjErr': 'La solicitud no se puede procesar'}
        return render(request,'form_registrar.html',datos)

def actualizarProducto(request, id):
    if request.method == 'POST':
        # Obtenemos el producto a actualizar
        producto = Producto.objects.get(id=id)
        
        # Capturamos los nuevos datos
        nom = request.POST['txtnom']
        mar = request.POST['cbomar']
        pre = request.POST['txtpre']
        
        # Validamos que el nombre contenga al menos una letra
        if not validar_nombre_producto(nom):
            datos = {
                'producto': producto,
                'msjErr': 'El nombre del producto debe contener al menos una letra'
            }
            return render(request,'form_actualizar.html',datos)
        
        # Actualizamos los datos
        producto.nombre = nom
        producto.marca = mar
        producto.precio = pre
        producto.save()
        
        # Redirigimos al listado
        return redirect('/listado')
    else:
        return redirect('/listado')

def eliminarProducto(request, id):
    # Buscamos el producto por ID
    producto = Producto.objects.get(id=id)
    # Eliminamos el producto
    producto.delete()
    # Redirigimos al listado
    return redirect('/listado')