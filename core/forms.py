from django import forms
from .models import Item, ItemCategory, ItemColor, CampusZone
from django.utils import timezone

class LostItemForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del objeto",
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-white/10 border border-white/30 rounded-lg text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-brandGreen focus:border-transparent transition-all',
            'placeholder': 'Ej: Laptop, Celular, Llaves, etc.'
        })
    )
    description = forms.CharField(
        label="Descripción",
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-3 bg-white/10 border border-white/30 rounded-lg text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-brandGreen focus:border-transparent transition-all resize-none',
            'rows': 4,
            'placeholder': 'Describe características adicionales del objeto...'
        })
    )
    category = forms.ModelChoiceField(
        label="Categoría",
        queryset=ItemCategory.objects.all(),
        empty_label="Selecciona una categoría",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-3 bg-white/10 border border-white/30 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-brandGreen focus:border-transparent transition-all appearance-none cursor-pointer'
        })
    )
    color = forms.ModelChoiceField(
        label="Color",
        queryset=ItemColor.objects.all(),
        empty_label="Selecciona un color",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-3 bg-white/10 border border-white/30 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-brandGreen focus:border-transparent transition-all appearance-none cursor-pointer'
        })
    )
    zone = forms.ModelChoiceField(
        label="Zona del campus",
        queryset=CampusZone.objects.filter(is_active=True),
        empty_label="Selecciona una zona",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-3 bg-white/10 border border-white/30 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-brandGreen focus:border-transparent transition-all appearance-none cursor-pointer'
        })
    )
    image = forms.ImageField(
        label="Fotografía del objeto",
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'hidden',
            'accept': 'image/*',
            'onchange': 'previewImage(event)'
        })
    )
    lost_date = forms.DateTimeField(
        label="Fecha en que se perdió",
        initial=timezone.now,
        widget=forms.DateTimeInput(attrs={
            'class': 'w-full px-4 py-3 bg-white/10 border border-white/30 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-brandGreen focus:border-transparent transition-all',
            'type': 'datetime-local'
        })
    )
    contact_info = forms.CharField(
        label="Información de contacto",
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-white/10 border border-white/30 rounded-lg text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-brandGreen focus:border-transparent transition-all',
            'placeholder': 'Teléfono, correo o ambos'
        })
    )

    class Meta:
        model = Item
        fields = ["name", "description", "category", "color", "zone", "image", "lost_date", "contact_info"]