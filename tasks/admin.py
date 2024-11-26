from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task

# Registro del modelo CustomUser en el admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),  # Este es el campo para email y contraseña
        ('Personal info', {'fields': ('first_name', 'last_name')}),  # Información personal
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),  # Permisos
        ('Important dates', {'fields': ('last_login', 'date_joined')}),  # Fechas importantes
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    filter_horizontal = ('groups', 'user_permissions')  # Asegúrate de que 'groups' y 'user_permissions' estén en el modelo si los usas

# Registra el modelo CustomUser con el UserAdmin personalizado
admin.site.register(CustomUser, CustomUserAdmin)

# Registro del modelo Task en el admin
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'owner', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('owner', 'created_at', 'updated_at')  # Puedes agregar más filtros si es necesario

# Registra el modelo Task
admin.site.register(Task, TaskAdmin)
