from django.shortcuts import render

# Create your views here.


def listarServicios(request):
    return render(request, 'lista.html')

def form_view(request):
    data ={
        'form':ServicioForm
    }
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request, 'servicio_form.html',data)
