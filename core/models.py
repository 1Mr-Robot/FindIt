from django.db import models
from django.conf import settings
from django.utils import timezone

# -------------------------
# CATÁLOGOS
# -------------------------

class ItemCategory(models.Model):
    category = models.CharField(max_length=255, unique=True, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modified = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Categoría de objeto"
        verbose_name_plural = "Categorías de objetos"

    def __str__(self):
        return self.category


class ItemColor(models.Model):
    color = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modified = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Color de objeto"
        verbose_name_plural = "Colores de objetos"

    def __str__(self):
        return self.color


class CampusZone(models.Model):
    zone = models.CharField(max_length=255, unique=True, verbose_name="Nombre")
    description = models.TextField(blank=True, verbose_name="Descripción")
    is_active = models.BooleanField(default=True, verbose_name="Activa")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modified = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Zona del campus"
        verbose_name_plural = "Zonas del campus"

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

    class Meta:
        verbose_name = "Objeto"
        verbose_name_plural = "Objetos"

    def __str__(self):
        return self.name