from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('viewRegistrarUsuarios/', views.viewRegistrarUsuarios),
    path('registrarUsuario/', views.registrarUsuario),
    path('verificarIniciarSesion/', views.verificarInicioSesion),
]
