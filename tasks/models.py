from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.utils import timezone
# Administrador personalizado para el modelo de usuario
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, age=0, **extra_fields):
        """
        Crea y devuelve un usuario con correo electrónico, nombre de usuario y contraseña.
        """
        if not email:
            raise ValueError("El correo electrónico es obligatorio")
        if not username:
            raise ValueError("El nombre de usuario es obligatorio")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            age=age,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        Crea y devuelve un superusuario con permisos correspondientes.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_superuser'):
            raise ValueError("El superusuario debe tener 'is_superuser=True'.")
        if not extra_fields.get('is_staff'):
            raise ValueError("El superusuario debe tener 'is_staff=True'.")

        return self.create_user(email, username, password, **extra_fields)

# Modelo de usuario personalizado
class CustomUser(AbstractBaseUser, PermissionsMixin):
    #username = models.CharField(max_length=150, unique=True, verbose_name="Nombre de usuario")
    username = models.CharField(('username'), max_length=150, default='')
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    age = models.PositiveIntegerField(default=0, verbose_name="Edad")
    is_superuser = models.BooleanField(default=False, verbose_name="Es superusuario")
    is_staff = models.BooleanField(default=False, verbose_name="Es personal")
    is_active = models.BooleanField(default=True, verbose_name="Está activo")
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    objects = CustomUserManager()

    #USERNAME_FIELD = 'email'  # Campo utilizado para iniciar sesión
    #REQUIRED_FIELDS = ['username']  # Campos requeridos además del email
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.email

# Modelo Task con relación al usuario personalizado
class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Relación con el modelo de usuario personalizado
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Propietario"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    def __str__(self):
        return self.title
