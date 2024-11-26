from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Formulario para creación de tareas (ya existente)
class TaskCreationForm(forms.Form):
    title = forms.CharField(label='Título', max_length=255)
    content = forms.CharField(label='Contenido', widget=forms.Textarea())

# Formulario para registro de usuario
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')  # Campos del modelo personalizado

# Formulario para inicio de sesión
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')  # Autenticación usando email y contraseña
