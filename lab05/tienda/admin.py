from django.contrib import admin
from .models import Categoria, Producto, Cliente, Inscripcion

def marcar_agotados(modeladmin, request, queryset):
    queryset.update(stock=0)

marcar_agotados.short_description = "Marcar como Agotados" 

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'estado'] 

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)  
admin.site.register(Cliente)
admin.site.register(Inscripcion)


