from django.contrib import admin
from .models import Empresa, Representante, Pais, Region, Comuna, Colegio, Departamento, Profile



class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'rut', 'razonsocial', 'comuna', 'direccion', 'telefono', 'email', 'logo', 'estado')
    search_fields = ('id', 'rut', 'razonsocial', 'comuna', 'direccion', 'telefono', 'email', 'logo', 'estado')
    list_filter = ('id', 'rut', 'razonsocial', 'comuna', 'direccion', 'telefono', 'email', 'logo', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'razonsocial')
    readonly_fields = ('id',)

admin.site.register(Empresa, EmpresaAdmin)

class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'empresa', 'rut', 'nombre', 'apellido', 'email', 'telefono', 'estado')
    search_fields = ('id', 'empresa', 'rut', 'nombre', 'apellido', 'email', 'telefono', 'estado')
    list_filter = ('id', 'empresa', 'rut', 'nombre', 'apellido', 'email', 'telefono', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'empresa')
    readonly_fields = ('id',)

admin.site.register(Representante, RepresentanteAdmin)

class PaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'estado')
    search_fields = ('id', 'codigo', 'nombre', 'estado')
    list_filter = ('id', 'codigo', 'nombre', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'codigo')
    readonly_fields = ('id',)

admin.site.register(Pais, PaisAdmin)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'estado')
    search_fields = ('id', 'codigo', 'nombre', 'estado')
    list_filter = ('id', 'codigo', 'nombre', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'codigo')
    readonly_fields = ('id',)

admin.site.register(Region, RegionAdmin)

class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'region', 'codigo', 'nombre', 'estado')
    search_fields = ('id', 'region', 'codigo', 'nombre', 'estado')
    list_filter = ('id', 'region', 'codigo', 'nombre', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'region')
    readonly_fields = ('id',)

admin.site.register(Comuna, ComunaAdmin)

class ColegioAdmin(admin.ModelAdmin):
    list_display = ('id', 'razon_social', 'comuna', 'direccion', 'telefono', 'email', 'estado')
    search_fields = ('id', 'razon_social', 'comuna', 'direccion', 'telefono', 'email', 'estado')
    list_filter = ('id', 'razon_social', 'comuna', 'direccion', 'telefono', 'email', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'razon_social')
    readonly_fields = ('id',)

admin.site.register(Colegio, ColegioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'estado')
    search_fields = ('id', 'nombre', 'descripcion', 'estado')
    list_filter = ('id', 'nombre', 'descripcion', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'nombre')
    readonly_fields = ('id',)

admin.site.register(Departamento, DepartamentoAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'about', 'trabajo', 'rut', 'pais', 'comuna',
                     'direccion', 'telefono', 'foto', 'socialx', 'socialfb', 'socialig', 'socialyt', 'socialli','estado')
    search_fields = ('id', 'user', 'about', 'trabajo', 'rut', 'pais', 'comuna',
                     'direccion', 'telefono', 'foto', 'socialx', 'socialfb', 'socialig', 'socialyt', 'socialli','estado')
    list_filter = ('id', 'user', 'about', 'trabajo', 'rut', 'pais', 'comuna',
                     'direccion', 'telefono', 'foto', 'socialx', 'socialfb', 'socialig', 'socialyt', 'socialli','estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'user')
    readonly_fields = ('id',)

admin.site.register(Profile, ProfileAdmin)