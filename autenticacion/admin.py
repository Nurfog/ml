from django.contrib import admin
from autenticacion.models import Profile



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

admin.site.register(Profile, profileAdmin)
