from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.utils import timezone
# Administrador personalizado para el modelo de usuario
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, age=None, **extra_fields):
        """
        Crea y devuelve un usuario con un email, una contraseña y una edad.
        """
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, age=age, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, age=None, **extra_fields):
        """
        Crea y devuelve un superusuario con un email, una contraseña y una edad.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email, password, age, **extra_fields)

# Modelo de usuario personalizado
class CustomUser(AbstractBaseUser, PermissionsMixin):  # Agrega PermissionsMixin aquí
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True, blank=True)  # Campo de edad
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Esto indica si el usuario es administrador

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Usamos el email para la autenticación
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


# Modelo Task con relación al usuario personalizado
class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Sólo auto_now_add, elimina default
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}, {self.content}'