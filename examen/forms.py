from django import forms

from .models import usuario, examenes, servicios

class pacienteForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = '__all__'

class examenesForm(forms.ModelForm):
    class Meta:
        model = examenes
        fields = '__all__'
        
class agendaForm(forms.ModelForm):
    class Meta:
        model = servicios
        fields = '__all__'
        