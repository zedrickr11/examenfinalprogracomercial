from django.shortcuts import render, get_object_or_404, redirect, render_to_response

#librería para manejar el envío de mensajes
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from .forms import GradoForm
from final.models import Profesor, Alumno, Materia, Grado, Pensum

# Create your views here.
def pensum_index(request):
    gra = Grado.objects.all()
    return render(request, 'grado/grado_index.html', {'gr': gra})

def pensum_new(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Cancion.objects.create(nombre=formulario.cleaned_data['nombre'], seccion = formulario.cleaned_data['seccion'])
            for Materia_id in request.POST.getlist('Materia'):
                pensum = Pensum(Materia_id=Materia_id, Grado_id = grado.id)
                participacion.save()
            return redirect('pensum_index')
    else:
        formulario = GradoForm()
    return render(request, 'grado/grado_editar.html', {'formulario': formulario})
