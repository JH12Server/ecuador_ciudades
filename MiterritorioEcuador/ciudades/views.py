from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Ciudad
from .forms import CiudadForm

# LISTAR
def ciudad_list(request):
    ciudades = Ciudad.objects.all().order_by('nombre')
    return render(request, 'ciudades/ciudad_list.html', {'ciudades': ciudades})

# DETALLE
def ciudad_detail(request, pk):
    ciudad = get_object_or_404(Ciudad, pk=pk)
    return render(request, 'ciudades/ciudad_detail.html', {'ciudad': ciudad})

# CREAR
def ciudad_create(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ciudad creada exitosamente.')
            return redirect('ciudad_list')
    else:
        form = CiudadForm()
    return render(request, 'ciudades/ciudad_form.html', {'form': form, 'title': 'Crear Ciudad'})

# ACTUALIZAR
def ciudad_update(request, pk):
    ciudad = get_object_or_404(Ciudad, pk=pk)
    if request.method == 'POST':
        form = CiudadForm(request.POST, instance=ciudad)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ciudad actualizada.')
            return redirect('ciudad_list')
    else:
        form = CiudadForm(instance=ciudad)
    return render(request, 'ciudades/ciudad_form.html', {'form': form, 'title': 'Editar Ciudad'})

# ELIMINAR
def ciudad_delete(request, pk):
    ciudad = get_object_or_404(Ciudad, pk=pk)
    if request.method == 'POST':
        ciudad.delete()
        messages.success(request, 'Ciudad eliminada.')
        return redirect('ciudad_list')
    return render(request, 'ciudades/ciudad_confirm_delete.html', {'ciudad': ciudad})

# Create your views here.
