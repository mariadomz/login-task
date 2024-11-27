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
    #path('profile/', views.account_details, name='profile'),  # Ruta para los detalles de la cuenta
    path('edit_account/', views.edit_account, name='edit_account'),
    path('change_password/', views.change_password, name='change_password'),  # Cambiar contraseña
    path('account_details/', views.account_details, name='account_details'),  # Página de detalles de la cuenta
    path('delete_account/', views.delete_account, name='delete_account'),  # Página de eliminación de cuenta
]


