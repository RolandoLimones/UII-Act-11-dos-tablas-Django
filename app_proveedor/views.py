from django.shortcuts import render, get_object_or_404, redirect
from .models import Proveedor
from .forms import ProveedorForm

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

def detalle_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    return render(request, 'detalle_proveedor.html', {'proveedor': proveedor})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_proveedor:listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'formulario_proveedor.html', {'form': form, 'titulo': 'Crear Proveedor'})

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, request.FILES, instance=proveedor)  
        if form.is_valid():
            form.save()
            return redirect('app_proveedor:detalle_proveedor', proveedor_id=proveedor.id)
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'formulario_proveedor.html', {'form': form, 'titulo': 'Editar Proveedor'})

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('app_proveedor:listar_proveedores')
    return render(request, 'confirmar_borrar.html', {'proveedor': proveedor})