from django import forms
from .models import Ciudad

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre', 'region', 'poblacion', 'lugares_turisticos']
        widgets = {
            'lugares_turisticos': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'nombre': 'Nombre de la Ciudad',
            'region': 'Región',
            'poblacion': 'Población',
            'lugares_turisticos': 'Lugares Turísticos'
        }