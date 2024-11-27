from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(BaseUserAdmin):
    # Formulario para agregar usuarios
    add_form = CustomUserCreationForm

    # Campos que se mostrarán en la vista de detalles del usuario
    list_display = ('username', 'email', 'age', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)
    search_fields = ('username', 'email')

    # Configuración de los campos que aparecen en los formularios de edición y creación
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'age')}),
        ('Permisos', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'age', 'is_staff', 'is_active'),
        }),
    )

    # Especifica el modelo que usa este admin
    model = CustomUser

# Registrar el modelo y su administrador
admin.site.register(CustomUser, CustomUserAdmin)
# Configuración para el modelo Task
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'owner', 'created_at', 'updated_at')  # Campos para mostrar
    search_fields = ('title', 'content')  # Campos de búsqueda
    list_filter = ('owner', 'created_at', 'updated_at')  # Filtros en el panel de admin

# Registrar el modelo Task
admin.site.register(Task, TaskAdmin)
