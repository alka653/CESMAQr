from django import forms

from .models import *

class ReporteForm(forms.Form):
	estudiante = forms.ModelChoiceField(Estudiantes.objects.all(), empty_label = 'Todos los alumnos', label = 'Estudiante', widget = forms.Select(attrs = {'class': 'form-control', 'id': 'id_estudiante', 'required': False}))
	fecha_inicio = forms.CharField(label = 'Fecha de inicio', widget = forms.DateInput(attrs = {'type': 'date', 'class': 'form-control', 'id': 'id_fecha_inicio', 'required': True}))
	fecha_final = forms.CharField(label = 'Fecha final', widget = forms.DateInput(attrs = {'type': 'date', 'class': 'form-control', 'id': 'id_fecha_final', 'required': True}))