""" User admin clases"""
#django
from django.contrib import admin

#models
from users.models import Profile

# Register your models here.
#admin.site.register(Profile)
#https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    #sirve para mostrar en el listado mas campos con informacion
    list_display = ('pk','user','phone_number', 'website','picture') 
    #hace un link con los datos del listado y el detalle 
    list_display_links = ('pk','user')
    #permite realizar edicion de la informacion directamente en la lista 
    list_editable = ('phone_number', 'website','picture')
    #permite habilitar el campo de busqueda 
    search_fields = ('user__username','user__email','user__first_name','user__last_name','phone_number'  )
    #permite mostrar filtros para el listado 
    list_filter = ('created','modified','user__is_active','user__is_staff')
