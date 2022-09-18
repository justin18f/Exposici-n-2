from django.shortcuts import render, redirect
from .models import Datos
from .models import Informacion
# Create your views here.
def home(request):
    return render(request, "entrada.html")

def Inicio(request):
    Lista=Informacion.objects.all()
    return render(request, "Inicio.html", {"Informacion":Lista})

def Info(request):
    return render(request, "Informacion.html")

def login(request):
    return render(request, "login.html")

def Gestion(request):
    return render(request, "Gestion.html")

def Registro(request):
    Listado= Datos.objects.all()
    return render(request, "gestionDatos.html", {"Datos":Listado})

def registrarDatos(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    Apellido=request.POST['txtApellido']
    Nacimiento=request.POST['txtNacimiento']
    Enfermedad=request.POST['txtEnfermedad']
    Tratamiento=request.POST['txtTratamiento']
    
    datos = Datos.objects.create(codigo=codigo, nombre=nombre, Apellido=Apellido,Nacimiento=Nacimiento, Enfermedad=Enfermedad, Tratamiento=Tratamiento)
    
    return redirect("/Gestion.html/gestionDatos/")

def edicionDatos(request, codigo):
     datos=Datos.objects.get(codigo=codigo)
     return render(request,"edicionDatos.html", {"Datos":datos})
 
def editarDatos(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    Apellido=request.POST['txtApellido']
    Nacimiento=request.POST['txtNacimiento']
    Enfermedad=request.POST['txtEnfermedad']
    Tratamiento=request.POST['txtTratamiento']

    datos=Datos.objects.get(codigo=codigo)
    datos.nombre= nombre
    datos.Apellido= Apellido
    datos.Nacimiento= Nacimiento
    datos.Enfermedad=Enfermedad
    datos.Tratamiento=Tratamiento
    datos.save()
    return redirect("/Gestion.html/gestionDatos/")

def eliminarDatos(request,codigo):
    datos=Datos.objects.get(codigo=codigo)
    datos.delete()
    return redirect("/Gestion.html/gestionDatos/")

def Regis(request):
    Lista=Informacion.objects.all()
    return render(request,"gestioninfo.html", {"Informacion":Lista})

def registrarinfo(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    Apellido=request.POST['txtApellido']
    Especialidad=request.POST['txtEspecialidad']
    Jornada=request.POST['txtJornada']
    Telefono=request.POST['txtTelefono']
    
    informacion = Informacion.objects.create(codigo=codigo, nombre=nombre, Apellido=Apellido,Especialidad=Especialidad, Jornada=Jornada, Telefono=Telefono)
    
    return redirect("/Gestion.html/gestioninfo/")

def edicioninfo(request, codigo):
     informacion=Informacion.objects.get(codigo=codigo)
     return render(request,"edicioninfo.html", {"Informacion":informacion})
 
def editarinfo(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    Apellido=request.POST['txtApellido']
    Especialidad=request.POST['txtEspecialidad']
    Jornada=request.POST['txtJornada']
    Telefono=request.POST['txtTelefono']

    informacion=Informacion.objects.get(codigo=codigo)
    informacion.nombre= nombre
    informacion.Apellido= Apellido
    informacion.Especialidad= Especialidad
    informacion.Jornada=Jornada
    informacion.Telefono=Telefono
    informacion.save()
    return redirect("/Gestion.html/gestioninfo/")

def eliminarinfo(request,codigo):
    informacion=Informacion.objects.get(codigo=codigo)
    informacion.delete()
    return redirect("/Gestion.html/gestioninfo/")