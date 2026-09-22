from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'estado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Diseñar nueva landing page'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'Añade notas o detalles de la tarea (opcional)...'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }