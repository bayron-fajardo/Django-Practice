from django.shortcuts import render, HttpResponse, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login


def home(request):

    return render(request,"home.html")

def viewRegistrarUsuarios(request):

    return render(request,"registrarUsuario.html")

def registrarUsuario(request):

    id = request.POST['txtId']
    nombre = request.POST['txtNombre']
    correo = request.POST['txtCorreo']
    usuario = request.POST['txtUsuario']
    contrasena = request.POST['txtContrasena']
    confirmarContrasena = request.POST['txtContrasenaConfirmacion']
    
    if contrasena == confirmarContrasena:
        usuario = Usuario.objects.create(id=id,nombre=nombre,correo=correo,usuario=usuario,contrasena=contrasena)
        return redirect('/')
    else:
        return HttpResponse("Contraseñas Distintas")

def verificarInicioSesion(request):
    
    if request.method == 'POST':
        usuario = request.POST['txtUsuario']
        contrasena = request.POST['txtContrasena']

        user = authenticate(request, username=usuario,password=contrasena )

        if user is not None:

            login(request, user)
            return redirect('viewRegistrarUsuarios/')
        else:

            return HttpResponse("Usuario o contraseña incorrectos")

    else:
        return HttpResponse(['Solo Metodo POST'])