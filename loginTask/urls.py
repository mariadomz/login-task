from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración

    # Rutas de la aplicación tasks
    path('', include('tasks.urls')),  # Incluir todas las rutas de tasks como rutas principales

    # Rutas de autenticación proporcionadas por Django
    path('accounts/', include('django.contrib.auth.urls')),  # Rutas de login, logout, etc.
]
