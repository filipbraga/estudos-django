from django import forms
from .models import RegistroEstudo

class RegistroEstudoForm(forms.ModelForm):
    class Meta:
        model = RegistroEstudo
        fields = ['titulo_aula', 'resumo', 'dificuldade']