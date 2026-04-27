from django.db import models
from django.conf import settings
from django.utils import timezone

# -------------------------
# CATÁLOGOS
# -------------------------

class ItemCategory(models.Model):
    category = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category


class ItemColor(models.Model):
    color = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.color


class CampusZone(models.Model):
    zone = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.zone

# -------------------------
# ITEM
# -------------------------

class Item(models.Model):
    class Status(models.TextChoices):
        LOST = 'Lost', 'Perdido'
        FOUND = 'Found', 'Encontrado'

    name = models.CharField(max_length=255, verbose_name="Nombre del objeto")
    description = models.TextField(blank=True, verbose_name="Descripción del objeto")
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, verbose_name="Categoría")
    color = models.ForeignKey(ItemColor, on_delete=models.CASCADE, verbose_name="Color")
    zone = models.ForeignKey(CampusZone, on_delete=models.CASCADE, verbose_name="Zona")
    image = models.ImageField(upload_to='items/', verbose_name="Imagen del objeto")
    lost_date = models.DateTimeField(default=timezone.now, verbose_name="Fecha en que se perdió")
    contact_info = models.CharField(max_length=255, verbose_name="Información de contacto")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.LOST, verbose_name="Estado del objeto")
    creator_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuario que reportó el objeto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modified = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    def __str__(self):
        return self.name

# -------------------------
# CLAIM
# -------------------------

class Claim(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    proof_description = models.TextField()
    receipt_code = models.CharField(max_length=25, unique=True)
    resolved = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Claim {self.receipt_code}"