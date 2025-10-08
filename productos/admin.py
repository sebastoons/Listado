from django.contrib import admin
from productos.models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'marca', 'precio')
    search_fields = ('nombre', 'marca')
    list_filter = ('marca',)