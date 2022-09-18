from django.urls import path
from .import views
urlpatterns=[path('',views.home),
             path('Inicio.html',views.Inicio),
             path('Informacion.html',views.Info),
             path('login.html',views.login),
             path('Gestion.html/', views.Gestion),
             path('Gestion.html/gestionDatos/',views.Registro),
             path('gestionDatos/', views.Registro),
             path('registrarDatos/',views.registrarDatos),
             path('Gestion.html/gestionDatos/edicionDatos/<codigo>', views.edicionDatos),
             path('editarDatos/',views.editarDatos),
             path('Gestion.html/gestionDatos/eliminarDatos/<codigo>', views.eliminarDatos),
             path('Gestion.html/gestioninfo/', views.Regis),
             path('gestioninfo/',views.Regis),
             path('registrarinfo/',views.registrarinfo),
             path('Gestion.html/gestioninfo/edicioninfo/<codigo>', views.edicioninfo),
             path('editarinfo/',views.editarinfo),
             path('Gestion.html/gestioninfo/eliminarinfo/<codigo>', views.eliminarinfo)]