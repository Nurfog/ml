from django.contrib import admin
from cms.models import Empresa, Representante, Pais, Region, Comuna, Colegio, Departamento, Profile
import cms.models as models


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'dniempresa', 'razonsocial', 'comuna', 'direccion', 'telefono', 'email', 'logo', 'estado')
    search_fields = ('id', 'dniempresa', 'razonsocial', 'comuna', 'direccion', 'telefono', 'email', 'logo', 'estado')
    list_filter = ('id', 'dniempresa', 'razonsocial', 'comuna', 'direccion', 'telefono', 'email', 'logo', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'razonsocial')
    readonly_fields = ('id',)

admin.site.register(models.Empresa, EmpresaAdmin)

class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'empresa', 'rut', 'nombre', 'apellido', 'email', 'telefono', 'estado')
    search_fields = ('id', 'empresa', 'rut', 'nombre', 'apellido', 'email', 'telefono', 'estado')
    list_filter = ('id', 'empresa', 'rut', 'nombre', 'apellido', 'email', 'telefono', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'empresa')
    readonly_fields = ('id',)

admin.site.register(models.Representante, RepresentanteAdmin)

class paisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'estado')
    search_fields = ('id', 'codigo', 'nombre', 'estado')
    list_filter = ('id', 'codigo', 'nombre', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'codigo')
    readonly_fields = ('id',)

admin.site.register(models.Pais, paisesAdmin)

class regionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'estado')
    search_fields = ('id', 'codigo', 'nombre', 'estado')
    list_filter = ('id', 'codigo', 'nombre', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'codigo')
    readonly_fields = ('id',)

admin.site.register(models.Region, regionesAdmin)

class comunasAdmin(admin.ModelAdmin):
    list_display = ('id', 'region', 'codigo', 'nombre', 'estado')
    search_fields = ('id', 'region', 'codigo', 'nombre', 'estado')
    list_filter = ('id', 'region', 'nombre', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'region')
    readonly_fields = ('id',)

admin.site.register(models.Comuna, comunasAdmin)

class colegiosAdmin(admin.ModelAdmin):
    list_display = ('id', 'razon_social', 'comuna', 'direccion', 'telefono', 'email', 'estado')
    search_fields = ('id', 'razon_social', 'comuna', 'direccion', 'telefono', 'email', 'estado')
    list_filter = ('id', 'razon_social', 'comuna', 'direccion', 'telefono', 'email', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'razon_social')
    readonly_fields = ('id',)

admin.site.register(models.Colegio, colegiosAdmin)

class departamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'estado')
    search_fields = ('id', 'nombre', 'descripcion', 'estado')
    list_filter = ('id', 'nombre', 'descripcion', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'nombre')
    readonly_fields = ('id',)

admin.site.register(models.Departamento, departamentoAdmin)

class profileAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'about', 'trabajo', 'rut', 'id_pais', 'id_comuna',
                     'direccion', 'telefono', 'foto', 'socialx', 'socialfb', 'socialig', 'socialyt', 'socialli','estado')
    search_fields = ('id', 'usuario', 'about', 'trabajo', 'rut', 'id_pais', 'id_comuna',
                     'direccion', 'telefono', 'foto', 'socialx', 'socialfb', 'socialig', 'socialyt', 'socialli','estado')
    list_filter = ('id', 'usuario', 'about', 'trabajo', 'rut', 'id_pais', 'id_comuna',
                     'direccion', 'telefono', 'foto', 'socialx', 'socialfb', 'socialig', 'socialyt', 'socialli','estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'usuario')
    readonly_fields = ('id',)

admin.site.register(models.Profile, profileAdmin)