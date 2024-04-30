from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login

import os
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def home(request):

    return render(request,"home.html")

def viewRegistrarUsuarios(request):

    return render(request,"registrarUsuario.html")

def viewRecuperarAcceso(request):

    return render(request,"recuperarAcceso.html")

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
    

def recuperarContrasena(request):

    correo = request.POST['txtCorreo']
    confirmarCorreo = request.POST['txtConfirmarCorreo']

    if correo == confirmarCorreo:

        try:
            

            load_dotenv()

            remitente = os.getenv('USER')
            asunto = 'Recuperar Acceso a tu cuenta de Flopyy'

            msg = MIMEMultipart()

            msg['Subject'] = asunto
            msg['From'] = remitente
            msg['To'] = correo
            
            ruta_archivo = os.path.join(settings.BASE_DIR, 'Login', 'templates', 'correoAcceso.html')
            
            with open (ruta_archivo,'r') as archivo:
                html = archivo.read()

            msg.attach(MIMEText(html,'html'))

            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()
            server.login(remitente, os.getenv('PASS'))

            server.sendmail(remitente, correo, msg.as_string())

            server.quit()

            
            return HttpResponse("Correo de recuperación enviado correctamente")

        except Exception as e:
            
            print("Error durante el envío del correo electrónico:", e)
            
            return HttpResponse("Ocurrió un error durante el proceso de recuperación de contraseña")
    else:

        return HttpResponse("Error al ingresar el correo")