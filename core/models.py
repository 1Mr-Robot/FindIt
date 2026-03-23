from django.db import models
from django.conf import settings

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


class ItemStatus(models.Model):
    status = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

# -------------------------
# ITEM
# -------------------------

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    color = models.ForeignKey(ItemColor, on_delete=models.CASCADE)
    zone = models.ForeignKey(CampusZone, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items/')
    found_date = models.DateTimeField(default=models.functions.Now)
    status = models.ForeignKey(ItemStatus, on_delete=models.CASCADE)
    creator_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

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
    resolved = models.DateTimeField(default=models.functions.Now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Claim {self.receipt_code}"