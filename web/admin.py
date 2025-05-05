from django.contrib import admin
import web.models as models

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion', 'imagen')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('titulo',)
    ordering = ('-id',)
    list_per_page = 10
    list_display_links = ('id', 'titulo')

admin.site.register(models.Slider, SliderAdmin)



