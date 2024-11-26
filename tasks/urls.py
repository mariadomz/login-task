from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    # Rutas para tareas
    path('', views.index, name='index'),  # Página principal (listado de tareas)
    path('create/', views.create, name='create'),  # Crear tarea
    path('detail/<int:task_id>/', views.detail, name='detail'),  # Detalle de tarea
    path('edit/<int:task_id>/', views.edit, name='edit'),  # Editar tarea
    path('delete/<int:task_id>/', views.delete, name='delete'),  # Eliminar tarea

    # Rutas para autenticación
    path('register/', views.register, name='register'),  # Registro de usuario
    path('login/', views.login_view, name='login'),  # Inicio de sesión
    path('logout/', views.logout_view, name='logout'),  # Cerrar sesión
]
