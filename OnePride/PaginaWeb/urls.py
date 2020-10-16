from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarServicios, name='serv'),
    path('registro/', views.form_view, name='reg')
]
