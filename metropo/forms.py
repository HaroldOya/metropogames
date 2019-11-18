from django import forms
from .models import Juego

class PostForm(forms.ModelForm):

    class Meta:
        model = Juego
        fields = ('id_juego', 'nombre','genero','annio_publicacion','descripcion',)
        widgets = {
            'id_juego': forms.TextInput(attrs={'class':'form'}),
            'nombre': forms.TextInput(attrs={'class':'Form'}),
            'genero': forms.TextInput(attrs={'class':'Form'}),
            'annio_publicacion': forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'Form','placeholder':'MM/DD/YYYY'}),
            'descripcion': forms.TextInput(attrs={'class':'Form'}),
        }