from django.urls import path
from . import views

urlpatterns = [
    path('cms/dashboard', views.dashboardcms, name='dashboardcms'),
    path('cms/crear_pais/', views.crear_pais, name='crear_pais'),
    path('cms/lista_paises/', views.lista_paises, name='lista_paises'),
    path('cms/editar_pais/<int:id>/', views.editar_pais, name='editar_pais'),
    path('cms/eliminar_pais/<int:id>/', views.eliminar_pais, name='eliminar_pais'),
    path('cms/crear_region/', views.crear_region, name='crear_region'),
    path('cms/lista_region/', views.lista_region, name='lista_region'),
    path('cms/editar_region/<int:id>/', views.editar_region, name='editar_region'),
    path('cms/eliminar_region/<int:id>/', views.eliminar_region, name='eliminar_region'),
    path('cms/crear_provincia/', views.crear_provincia, name='crear_provincia'),
    path('cms/lista_provincia/', views.lista_provincia, name='lista_provincia'),
    path('cms/editar_provincia/<int:id>/', views.editar_provincia, name='editar_provincia'),
    path('cms/eliminar_provincia/<int:id>/', views.eliminar_provincia, name='eliminar_provincia'),
    path('cms/crear_comuna/', views.crear_comuna, name='crear_comuna'),
    path('cms/lista_comuna/', views.lista_comunas, name='lista_comuna'),
    path('cms/editar_comuna/<int:id>/', views.editar_comuna, name='editar_comuna'),
    path('cms/eliminar_comuna/<int:id>/', views.eliminar_comuna, name='eliminar_comuna'),
    path('cms/perfil/<str:username>/', views.mostrar_perfil, name='perfil'),
    #path('cms/editar_perfil/<int:id>/', views.editar_perfil, name='editar_perfil'),
]