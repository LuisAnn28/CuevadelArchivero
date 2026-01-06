from django import forms
from .models import Libro 

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'anio', 'genero']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input'}),
            'autor': forms.TextInput(attrs={'class': 'input'}),
            'anio': forms.DateInput(attrs={'type': 'input'}),
            'genero': forms.TextInput(attrs={'class': 'input'}),
        }