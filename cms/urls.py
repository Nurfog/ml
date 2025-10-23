from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.dashboardcms, name='dashboard'),
    path('perfil/<str:username>/', views.mostrar_perfil, name='perfil'),
    path('paises/', views.lista_paises, name='lista_paises'),
    path('paises/crear/', views.crear_pais, name='crear_pais'),
    path('paises/editar/<int:id>/', views.editar_pais, name='editar_pais'),
    path('paises/eliminar/<int:id>/', views.eliminar_pais, name='eliminar_pais'),
    path('perfil/editar/<int:id>/', views.editar_perfil, name='editar_perfil'),
    path('regiones/', views.lista_region, name='lista_region'),
    path('regiones/crear/', views.crear_region, name='crear_region'),
    path('regiones/editar/<int:idreg>/', views.editar_region, name='editar_region'),
    path('regiones/eliminar/<int:idreg>/', views.eliminar_region, name='eliminar_region'),
    path('comunas/', views.lista_comuna, name='lista_comuna'),
    path('comunas/crear/', views.crear_comuna, name='crear_comuna'),
    path('comunas/editar/<int:id>/', views.editar_comuna, name='editar_comuna'),
    path('comunas/eliminar/<int:id>/', views.eliminar_comuna, name='eliminar_comuna'),
]