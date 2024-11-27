from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Formulario para creación de tareas
class TaskCreationForm(forms.Form):
    title = forms.CharField(
        label='Título', 
        max_length=255, 
        widget=forms.TextInput(attrs={'placeholder': 'Título de la tarea'})
    )
    content = forms.CharField(
        label='Contenido', 
        widget=forms.Textarea(attrs={'placeholder': 'Contenido de la tarea'})
    )

# Formulario para registro de usuario
class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField(
        required=True, 
        min_value=18, 
        max_value=120, 
        label="Edad", 
        widget=forms.NumberInput(attrs={'placeholder': 'Ingresa tu edad'})
    )
    username = forms.CharField(
        required=True, 
        max_length=150, 
        label="Nombre de usuario", 
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre de usuario'})
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age','password1', 'password2')  # Campos del modelo personalizado

# Formulario para inicio de sesión
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        required=True,
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'placeholder': 'Ingresa tu correo electrónico'})
    )


