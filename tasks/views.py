from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden
from .models import Task
from .forms import TaskCreationForm, CustomUserCreationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm #nuevo
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

# Vista de inicio (listado de tareas) - Solo accesible para usuarios autenticados
@login_required
def index(request):
    tasks = Task.objects.filter(owner=request.user)  # Filtrar por usuario autenticado
    params = {
        'tasks': tasks,
    }
    return render(request, 'tasks/index.html', params)

# Crear tarea - Solo accesible para usuarios autenticados
@login_required
def create(request):
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = Task(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                owner=request.user  # Asignar tarea al usuario autenticado
            )
            task.save()
            return redirect('tasks:index')
    else:
        form = TaskCreationForm()
    params = {
        'form': form,
    }
    return render(request, 'tasks/create.html', params)

# Detalle de una tarea - Solo accesible si pertenece al usuario autenticado
@login_required
def detail(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.owner != request.user:
        return HttpResponseForbidden("No tienes permiso para ver esta tarea.")
    params = {
        'task': task,
    }
    return render(request, 'tasks/detail.html', params)

# Editar una tarea - Solo accesible si pertenece al usuario autenticado
@login_required
def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.owner != request.user:
        return HttpResponseForbidden("No tienes permiso para editar esta tarea.")
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.content = form.cleaned_data['content']
            task.save()
            return redirect('tasks:detail', task_id)
    else:
        form = TaskCreationForm(initial={
            'title': task.title,
            'content': task.content,
        })
    params = {
        'task': task,
        'form': form,
    }
    return render(request, 'tasks/edit.html', params)

# Eliminar una tarea - Solo accesible si pertenece al usuario autenticado
@login_required
def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.owner != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar esta tarea.")
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:index')
    params = {
        'task': task,
    }
    return render(request, 'tasks/delete.html', params)

# Registro de usuario
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('tasks:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

# Inicio de sesión
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Obtiene el usuario del formulario
            login(request, user)  # Inicia sesión al usuario
            return redirect('tasks:index')  # Redirige al listado de tareas
    else:
        form = AuthenticationForm()  # Si es un GET, muestra el formulario vacío

    return render(request, 'tasks/login.html', {'form': form})  # Especifica la ubicación correcta de la plantilla

@login_required
def account_details(request):
    user = request.user
    age = user.age  # Obtener la edad del usuario directamente del campo 'age'
    
    if request.method == 'POST':
        password_form = PasswordChangeForm(user, request.POST)
        if password_form.is_valid():
            password_form.save()
            messages.success(request, "Contraseña cambiada correctamente.")
            return redirect('tasks:profile')
    else:
        password_form = PasswordChangeForm(user)

    return render(request, 'tasks/account_details.html', {
        'user': user,
        'age': age,
        'password_form': password_form
    })
#nuevo

@login_required
def edit_account(request):
    user = request.user

    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Datos actualizados correctamente.")
            return redirect('tasks:profile')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        user_form = UserChangeForm(instance=user)

    return render(request, 'tasks/edit_account.html', {'user_form': user_form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()  # Guarda la nueva contraseña
            update_session_auth_hash(request, user)  # Mantiene la sesión activa
            messages.success(request, "Tu contraseña se ha cambiado exitosamente.")
            return redirect('tasks:profile')  # Cambia 'tasks:profile' a la vista que desees
        else:
            messages.error(request, "Por favor, corrige los errores.")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'tasks/change_password.html', {'form': form})
@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        # Cerrar la sesión del usuario antes de eliminar su cuenta
        logout(request)
        user.delete()
        messages.success(request, "Tu cuenta ha sido eliminada exitosamente.")
        return redirect('tasks:login')  # Redirige a la página de login

    return render(request, 'tasks/delete_account.html')
# Cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('tasks:login')

