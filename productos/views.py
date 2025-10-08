from django.shortcuts import render
from productos.models import Producto

# Create your views here.

def mostrarIndex(request):
    return render(request,"index.html")

def mostrarListado(request):
    return render(request,"listado.html")

def mostrarFormRegistrar(request):
    return render(request,"form_registrar.html")

def mostrarFormActualizar(request):
    return render(request,"listado.html")

def insertarProducto(request):
    if request.method == 'POST':
        # capturamos los datos ingresados en el formulario
        nom=request.POST['txtnom']
        mar=request.POST['cbomar']
        pre=request.POST['txtpre']
        # creamos un objeto de tipo Producto
        pro=Producto(nombre=nom,marca=mar,precio=pre)
        # grabamos 
        pro.save()
        # save es una función creada dentro del ORM de Django
        # que permite almacenar un registro en la tabla
        datos = {'msjOk': 'Registro grabado exitosamente'}
        return render(request,'form_registrar.html',datos)        
    else:
        # creamos un diccionario
        datos = {'msjErr': 'La solicitud no se puede procesar !!'}
        return render(request,'form_registrar.html',datos)



