from django.shortcuts import render
from .models import *
from .form import ServicioForm

# Create your views here.


def listarServicios(request):
    servicio = Servicio.objects.all()
    contexto = {'servicios': servicio}
    return render(request, 'lista.html', contexto)


def form_view(request):
    data = {
        'form': ServicioForm
    }
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'servicio_form.html', data)
