from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_tuition(value):
    pattern = r'^[12]\d{6}$'  # 1 o 2 + 6 dígitos = 7 en total
    if not re.match(pattern, value):
        raise ValidationError('La matrícula debe tener 7 dígitos y empezar con 1 o 2')

def validate_uanl_email(value):
    pattern = r'^[\w\.-]+@uanl\.edu\.mx$'
    if not re.match(pattern, value):
        raise ValidationError('El correo debe ser institucional (@uanl.edu.mx)')

class CustomUserManager(BaseUserManager):
    def create_user(self, institutional_email, password=None, **extra_fields):
        if not institutional_email:
            raise ValueError("El email institucional es obligatorio")

        user = self.model(
            institutional_email=self.normalize_email(institutional_email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, institutional_email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(institutional_email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    institutional_email = models.EmailField(unique=True, validators=[validate_uanl_email])
    tuition = models.CharField(max_length=7, unique=True, validators=[validate_tuition])
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'institutional_email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'tuition']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.institutional_email})"