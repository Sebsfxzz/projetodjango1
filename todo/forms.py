from django import forms
from .models import Tarea
class tareaForm(forms.ModelForm):
    class Meta:
        model:Tarea
        fields=["tarea"]