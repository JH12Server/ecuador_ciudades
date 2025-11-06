from django.contrib import admin
from .models import Ciudad

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region', 'poblacion')
    search_fields = ('nombre', 'region')
    list_filter = ('region',)
# Register your models here.
