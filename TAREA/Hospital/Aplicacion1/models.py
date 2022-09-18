from django.db import models

# Create your models here.
class Datos(models.Model):
   codigo=models.CharField(primary_key=True,max_length=6)
   nombre = models.CharField(max_length=50)
   Apellido = models.CharField(max_length=50)
   Nacimiento=models.CharField(max_length=50)
   Enfermedad=models.CharField(max_length=50)
   Tratamiento=models.CharField(max_length=200)
   
   def __str__(self):
      texto ="{0} ({1})"
      return texto.format(self.Apellido,self.codigo)

class Informacion(models.Model):
   codigo=models.CharField(primary_key=True,max_length=6)
   nombre = models.CharField(max_length=50)
   Apellido = models.CharField(max_length=50)
   Especialidad=models.CharField(max_length=50)
   Jornada=models.CharField(max_length=15)
   Telefono=models.CharField(max_length=10)     
   
   def __str__(self):
      texto ="{0} ({1})"
      return texto.format(self.Apellido,self.codigo)